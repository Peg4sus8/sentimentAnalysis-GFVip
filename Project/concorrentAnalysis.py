import spacy as spacy

from capture import *

# print("Analisi più dettagliata dei Tweet")
nlp = spacy.load('it_core_news_sm')

print(concGF)
for tweet in tweets:
    concGF_clone = copy.deepcopy(concGF)
    doc = nlp(tweet.getText())
    """print("TWEET: ")
    print("Testo tweet: " + tweet.getText())
    print("Sentiment: " + str(tweet.getSentiment()))
    """
    ents = []
    for entity in doc.ents:
        for concorrente in concGF:
            # non mettiamo il break, a fine 'if', poichè all'interno di un soggetto potrebbero esserci più concorrenti e quindi vogliamo
            # prima estrapolare tutti i concorrenti dal soggetto e poi andare avanti col prossimo soggetto
            if (concorrente.getName().upper() in entity.text.upper()) and (concorrente in concGF_clone):
                if (concorrente.getName().upper() == "EDOARDO") or (concorrente.getName().upper() == "LUCA") or \
                        (concorrente.getName() == "Edoardo") or (concorrente.getName() == "Luca"):
                    if concorrente.getCognome().upper() in entity.text.upper():
                        conc = concorrente.getName()
                        conc += " " + concorrente.getCognome()
                        ents.append(conc)
                        concorrente.addScore(tweet.getSentiment())
                        concGF_clone.pop(concGF_clone.index(concorrente))
                else:
                    ents.append(concorrente.getName())
                    concorrente.addScore(tweet.getSentiment())
                    concGF_clone.pop(concGF_clone.index(concorrente))
                    # print("text: " + entity.text, ", concorrente_name: " + concorrente.getName())
        print(entity)
                # print("FINE " + "text: " + entity.text, "type/label: " + entity.label_)

    tweet.setEnts(ents)

""" print("Ents: " + str(tweet.getEnts()))
    print()"""

"""print("LISTA CON PUNTEGGI")
for c in concGF:
    print("Name: " + c.getName())
    print("score_negativo: " + str(c.getScoreNegativo()))
    print("score_tendente_negativo: " + str(c.getScoreTendenteNegativo()))
    print("score_neutro: " + str(c.getScoreNeutro()))
    print("score_tendente_positivo: " + str(c.getScoreTendentePositivo()))
    print("score_positivo: " + str(c.getScorePositivo()))
    print()
"""
print("Done analysis!")

from concorrentAnalysis import *
from ConcorrenteGf import *
import csv
import pandas

# Nomi dei file
name_file_tweets = "../Dataset_tweets/GFVip(" + str(date_tweepy) + ").csv"
name_file_concorrenti_score = "../Dataset_tweets/GFVip_Score_Concorrenti(" + str(date_tweepy) + ").csv"
name_file_sumScore = "../Dataset_tweets/GFVip_Score_Concorrenti.csv"

# ----------- Dataset -----------
print(f"\n---Writing in file '{name_file_tweets}' ...")

# Creazione nostro file dove salveremo tutti i tweets con le relative informazioni
csv_file = open(name_file_tweets, "w", encoding='utf-8', newline='')
writer = csv.writer(csv_file)
head1 = ["Id", "Screen_name", "Created_at", "Retweet", "Text", "Hashtags", "Sentiment", "Compound", "Ents"]
writer.writerow(head1)

def converto_in_list(lista):
    stringa = ""
    for i in range(len(lista)):
        if (i == len(lista)-1):
            stringa += str(lista[i])
        elif (i < len(lista)-1):
            stringa += str(lista[i]) + ";"

    return stringa


# Aggiunta dei tweets nel file CSV
for t in tweets:
    lista_ents = converto_in_list(t.getEnts())
    writer.writerow([str(t.getId()), str(t.getScreen_name()), str(t.getCreated_at()), str(t.getRetweet()), str(t.getText()),
                     str(t.getHashtags()), str(t.getSentiment()), str(t.getCompound()), lista_ents])
csv_file.close()

print(f"---File '{name_file_tweets}' writing completed!---")

# ----------- Concorrenti: Score quotidiano -----------
print(f"\n---Writing in file '{name_file_concorrenti_score}' ...")
# Creazione nostro file dove salveremo gli score di ogni concorrente
csv_file = open(name_file_concorrenti_score, "w", encoding='utf-8', newline='')
writer = csv.writer(csv_file)
head2 = ["Name", "Cognome", "score_negativo","score_tendente_negativo","score_neutro","score_tendente_positivo","score_positivo"]
writer.writerow(head2)

# Aggiunta dei concorrenti con i relativi score nel file CSV
for c in concGF:
    writer.writerow([str(c.getName()), str(c.getCognome()), str(c.getScoreNegativo()), str(c.getScoreTendenteNegativo()), str(c.getScoreNeutro()), str(c.getScoreTendentePositivo()),
                     str(c.getScorePositivo())])
csv_file.close()

print(f"---File '{name_file_concorrenti_score}' writing completed!---")

# -------- Concorrenti: Score generale --------
print(f"\n---Editing in file '{name_file_sumScore}' ...")
df = pandas.read_csv(name_file_sumScore, header=0, delimiter=";")
df2 = pandas.read_csv(name_file_concorrenti_score, header=0, delimiter=";")
n = df.to_numpy()
n2 = df2.to_numpy()
concTot = []
concParz = []
for i in range(n.shape[0]):
    l = ConcorrenteGF(n[i, 0], n[i, 1])
    l.setScoreNegativo(n[i, 2])
    l.setScoreTendenteNegativo(n[i, 3])
    l.setScoreNeutro(n[i, 4])
    l.setScoreTendentePositivo(n[i, 5])
    l.setScorePositivo(n[i, 6])
    l.calculateRank()
    concTot.append(l)

for j in range(n2.shape[0]):
    t = ConcorrenteGF(n2[j, 0], n2[j, 1])
    t.setScoreNegativo(n2[j, 2])
    t.setScoreTendenteNegativo(n2[j, 3])
    t.setScoreNeutro(n2[j, 4])
    t.setScoreTendentePositivo(n2[j, 5])
    t.setScorePositivo(n2[j, 6])
    concParz.append(t)

for x in range(len(concTot)):
    concTot[x].setScoreNegativo(concTot[x].getScoreNegativo() + concParz[x].getScoreNegativo())
    concTot[x].setScoreTendenteNegativo(concTot[x].getScoreTendenteNegativo() + concParz[x].getScoreTendenteNegativo())
    concTot[x].setScoreNeutro(concTot[x].getScoreNeutro() + concParz[x].getScoreNeutro())
    concTot[x].setScoreTendentePositivo(concTot[x].getScoreTendentePositivo() + concParz[x].getScoreTendentePositivo())
    concTot[x].setScorePositivo(concTot[x].getScorePositivo() + concParz[x].getScorePositivo())
    concTot[x].calculateRank()


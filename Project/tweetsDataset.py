from main import *
import csv

# Nomi dei file
name_file_tweets = "./Dataset_tweets/GFVip(" + str(date_tweepy) + ").csv"
name_file_concorrenti_score = "./Dataset_tweets/GFVip_Score_Concorrenti(" + str(date_tweepy) + ").csv"
name_file_sumScore = "./Dataset_tweets/GFVip_Score_Concorrenti.csv"
# ----------- 1 parte -----------
print(f"\n---Writing in file '{name_file_tweets}' ...---")

# Creazione nostro file dove salveremo tutti i tweets con le relative informazioni
csv_file = open(name_file_tweets, 'w', encoding='utf-8', newline='')
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

# ----------- 2 parte -----------
print(f"\n---Writing in file '{name_file_concorrenti_score}' ...---")
# Creazione nostro file dove salveremo gli score di ogni concorrente
csv_file = open(name_file_concorrenti_score, 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
head2 = ["Name_concorrente","score_negativo","score_tendente_negativo","score_neutro","score_tendente_positivo","score_positivo"]
writer.writerow(head2)

# Aggiunta dei concorrenti con i relativi score nel file CSV
for c in concGF:
    writer.writerow([str(c.getName()), str(c.getScoreNegativo()), str(c.getScoreTendenteNegativo()), str(c.getScoreNeutro()), str(c.getScoreTendentePositivo()),
                     str(c.getScorePositivo())])
csv_file.close()

print(f"---File '{name_file_concorrenti_score}' writing completed!---")
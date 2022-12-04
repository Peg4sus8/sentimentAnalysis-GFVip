from concorrentAnalysis import *
from ConcorrenteGf import *
import csv
import pandas

# Nomi dei file

name_file_tweets = "../Dataset_tweets/GFVip(" + str(date_tweepy) + ").csv"
name_file_concorrenti_score = "../Dataset_users/GFVip_Score_Concorrenti(" + str(date_tweepy) + ").csv"
name_file_sumScore = "../Dataset_users/GFVip_Score_Concorrenti.csv"

# ----------- Dataset -----------
print(f"\n---Writing in file '{name_file_tweets}' ...")

# ------ Creazione file ------
csv_file = open(name_file_tweets, "w", encoding='utf-8', newline='')
writer = csv.writer(csv_file)
head1 = ["Id", "Screen_name", "Created_at", "Retweet", "Text", "Hashtags", "Sentiment", "Compound", "Ents"]
writer.writerow(head1)


def converto_in_list(lista):
    stringa = ""
    for i in range(len(lista)):
        if (i == len(lista) - 1):
            stringa += str(lista[i])
        elif (i < len(lista) - 1):
            stringa += str(lista[i]) + ";"

    return stringa

    # ------ Aggiunta dei concorrenti con i relativi score nel file CSV

for t in tweets:
    lista_ents = converto_in_list(t.getEnts())
    writer.writerow(
        [str(t.getId()), str(t.getScreen_name()), str(t.getCreated_at()), str(t.getRetweet()), str(t.getText()),
         str(t.getHashtags()), str(t.getSentiment()), str(t.getCompound()), lista_ents])
csv_file.close()
# -------- Fine --------

print(f"---File '{name_file_tweets}' writing completed!---")

# ----------- Concorrenti: Score quotidiano -----------
# ------ Creazione file ------
print(f"\n---Writing in file '{name_file_concorrenti_score}' ...")
csv_file = open(name_file_concorrenti_score, "w", encoding='utf-8', newline='')
writer = csv.writer(csv_file)
head2 = ["Name", "Cognome", "score_negativo", "score_tendente_negativo", "score_neutro", "score_tendente_positivo",
         "score_positivo", "rank"]
writer.writerow(head2)

# ------ Aggiunta dei concorrenti con i relativi score nel file CSV
for c in concGF:
    writer.writerow(
        [str(c.getName()), str(c.getCognome()), str(c.getScoreNegativo()), str(c.getScoreTendenteNegativo()),
         str(c.getScoreNeutro()), str(c.getScoreTendentePositivo()),
         str(c.getScorePositivo()), str(c.calculateRank())])
csv_file.close()
# -------- Fine --------

print(f"---File '{name_file_concorrenti_score}' writing completed!---")

# -------- Concorrenti: Score generale --------
# ------ Creazione file ------
print(f"\n---Writing in file '{name_file_sumScore}' ...")

csv_file = open(name_file_sumScore, "w", encoding='utf-8', newline='')
writer = csv.writer(csv_file)
head3 = head3 = ["Name", "Cognome", "score_negativo", "score_tendente_negativo", "score_neutro", "score_tendente_positivo",
         "score_positivo", "rank"]
writer.writerow(head3)
for c in concGF:
    writer.writerow(
        [str(c.getName()), str(c.getCognome()), str(c.getScoreNegativo()), str(c.getScoreTendenteNegativo()),
         str(c.getScoreNeutro()), str(c.getScoreTendentePositivo()),
         str(c.getScorePositivo()), str(c.getRank())])
csv_file.close()

# ------ Aggiornamento ------
print(f"\n---Editing in file '{name_file_sumScore}' ...")
concTot = []
concParz = []
colonne = ["Name", "Cognome", "score_negativo", "score_tendente_negativo", "score_neutro", "score_tendente_positivo",
         "score_positivo", "rank"]

# ---- raccolta dati ----
with open(name_file_sumScore, mode="r", encoding='UTF8') as csv_read:
    reader = csv.reader(csv_read, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            pass
        else:
            l = ConcorrenteGF(row[0], row[1])
            l.setScoreNegativo(row[2])
            l.setScoreTendenteNegativo(row[3])
            l.setScoreNeutro(row[4])
            l.setScoreTendentePositivo(row[5])
            l.setScorePositivo(row[6])
            l.setRank(row[7])
            concTot.append(l)
        line_count += 1
    csv_read.close()

with open(name_file_concorrenti_score, mode="r", encoding='UTF8') as halfCsv:
    reader = csv.reader(halfCsv, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            pass
        else:
            l = ConcorrenteGF(row[0], row[1])
            l.setScoreNegativo(row[2])
            l.setScoreTendenteNegativo(row[3])
            l.setScoreNeutro(row[4])
            l.setScoreTendentePositivo(row[5])
            l.setScorePositivo(row[6])
            l.setRank(row[7])
            concParz.append(l)
        line_count += 1
    halfCsv.close()

    # ---- Calcolo rank e scrittura ----
with open(name_file_sumScore, mode="w", encoding='UTF8', newline='') as csv_write:
    writer = csv.writer(csv_write)
    head3 = ["Name", "Cognome", "score_negativo", "score_tendente_negativo", "score_neutro", "score_tendente_positivo",
             "score_positivo", "rank"]
    writer.writerow(head3)
    for x in range(len(concTot)):
        concTot[x].setScoreNegativo(concTot[x].getScoreNegativo() + concParz[x].getScoreNegativo())
        concTot[x].setScoreTendenteNegativo(
            concTot[x].getScoreTendenteNegativo() + concParz[x].getScoreTendenteNegativo())
        concTot[x].setScoreNeutro(concTot[x].getScoreNeutro() + concParz[x].getScoreNeutro())
        concTot[x].setScoreTendentePositivo(
            concTot[x].getScoreTendentePositivo() + concParz[x].getScoreTendentePositivo())
        concTot[x].setScorePositivo(concTot[x].getScorePositivo() + concParz[x].getScorePositivo())
        concTot[x].setRank(concTot[x].getRank() + concParz[x].getRank())
        writer.writerow(
            [str(concTot[x].getName()), str(concTot[x].getCognome()), str(concTot[x].getScoreNegativo()),
             str(concTot[x].getScoreTendenteNegativo()), str(concTot[x].getScoreNeutro()),
             str(concTot[x].getScoreTendentePositivo()), str(concTot[x].getScorePositivo()),
             str(concTot[x].getRank())])

# -------- fine --------

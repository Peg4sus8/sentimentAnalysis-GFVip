import csv
from ConcorrenteGf import ConcorrenteGF

yesterday = "../Dataset_users/GFVip_Score_Concorrenti.csv"
today = "../Dataset_users/GFVip_Score_Concorrenti(2022-12-04).csv"
sumFile = "../Dataset_users/GFVip_Score_Concorrenti.csv"

yesConc = []
todConc = []

# ---- raccolta dati ----
with open(today, mode="r", encoding='UTF8') as csv_read:
    reader = csv.reader(csv_read, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            pass
        else:
            p = ConcorrenteGF(row[0], row[1])
            p.setScoreNegativo(row[2])
            p.setScoreTendenteNegativo(row[3])
            p.setScoreNeutro(row[4])
            p.setScoreTendentePositivo(row[5])
            p.setScorePositivo(row[6])
            p.setRank(row[7])
            todConc.append(p)
        line_count += 1
    csv_read.close()

with open(yesterday, mode="r", encoding='UTF8') as halfCsv:
    reader = csv.reader(halfCsv, delimiter=',')
    line_count = 0
    for line in reader:
        if line_count == 0:
            pass
        else:
            g = ConcorrenteGF(line[0], line[1])
            g.setScoreNegativo(line[2])
            g.setScoreTendenteNegativo(line[3])
            g.setScoreNeutro(line[4])
            g.setScoreTendentePositivo(line[5])
            g.setScorePositivo(line[6])
            g.setRank(line[7])
            yesConc.append(g)

        line_count += 1
    halfCsv.close()

    # ---- Calcolo rank e scrittura ----
with open(sumFile, mode="w", encoding='UTF8', newline='') as csv_write:
    writer = csv.writer(csv_write)
    head3 = ["Name", "Cognome", "score_negativo", "score_tendente_negativo", "score_neutro", "score_tendente_positivo",
             "score_positivo", "rank"]
    writer.writerow(head3)
    for x in range(len(todConc)):
        todConc[x].setScoreNegativo(float(todConc[x].getScoreNegativo()) + float(yesConc[x].getScoreNegativo()))
        todConc[x].setScoreTendenteNegativo(
            float(todConc[x].getScoreTendenteNegativo()) + float(yesConc[x].getScoreTendenteNegativo()))
        todConc[x].setScoreNeutro(float(todConc[x].getScoreNeutro()) + float(yesConc[x].getScoreNeutro()))
        todConc[x].setScoreTendentePositivo(
            float(todConc[x].getScoreTendentePositivo()) + float(yesConc[x].getScoreTendentePositivo()))
        todConc[x].setScorePositivo(float(todConc[x].getScorePositivo()) + float(yesConc[x].getScorePositivo()))
        todConc[x].setRank(float(todConc[x].getRank()) + float(yesConc[x].getRank()))
        print(todConc[x].getRank())
        writer.writerow(
            [str(todConc[x].getName()), str(todConc[x].getCognome()), str(todConc[x].getScoreNegativo()),
             str(todConc[x].getScoreTendenteNegativo()), str(todConc[x].getScoreNeutro()),
             str(todConc[x].getScoreTendentePositivo()), str(todConc[x].getScorePositivo()),
             str(todConc[x].getRank())])

from ConcorrenteGf import *
import pandas

# andiamo a registrare tutti concorrenti del GF Vip prendendo i nomi dal file
inputFile = "sentimentAnalysis-GFVip/concorrentiGF.csv"
df = pandas.read_csv(inputFile, header=0, delimiter=";")

# si inseriscono le colonne del file in un oggetto numpy
# si possono inserire anche alcune colonne solo

n = df.to_numpy()
concGF = []

for i in range(n.shape[0]):
    provv = ConcorrenteGF(n[i, 0], n[i, 1])
    concGF.append(provv)

# stampa concorrenti
print("----------CONCORRENTI----------\n")
for i in range(len(concGF)):
    print("--", concGF[i].getName(), concGF[i].getCognome())

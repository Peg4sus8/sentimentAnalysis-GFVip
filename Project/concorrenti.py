import ConcorrenteGf
import numpy
import pandas

#andiamo a registrare tutti concorrenti del GF Vip prendendo i nomi dal file
inputFile = "../concorrentiGF.csv"
df = pandas.read_csv(inputFile, header = 0, delimiter = ";")

#si inseriscono le colonne del file in un oggetto numpy
#si possono inserire anche alcune colonne solo
n = df.to_numpy()

conc_GF = []

for i in range(n.shape[0]):
    provv = ConcorrenteGf(n[i, 0], n[i, 1])
    conc_GF.append(provv)

#nel for in cui si assegnano nome e cognome;
# conc_GF.append(ConcorrenteGF(nome, cognome))
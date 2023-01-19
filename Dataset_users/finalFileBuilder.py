import os
import csv
import datetime
import pandas as pd

pathName = "./DailyCap/GFVip_Score_Concorrenti("
endPathName = ").csv"
date = datetime.date(2022, 11, 27)
argument = []
first = False

for i in range(33):
    df = pd.read_csv(pathName + str(date) + endPathName, header=0, delimiter=",")
    arr = df.to_numpy()
    for j in range(arr.shape[0]):            #Per ogni riga in array
        if i == 0:
            argument += [[arr[j, 0], arr[j, 1], arr[j, 7]]]
        else:
            argument += [str(arr[j, 7])]

    if i == 0:
        finalDF = pd.DataFrame(argument, columns=['NOME', 'COGNOME', date])
    else:
        finalDF.loc[:, str(date)] = argument

    date = date + datetime.timedelta(days=1)
    argument = []

finalDF.to_csv("./FinalFiles/finalFile.csv", index=False)
print(finalDF)


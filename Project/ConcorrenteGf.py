class ConcorrenteGF:
    # Metodo costruttore
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.score_negativo = 0
        self.score_tendente_negativo = 0
        self.score_neutro = 0
        self.score_tendente_positivo = 0
        self.score_positivo = 0

    # Metodi getter
    def getName(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getScoreNegativo(self):
        return self.score_negativo

    def getScoreTendenteNegativo(self):
        return self.score_tendente_negativo

    def getScoreNeutro(self):
        return self.score_neutro

    def getScoreTendentePositivo(self):
        return self.score_tendente_positivo

    def getScorePositivo(self):
        return self.score_positivo

    # Metodi setter
    def setNome(self, nome):
        self.nome = nome

    def setCognome(self, cognome):
        self.cognome = cognome

    def setScoreNegativo(self, score):
        self.score_negativo = score

    def setScoreTendenteNegativo(self, score):
        self.score_tendente_negativo = score

    def setScoreNeutro(self, score):
        self.score_neutro = score

    def setScoreTendentePositivo(self, score):
        self.score_tendente_positivo = score

    def setScorePositivo(self, score):
        self.score_positivo = score

    # metodi utili
    def addScore(self, type:int):
        int(type)
        if (type == 1):
            self.score_negativo += 1
        elif (type == 2):
            self.score_tendente_negativo += 1
        elif (type == 3):
            self.score_neutro += 1
        elif (type == 4):
            self.score_tendente_positivo += 1
        elif (type == 5):
            self.score_positivo += 1
        elif ():
            print("ERRORE IN FUNZIONE 'addScore' di 'Concorrente_Amici'\n")

    def calculateRank(self):
        rank = 0.0
        rank += float(self.getScoreNegativo() * (-1))
        rank += float(self.getScoreTendenteNegativo() * (-0.5))
        rank += float(self.getScoreNeutro() * 0)
        rank += float(self.getScoreTendentePositivo() * 0.5)
        rank += float(self.getScorePositivo() * 1)

        return rank

    # metodi Object
    def __eq__(self, o: object):
        if isinstance(o, ConcorrenteGF):
            return (o.nome == self.nome) and (o.cognome == self.cognome)

    def __str__(self):
        return f"Concorrente: {self.getName()} {self.cognome} \n"   \
            f"Score negativo: {self.getScoreNegativo}\n"    \
            f"Score tendente-negativo: {self.getScoreTendenteNegativo()}\n" \
            f"Score neutro: {self.getScoreNeutro()}\n"  \
            f"Score tendente-positivo: {self.getScoreTendentePositivo()}\n" \
            f"Score positivo: {self.getScorePositivo()}\n"

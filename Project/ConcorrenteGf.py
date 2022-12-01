class ConcorrenteGF:
    # Metodo costruttore
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.score_negativo = 0.0
        self.score_tendente_negativo = 0.0
        self.score_neutro = 0.0
        self.score_tendente_positivo = 0.0
        self.score_positivo = 0.0
        self.rank = 0.0
        self.buildHashtag()

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

    def getHashtags(self):
        return self.hashtags

    def getRank(self):
        return self.rank

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

    def setRank(self, rank):
        self.rank = rank
    # metodi utili
    def buildHashtag(self):
        self.hashtags = []
        provv = "#"
        if self.getName()!="Luca" or self.getName()!="Edoardo":
            provv += self.getName()
            self.hashtags.append(provv)
        else:
            provv += self.getCognome()
            self.hashtags.append(self.cognome)

        if self.getCognome() == "Incorvaia" or self.getCognome() == "Tavassi":
            self.hashtags.append("#incorvassi")
        if self.getCognome() == "De Pisis":
            self.hashtags.append("#thepisis")
        if self.getCognome() == "Fiordelisi" or self.getCognome() == "Donnamaria":
            self.hashtags.append("#donnalisi")
        if self.getName() == "Nikita":
            self.hashtags.append("#nikiters")



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
        self.rank += float(self.getScoreNegativo() * (-1))
        self.rank += float(self.getScoreTendenteNegativo() * (-0.5))
        self.rank += float(self.getScoreNeutro() * 0)
        self.rank += float(self.getScoreTendentePositivo() * 0.5)
        self.rank += float(self.getScorePositivo() * 1)

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

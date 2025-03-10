import operator
from dataclasses import dataclass

cfuTot = 180

@dataclass(order = True)
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    def copy(self):
        return Voto(self.materia, self.punteggio, self.data, self.lode)

    def __eq__(self, other):
        if (self.materia == other.materia and
            self.punteggio == other.punteggio and
            self.lode == other.lode):
            return True
        return False

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto): # duck!
        if (self.hasConflitto(voto) == False
            and self.hasVoto(voto) == False):
            self.voti.append(voto)
        else:
            raise ValueError("Il voto è già presente")

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario} \n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr

    def __len__(self):
        return len(self.voti)

    def calcolaMedia(self):
        '''
        Restituisce la media dei voti attualmente presenti nel Libretto
        :return: valore numerico della media oppure ValueError (nel caso la lista fosse vuota)
        '''

        #media = sommaVoti / numeroEsami
        #v = []
        #for voto in self.voti:
        #    v.append(voto.calcolaMedia())

        if len(self.voti) == 0:
            raise ValueError("Attenzione, lista esami vuota!")

        v = [voto.punteggio for voto in self.voti]
        media = sum(v) / len(v)
        return media
        #return math.mean(v)

    def getVotiByPunti(self, punti, lode):
        '''
        Restituisce una lista di voti in cui si ha ottenuto il punteggio
        uguale a punti (e lode, se applicabile)
        :param punti: punteggio ottenuto in esame
        :param lode:
        :return: lista di voti
        '''

        votiFiltrati = []
        for voto in self.voti:
            if voto.punteggio == punti and voto.lode == lode:
                votiFiltrati.append(voto)

        return votiFiltrati

    def getVotoByName(self, nome):
        '''
        Restituisce un oggetto Voto il cui campo materia è uguale a nome
        :param nome: stringa che indica il nome della materia
        :return: oggetto di tipo Voto oppure None (se voto non trovato)
        '''

        for voto in self.voti:
            if voto.materia == nome:
                return voto

    def hasVoto(self, voto):
        '''
        Verifica se il libretto contiene già il voto. Due voti sono considerati uguali
        se hanno lo stesso campo materia e lo stesso campo punteggio (punteggio + lode).
        :param voto: intero indicante il voto conseguito
        :param lode: bool che indica presenza della lode
        :return: True se già presente, False altrimenti
        '''

        for v in self.voti:
            if v == voto: #ho definito il __eq__ in voto
                return True
        return False

    def hasConflitto(self, voto):
        '''
        Questo metodo controlla che il voto "voto" non rappresenti un conflitto con
        i voti già presenti nel libretto. Consideriamo due voti in conflitto quando
        hanno lo stesso campo materia ma diversa coppia (punteggio, lode)
        :param voto: istanza della classe Voto
        :return: True se in conflitto, False altrimenti
        '''

        for v in self.voti:
            if (v.materia == voto. materia
                    and not (v.punteggio == voto.punteggio and v.lode == voto.lode)):
                return True
        return False

    def copy(self):
        '''
        Crea una nuova copia del libretto
        :return: istanza della classe Libretto
        '''
        nuovo = Libretto(self.proprietario, [])
        for v in self.voti:
            nuovo.append(v.copy())
        return nuovo

    def creaMigliorato(self):
        '''
        Crea un nuovo oggetto Libretto, in cui i voti sono migliorati secondo
        la seguente logica :
        se il voto è >= 18 e < 24 aggiungo +1
        se il voto è >= 24 e < 29 aggiungo +2
        se il voto è 29 aggiungo +1
        se il voto è 30 rimane 30
        :return: nuovo Libretto
        '''

        nuovo = self.copy() # definito metodo copy sopra in Libretto
        #modifico i voti in nuovo

        for v in nuovo.voti:
            if 18 <= v.punteggio < 24:
                v.punteggio += 1
            elif 24 <= v.punteggio < 29:
                v.punteggio += 2
            elif 29 <= v.punteggio < 30:
                v.punteggio = 30

        return nuovo

    def sortByMateria(self):
        # self.voti.sort(key = estraiMateria)
        self.voti.sort(key = operator.attrgetter('materia'))
#     Opzione 1 : creo due metodi di stampa che prima ordinano e poi stampano
#     Opzione 2 : creo due metodi che ordinano la lista di self e poi un metodo unico che stampa
#     Opzione 3 : creo due metodi che fanno una copia della lista, la ordinano e poi la resituitscono
#                 e poi un altro metodo che stampa
#     Opzione 4 : creo una shallow copy di self.voti e ordino

    def sortByVoto(self):
        self.voti.sort(key = operator.attrgetter('voto'))

    def creaLibOrdinatoPerMateria(self):
        '''
        Crea un nuovo oggetto Libretto e lo ordina per materia
        :return: nuova istanza dell'oggetto Libretto
        '''

        nuovo = self.copy()
        nuovo.sortByMateria()
        return nuovo

    def creaLibOrdinatoPerVoto(self):
        '''
        Crea un nuovo oggetto Libretto e lo ordina per voto
        :return: nuova istanza dell'oggetto Libretto
        '''
        nuovo = self.copy()
        nuovo.voti.sort(key = lambda v : (v.punteggio, v.lode), reverse = True)
        return nuovo

    def cancellaInferiori(self, punteggio):
        '''
        Questo metodo agisce sul libretto corrente, eliminando tutti i voti
        inferiori al parametro indicato
        :param punteggio: intero indicante il punteggio minimo
        :return:
        '''
        # Modo 1
        # for i in range(len(self.voti)):
        #     if self.voti[i].punteggio < punteggio:
        #         self.voti.pop(i)

        # Modo 2
        # for v in self.voti:
        #     if v.punteggio < punteggio:
        #         self.voti.remove(v)

        # entrambi i primi due metodi modificano la lista iniziale

        # Modo 3
        # nuovo = []
        # for v in self.voti:
        #     if v.punteggio >= punteggio:
        #         nuovo.append(v)
        # self.voti = nuovo

        return [v for v in self.voti if v.punteggio >= punteggio]


def estraiMateria(voto):
    '''
    Questo metodo restituisce il campo materia dell'oggetto voto
    :param voto: istanza della classe Voto
    :return: stringa rappresentante il nome della materia
    '''
    return voto.materia

def testVoto():
    print("Ho usato Voto in maniera standalone")
    v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
    v2 = Voto("Pozioni", 30, "2022-02-17", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
    print(v1)

    mylib = Libretto(None, [v1, v2])
    print(mylib)
    mylib.append(v3)
    print(mylib)

if __name__ == "__main__":
    testVoto()


# class Voto:
#     def __init__(self, materia, punteggio, data, lode):
#         if  punteggio == 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = lode
#         elif punteggio < 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = False
#         else:
#             raise ValueError(f"Attenzione, non posso creare un voto con punteggio {punteggio}")
#     def __str__(self):
#         if self.lode:
#             return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
#         else:
#             return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

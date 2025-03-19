from scuola import Student
from view import View
from voto.voto import Libretto, Voto
import flet as ft


class Controller:
    def __init__(self, v: View):
        self._view = v
        self._student = Student('Harry', 'Potter', 11, 'castani', 'castani',
                'Grifondoro', 'civetta', 'Expecto Patronum')
        self._model = Libretto(self._student, [])
        self.fillLibretto()

    def handleAggiungi(self, e):
        #Raccoglie tutte le info per creare un nuovo voto
        #Crea un oggetto Voto
        #Fa append sul libretto
        nome = self._view._txtInNome.value
        if nome == "":
            self._view._txtOut.controls.append(ft.Text("Attenzione, il campo nome non può essere vuoto.", color = "red"))
            self._view._page.update()
            return

        punti = self._view.ddVoto.value
        if punti is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione, selezionare un voto.", color="red"))
            self._view._page.update()
            return

        data = self._view._dp.value
        if data is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione, selesionare una data.", color="red"))
            self._view._page.update()
            return

        if punti == "30L":
            self._model.append(Voto(nome, 30, f'{data.year}-{data.month}-{data.day}', True))
        else:
            self._model.append(Voto(nome, int(punti), f'{data.year}-{data.month}-{data.day}', False))

        self._view._txtOut.controls.append(ft.Text("Voto correttamente aggiunto", color = "green"))
        self._view._page.update()


    def handleStampa(self, e):
        self._view._txtOut.controls.append(ft.Text(str(self._model), color = "white"))
        self._view._page.update()

    def getStudent(self):
        '''
        Restituisce informazioni studente, usando il __str__ dell'oggetto Student
        :return:
        '''
        return str(self._student)

    def fillLibretto(self):
        v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)
        v2 = Voto("Babbanologia", 21, "2022-02-12", False)
        self._model.append(v1)
        self._model.append(v2)

        self._model.append(Voto("Pozioni", 21, "2022-06-14", False))
        self._model.append(Voto("Trasfigurazione", 21, "2022-06-14", False))
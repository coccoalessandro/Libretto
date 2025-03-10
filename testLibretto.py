from voto.voto import Libretto, Voto
from scuola import Student

Harry = Student('Harry', 'Potter', 11, 'castani', 'castani',
                'Grifondoro', 'civetta', 'Expecto Patronum')

myLib = Libretto(Harry, [])

v1 = Voto('Difesa contro le arti oscure', 25, '2022-01-30', False)
v2 = Voto('Babbanologia', 30, '2022-02-12', True)

myLib.append(v1)
myLib.append(v2)

myLib.append(Voto('Pozioni', 21, '2022-06-14', False))

print()
mediaVoti = myLib.calcolaMedia()
print(mediaVoti)

votiFiltrati = myLib.getVotiByPunti(21, False)
print(votiFiltrati)

votoTrasfigurazione = myLib.getVotoByName('Pozioni')
if votoTrasfigurazione is None:
    print('Voto non trovato')
else :
    print(votoTrasfigurazione)

print(f'\nVerifico metodo hasVoto:')
print(myLib.hasVoto(v1))
print(myLib.hasVoto(Voto('Aritmanzia', 30, '2023-02-20', False)))
print(myLib.hasVoto(Voto('Difesa contro le arti oscure', 25, '2022-01-30', False)))

print(f'\nVerifico metodo hasConflitto:')
print(myLib.hasConflitto(Voto('Pozioni', 20, '2022-06-14', False)))

print(f'\nTest append modificata')
myLib.append(Voto('Aritmanzia', 30, '2023-02-20', False))
# myLib.append(Voto('Difesa contro le arti oscure', 25, '2022-01-30', False)) --> DA' ERRORE (GIUSTOOO !!!)

myLib.append(Voto('Divinazione', 27, '2021-02-08', False))
myLib.append(Voto('Cura', 26, '2021-7-23', False))

print(f'\n--------------------------------------------\nTest creaMigliorato')
print(f'Libretto originale:\n{myLib}')
print(f'Libretto migliorato:\n{myLib.creaMigliorato()}')
print(f'Le due copie del libretto sono indipendenti, infatti se ristampo quello originale:\n{myLib}')

print(f'\n--------------------------------------------\nTest ordinamento materia')
ordinato = myLib.creaLibOrdinatoPerMateria()
print(ordinato)

print(f'\n--------------------------------------------\nTest ordinamento voto')
ordinatoVoti = myLib.creaLibOrdinatoPerVoto()
print(ordinatoVoti)


print(f'\n--------------------------------------------\nCancello dal libretto voti inferiori a 24')
ordinato2 = ordinatoVoti.cancellaInferiori(24)
print(ordinato2)


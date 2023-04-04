from kolegij import unos_kolegija, ispis_kolegija
from ispit import unos_ispita, ispis_ispita

kolegiji = []
ispiti = []


broj_kolegija = int(input('Unesite broj kolegija: '))
for i in range(1, broj_kolegija+1):
    kolegiji.append(unos_kolegija(i))

broj_ispita = int(input('Unesite broj ispita: '))
for i in range(1, broj_ispita+1):
    ispiti.append(unos_ispita(kolegiji, i))

for ispit in ispiti:
    ispis_ispita(ispit)



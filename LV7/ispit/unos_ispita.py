from kolegij import get_kolegij
from datetime import date
from utilities import unos_intervala, unos_datuma
from .ispit import Ispit


def unos_ispita(kolegiji, redni_broj):
    print('Popis koelgija: ')
    for i, kolegij in enumerate(kolegiji, start=1):
        print(get_kolegij(i, kolegij))

    print('Za odabir kolegija')
    odabrani_kolegij = unos_intervala(1, len(kolegiji))
    kolegij = kolegiji[odabrani_kolegij - 1]

    datum = unos_datuma(f"Unesite dan {redni_broj}. ispita: ")

    return Ispit(kolegij, datum)

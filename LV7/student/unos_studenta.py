from ispit import get_ispit
from utilities import unos_intervala
from .redovni_student import RedovniStudent
from .vanredni_student import VanredniStudent


def unos_studenta(ispiti, redni_broj):
    print('Odaberite tip studenta: ')
    print('\t1. Redovni student')
    print('\t2. Vanredni student')
    tip_studenta = int(input('Unesite tip studenta: '))

    ime = input(f"Unesite ime {redni_broj}. studenta: ").capitalize()
    prezime = input(f"Unesite prezime {redni_broj}. studenta: ").capitalize()
    for j, ispit in enumerate(ispiti, start=1):
        print(get_ispit(j, ispit))

    x = len(ispiti)
    print('Za odabir ispita')
    odabrani_ispit = unos_intervala(1, x)
    ispit = ispiti[odabrani_ispit - 1]

    if tip_studenta == 1:
        broj_prijava = int(input('Unesite broj prijava: '))
        return RedovniStudent(ime, prezime, ispit, broj_prijava)

    if tip_studenta == 2:
        return VanredniStudent(ime, prezime, ispit)
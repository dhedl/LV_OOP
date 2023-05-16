from ispit import get_ispit
from utilities import unos_intervala
from .redovni_student import RedovniStudent
from .vanredni_student import VanredniStudent
from utilities import unos_pozitivnog_cijelog_broja, unos_teksta


def unos_studenta(ispiti, redni_broj):

    ime = unos_teksta(f"Unesite ime {redni_broj}. studenta: ").capitalize()
    prezime = unos_teksta(f"Unesite prezime {redni_broj}. studenta: ").capitalize()

    for j, ispit in enumerate(ispiti, start=1):
        print(get_ispit(j, ispit))

    x = len(ispiti)
    print('Za odabir ispita')
    odabrani_ispit = unos_intervala(1, x)
    ispit = ispiti[odabrani_ispit - 1]

    print('Odaberite tip studenta: ')
    print('\t1. Redovni student')
    print('\t2. Vanredni student')
    tip_studenta = unos_pozitivnog_cijelog_broja('Unesite tip studenta: ')

    if tip_studenta == 1:
        broj_prijava = unos_pozitivnog_cijelog_broja('Unesite broj prijava: ')
        return RedovniStudent(ime, prezime, ispit, broj_prijava)

    if tip_studenta == 2:
        return VanredniStudent(ime, prezime, ispit)
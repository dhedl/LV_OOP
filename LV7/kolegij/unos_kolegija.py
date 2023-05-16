from .kolegij import Kolegij
from utilities import unos_teksta, unos_pozitivnog_cijelog_broja
def unos_kolegija(redni_broj):
    ime = unos_teksta(f"Unesite ime {redni_broj}. kolegija: ")
    ects = unos_pozitivnog_cijelog_broja(f"Unesite ECTS bodove za {redni_broj}. kolegij: ")

    return Kolegij(ime, ects)

from ispit import ispit


def ispis_studenta(student):
    print(f"\tStudent {student.ime} {student.prezime} je prijavio:")
    student.ispit.ispis()


def ispis_svih_studenata(studenti):
    print('Popis svih studenata: ')
    for student in studenti:
        student.ispis()

from .student import Student
from .izracun_skolarine import IzracunSkolarine


class VanredniStudent(Student, IzracunSkolarine):
    def __init__(self, ime, prezime, ispit):
        super().__init__(ime, prezime, ispit)

    def ispis(self):
        print(f"Redovni student {self.ime} {self.prezime} je prijavio ispit:")
        self.ispit.ispi()
        print(f"\t Potrebno je platiti {self.izracun_skolarine()} eura")

    def izracun_skolarine(self):
        return self.ispit.kolegij.ects * 50

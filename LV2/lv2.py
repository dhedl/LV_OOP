from datetime import date

kolegij = {}

kolegij['Ime kolegija'] = input('Unesite ime kolegija: ').upper()
kolegij['Broj ECTS'] = int(input('Unesite ECTS bodove za kolegij: '))

# print('Kolegij', kolegij['Ime kolegija'], 'nosi', kolegij['Broj ECTS'], 'ECTS bodova')

ispit = {}

ispit = kolegij.copy()
dan = int(input('Unesite dan ispita: '))
mjesec = int(input('Unesite mjesec ispita: '))
godina = int(input('Unesite godinu ispita: '))
ispit['Datum ispita'] = date(godina, mjesec, dan)
# print('Kolegij', ispit['Ime kolegija'], 'nosi', ispit['Broj ECTS'], 'ECTS bodova')
# print('Datum ispita je:', ispit['Datum ispita'])

student = {}

student = ispit.copy()
ime = input('Unesite ime studenta: ').capitalize()
prezime = input('Unesite prezime studenta: ').capitalize()
student['Podaci'] = ime + ' ' + prezime
print('Student', student['Podaci'], 'je prijavio ispit iz kolegija',
       student['Ime kolegija'], 'koji će se održati:', student['Datum ispita'])

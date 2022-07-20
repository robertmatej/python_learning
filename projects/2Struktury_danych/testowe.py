"""
Poprawona wersja FOR z poprzedniego kursu

"""
lista = [-1, 2, -2, 6, 3, -4, 5, 5, -8, -8, 9]

#wersja licznik
dodatnie = 0
ujemne = 0

for licznik in lista:
    if licznik > 0:
        dodatnie +=1

    if licznik < 0:
        ujemne += 1

print (f'Liczb dodatnich jest: {dodatnie}, a ujemnyhc {ujemne}')

#wersja na listach
dodatnie2 = []
ujemne2 = []
for licznik2 in lista:
    if licznik2 > 0:
        dodatnie2.append(licznik2)

    if licznik2 < 0:
        ujemne2.append(licznik2)

print (f'Liczb dodatnich jest: {len(dodatnie2)}, a ujemnyhc {len(ujemne2)}')
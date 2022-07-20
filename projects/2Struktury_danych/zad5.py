"""
Wypisać na konsoli tabliczkę mnożenia w formacie tabeli 9x9

"""
a = range(0,10)
b = range(0,10)
wynik = []
poziom = []
for pion in a:

    for poziom in b:
        print(f'{pion*poziom}',sep=',,,,',end='')

    print ()
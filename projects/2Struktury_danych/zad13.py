'''
Każą w konsoli stworzyć struktury korzystając ze skróconej wersjii zapisu
-lista zawierająca liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
-zbiór tupli zawierajjących 3 elementy - daną licznę, - jej kwadrat i jej sześcian w przedziale -10 10
- słownik mapujący napisy w ich długoś powstały ze zbioru napisów
'''

"1: "
lista = print([0.1*j for j in range(0,10,1)])


'2: '
zbior = print([(i,i**2,i**3) for i in range(-10,10,1)])

zbior2 = []
for i in range(-10,10,1):
    zbior2.append((i,i**2,i**3))     #przekazuję tuplę argumentów jako JEDEN arg (funkcja moze przyjąc tylko 1 arg)

print(zbior2)

slownik = print({x: len(x) for x in {'jakies', 'jaja', 'z', 'tymi', 'zbiorami'}})
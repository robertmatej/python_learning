"""
program zliczający wystąpienie każdego znaku w napisie wprowadzonym przez usera
"""
napis = input ('wprowadź napis, policzę ilość wystąpień każdego znaku: ')
slownik = {}

for litera in napis:
    slownik[litera]=slownik.get(litera,0)+1
    #print(slownik)

print (f'słownik znaków: {slownik} suma snaków: {len(napis)}')
"""
user podaje ciąg zawierający <> a pmięzy jakiś napis, policzyć znaki pomiędzy <>
<> moga wystąpić tlyko raz
pzydało by się zrobć zabezlpieczenia na jednorazowe uzycie nawiasów
"""
napis = input('Drogi userze podaj ciąg znaków z <dowolny tekst>, polczę znaki pomiedzy <>: ')
licz = 0
zamknij  = 0
czy_miedzy_nawiasami = False
for iter in napis:

    if iter == '<':
        czy_miedzy_nawiasami = True
    elif iter == '>':
        czy_miedzy_nawiasami = False
        zamknij +=1
    elif czy_miedzy_nawiasami:
        licz += 1
if zamknij == 0:
    print('nie zamknąłes nawiasu >')

print (f'ilość znaków pomiędzy <> wynosi: {licz}')


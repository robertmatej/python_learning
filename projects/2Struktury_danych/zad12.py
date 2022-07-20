"""
Posortować liczby w tablicy przy wykorzystaniu algorytmu
"sorotwanie przez wybieranie"
gdy są 2 identyczne liczby to się gubi - wypisuje ja na koniec, rozwiązanie to przekonwertować do zbioru i spowrotem na liste
"""

#tab = set([23, 2,5, 3, 5, 66, 12, 52, -3, 1, 9, -20, -3, 0])
#tab = list(tab1)
tab = [23, 2,5, 3, 5, 66, 12, 52, -3, 1, 9, -20, 0]
print (f'tablica przed sortowaniem: {tab}')
for i in tab:
    i_pozycja = tab.index(i)       ## jak się zachowa gdy 2 takie same liczby będą ?
    tab_min = tab[i_pozycja:]       #pomniejszona tabl do szukania min
    print(f'1: Tab min: {tab_min}')
    index_wart_min = tab.index(min(tab_min)) # indeks z tabliczy "tab" najmniejszej wartości znalezionej w tablicy min
#    print(index_wart_min)
    wart_min = min(tab_min)         #wartość minimalna w pomniejszonej tabeli
    tab[index_wart_min] = i
    tab[i_pozycja] = wart_min

#    print(tab)
print(f'tablica po sortowaniu: {tab}')
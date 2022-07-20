"""
funkcja zwracająca zbiór wszsytkich znaków występujących w napisie więcej niż zadana ilość.
Nieudana !!!!!!!!!!!!!
"""

def wiecej_niż(napis, ilosc_znak):
    licznik = dict()

    for znak in napis:

        licznik[znak] = licznik.get(znak,0)+1
        print (licznik)
        item = licznik.values()

    for i in item:
        if i > ilosc_znak:
            print(i)
    return licznik, item

out, item = wiecej_niż("jakis napis kurna",2)
print(out, item)
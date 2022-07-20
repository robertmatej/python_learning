"""
funkcja licząca silnię dla zadanej wartości, rekurencja

"""

def silnia(wart):

    if wart == 0:
        return 1
    else:
        return wart * silnia(wart-1)  # return pozwala pominąć konwersję typów i związanych z tym błędów
#        print(wart * silnia(wart-1)) # w tej konfiguracji wyrzuca niezgodność typów zmienych przy mnożeniu.

print(silnia(5))

'''
 FUNKCJA
 podajemy 2 liczby program ma dokonać jakiejś operacji matemeycznej (+, -, dzielenie, mnożenie)
 podjamey tez operację, w wyniku zlej operacji wyrzyca błąd

'''

def wykonaj_dzialanie(dane):
    a = dane[0]
    b = dane[1]
    operacja = dane[2]
    wynik = None
    if operacja == '+' or operacja == 'dodawanie':
        wynik = a + b
    elif operacja == '-' or operacja == 'odejmowanie':
        wynik = a - b
    elif operacja == '*' or operacja == 'mnoezenie':
        wynik = a * b
    elif operacja == '/' or operacja == 'dzielenie':
        while b == 0:
            b = float(input('nie mozna dzielic przez 0, podaj liczbe rozna od zera: '))
        wynik = a / b
    else:
        print('podales niepoprawny parametr dzialania')

    return wynik

def pobierz_dane():
    liczba1 = float(input('podaj pierwszą liczbę do obliczeń: '))
    liczba2 = float(input('podaj drugą liczbę do obliczeń: '))
    dzialanie = input('podaj dzialanie które wykonam: ')

    return liczba1, liczba2, dzialanie

def wyswietl_wynik():
    dane = pobierz_dane()
    wynik = wykonaj_dzialanie(dane)
    print (wynik)

wyswietl_wynik()
def wiecej_niz (napis, prog):
    wynik = set()
    for litera in napis.lower():
       if napis.count(litera) >prog:
           wynik.add(litera)
    return wynik

# out = wiecej_niz("jakis tekst o byle czym a moze o",2)
# print (out)

def test_wiecejniz_pusty_napis():
    assert  wiecej_niz('dsddsd',2) == {'d'}

test_wiecejniz_pusty_napis()       # wywołanie testu do sprawdzenia prog.


print(wiecej_niz('dsddsd',2)) # wydruk do wizualizacji pracy
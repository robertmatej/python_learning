"""
Zaimplemnetować funkcję formatującą tekst
podmieania "$cena" na zmienną cena o konkretnej wartośći
funkcja ma przyjmować dowolną liczbę argumentów
"""

def formatuj (*args, **kwargs):
#    args = ('koszt $cena PLN ', 'kwota $cena brutto')
#    kwargs  = {"$cena": "10"}
#    a = str(kwarg
#    print(args)
#    print (kwargs)
#    d = str(args).replace('$cena', "#10")


    for klucz in kwargs:
        #print (klucz)
        out = str(args).replace(klucz, str(kwargs[klucz]))
        print (out)

formatuj ('koszt $cena PLN ', 'kwota cena1 brutto', cena = 10, cena1 =20)
# w pierwszej petli for podstawia pod "cena" wartość 10, w drugiem przebiegu pod "cena1" wstawia 20
"""
('koszt $10 PLN ', 'kwota 101 brutto')
('koszt $cena PLN ', 'kwota 20 brutto'
"""
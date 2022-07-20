"""
Zaimplementować klasę Basket umożliwającą dodawanie produktów w określoniej ilości do koszyka
zaimpl. metode obliczającą całkowitą wartość koszyka, wypisującą info o zawartości koszyka
dodanie 2x tego amego produktu powinno stwożyć tylko jedną pozycję.
"""
class Produkt:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def drukuj_info(self):
        return f'aktualyny produkt: "{self.nazwa}", id: {self.id}, cena: {self.cena} PLN'
class WlozenieKoszyk:

    def __init__(self,produkt,ilosc):
        self.produkt = produkt
        self.ilosc = ilosc
        print(f'produkt: {self.produkt}')

    def licz_cene(self):
        return self.produkt.cena * self.ilosc

    def drukuj_raport(self):
        return f'- {self.produkt.nazwa}({self.produkt.id}), cena: {self.produkt.cena} x {self.ilosc}\n '

class Koszyk:

    def __init__(self):
        self.wpisy = []

    def __str__(self):
        return "Koszyk"

    def dodaj_produkt(self, produkt, ilosc):
        wlozenie_kosz = WlozenieKoszyk(produkt, ilosc)
        self.wpisy.append(wlozenie_kosz)
        print(f'wpisy: {self.wpisy}')


    def policz_wartosc_koszyka(self):
        sumuj = 0
        for e in self.wpisy:
            sumuj += e.licz_cene()
        return sumuj

    def generuj_raport(self):
        cena_koszyk = self.policz_wartosc_koszyka()
        temp=""
        for wpis in self.wpisy:
            temp += wpis.drukuj_raport()
        output = f"""
        Produkty w koszyku:  
        {temp}
        w sumie: {cena_koszyk}"""

        return output

produkt = Produkt(1, "woda", 2.1)
koszyk = Koszyk()
koszyk.dodaj_produkt(produkt,2)
koszyk.dodaj_produkt(produkt,3)
raport = koszyk.generuj_raport()
print (raport)

def test_product():
    produkt = Produkt(2, "flaszka", 23.4)

    assert hasattr(produkt, "id")
    assert hasattr(produkt, "cena")
    assert hasattr(produkt, "nazwa")

    assert produkt.cena == 23.4
    assert produkt.id == 2
    assert produkt.nazwa == "flaszka"

def test_produkt_drukuj_info():
    produkt = Produkt(3, "napój", 6.7)

    assert produkt.drukuj_info() == f'aktualyny produkt: "napój", id: 3, cena: 6.7 PLN'

def test_stworz_koszyk():
    koszyk = Koszyk()
    assert str(koszyk) == "Koszyk"
    assert koszyk.wpisy == []

def test_dodaj_produkt():
    koszyk= Koszyk()
    produkt1 = Produkt(1, "napój", 6.7)
    produkt2 = Produkt(2, "faszka", 30.2)
    koszyk.dodaj_produkt(produkt1,2)
    koszyk.dodaj_produkt(produkt2,1)
    assert len(koszyk.wpisy) == 2

def test_policz_wartosc_koszyka():
    koszyk= Koszyk()
    produkt1 = Produkt(1, "napój", 6)
    produkt2 = Produkt(2, "faszka", 30)
    koszyk.dodaj_produkt(produkt1,2)
    koszyk.dodaj_produkt(produkt2,1)
    assert koszyk.policz_wartosc_koszyka() == 41

def test_policz_wartosc_wlozenia():
    wlozenie = WlozenieKoszyk(Produkt(2, "faszka", 30),6)
    assert wlozenie.licz_cene() == 180

def test_koszyk_generuj_raport():
    koszyk = Koszyk()
    produkt = Produkt(2, "flaszka", 30)
    produkt1 = Produkt(1, "napój", 10)
    koszyk.dodaj_produkt(produkt,2)
    koszyk.dodaj_produkt(produkt1,4)
    assert koszyk.generuj_raport() == """
    Produkty w koszyku:
    - flaszka(2), cena: 30 x 2
- napój(1), cena: 10 x 4

        w sumie: 100"""

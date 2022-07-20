"""
Zaimplementowaćklasę Employee umożliwiającąrejestrowanie czasu pracy oraz wypłacanie pensji
na podstawie  zadanej stawki godzinowej. Jeżeli pracownik będize pracował powyżej 8h (podczas jednej rejestracji czasu)
to kolejne godziny policz jako nadgodziny za podwójną stawkę h

"""

class Pracownik:
    def __init__(self,imie,nazwisko,stawka_godz):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka_godz = stawka_godz

    def rejestruj_czas_pracy(self,czas_pracy):
#        print (czas_pracy)
        return czas_pracy, self.imie, self.nazwisko

    def wypłac_pensje(self,czas_pracy):
        stawka_godz  = self.stawka_godz

        if czas_pracy<= 8:
            wyplata = czas_pracy*stawka_godz
        elif czas_pracy > 8:
            wyplata = 8 * stawka_godz + (czas_pracy-8)*2*stawka_godz
        return float(wyplata)


pracownik = Pracownik('Robert',"Matejek", 22)
przepracowal, im, nazw = pracownik.rejestruj_czas_pracy(8)
wyplata = pracownik.wypłac_pensje(przepracowal)
print(f'wyplata dla: {im} {nazw} za dziś: {wyplata}')

def test_pracownik():
    robol = Pracownik('Jan', 'Kowalski',13)
    assert robol.imie == "Jan"
    assert robol.nazwisko == 'Kowalski'
    assert robol.stawka_godz == 13

def test_wyplata():
    robol = Pracownik('Jak', 'Kaczka', 9)
    pensja,a,b = robol.rejestruj_czas_pracy(5)
    assert robol.rejestruj_czas_pracy(5) == (5,"Jak","Kaczka")
    assert robol.wypłac_pensje(pensja) == 45
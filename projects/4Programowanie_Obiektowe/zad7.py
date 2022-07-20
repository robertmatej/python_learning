"""
Premium Employee
będzie pochodną kalasy Emplpyee, powinna umożliwiać przyznawanie bonusów pracownikowi.

Employee:
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


class PracownikPremiowany(Pracownik):
    def __init__(self,imie,nazwisko,stawka_godz,premia):
        super().__init__(self,imie,nazwisko,stawka_godz)
        self.premia = premia

    @property
    def czy_wyplac_premie(self):
        czas_pracy  = Pracownik.rejestruj_czas_pracy       ## jak przekazać zmienną czas pracy, żeby nie pobierac jje bezposrednio i nie przerabiać całego kodu???
        if czas_pracy > 8:
            premia = (czas_pracy-8)* self.stawka_godz*3
            return self.premia
        else:
            return f"brak premii, przepracowałeś tylko {czas_pracy} robaku "

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

def test_czy_wypl_premia():
    wzorowy_robol = PracownikPremiowany("ronaldo", "pedał", 2, 500)
    pensja ,a,b = wzorowy_robol.rejestruj_czas_pracy(9)
    premia = wzorowy_robol.czy_wyplac_premie()
    assert premia == 8

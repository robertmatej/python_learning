"""
Klasa CashMachine umożliwia wpłacanie i wypłacanie pieniędzy
stan bankomatu ma być przechowywany w zmiennych prywatnych

"""
class Bankomat:

    def __init__(self):
        self.__srodki = 10000

    def __str__(self):
        return "Bankomat"

    def wyplata(self,kwota):

        if kwota < self.__srodki:
            self.__srodki = self.__srodki - kwota
            return f"wyplacono {kwota}"
        elif kwota > self.__srodki:
            return "wypłata nie możliwa, za mało środków w urządzeniu"

    def wplata(self, kwota):
        self.__srodki = self.__srodki + kwota
        return f"wplacono {kwota}"

    def kwota_w_bankomat(self,haslo):
        if haslo == 123:
           return f" INFO SERWIS w bankomacie pozostało {self.__srodki}"
        else:
            return "próba kradzieży wzywam 112"

# euronet = Bankomat()
# out = euronet.wplata(100)
# out2 = euronet.wyplata(9999999)
# out2 = euronet.wyplata(10020)
# #out1 = euronet.__srodki
# print (out)
# #print (out2)
# stan_bank = euronet.kwota_w_bankomat(123)
# print(stan_bank)

def test_stworz_bankomat():
    euronet = Bankomat
#    assert str(euronet) == "Bankomat"
#    assert euronet.__srodki == 10000

def test_sprawdz_wplata():
    euronet = Bankomat()
    out = euronet.wplata(100)
    assert out == "wplacono 100"

def test_sprawdz_wyplata():
    euronet = Bankomat()
    out = euronet.wyplata(1650)
    assert out == "wyplacono 1650"
    out2 = euronet.wyplata(999999)
    assert out2 == "wypłata nie możliwa, za mało środków w urządzeniu"

def test_sprawdz_stan_bankomatu():
    euronet = Bankomat()
    assert euronet.kwota_w_bankomat(123) == f" INFO SERWIS w bankomacie pozostało 10000"
    assert euronet.kwota_w_bankomat(2443) ==  "próba kradzieży wzywam 112"
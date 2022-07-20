"""
Zaimplementować kalsę Product przechowującą inforamcję o cenie, nazwie oraz ID produktu
zaimplementuj metodę wypisującę info o produkcie na konsolę
"""

class Product:

    y = "morskie"
    def __init__(self, tablica,tt):
        self.hujwico = tablica
#        x = (1, "wódka", 23)
#        y = "morskie"

    def wydruk(self):
        print(self.y)
        print (f'Prorodukt {self.hujwico[1]}, id: {self.hujwico[0]}, cena: {self.hujwico[2]}PLN')

produkt = Product((1, "wódka", 23), "wow")
#print (produkt.x)
#print(produkt.hujwico)

produkt.wydruk()
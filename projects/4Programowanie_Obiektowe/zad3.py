'''
klada odwzorująca zachowanie autea ekeltrycznego
przejechnie zadanej odległości nie większej niż max zasięg i opcja ładowania

'''

class ElectricCar:

    def __init__(self,zasieg_max):
        pass
        self.zasieg_max = zasieg_max
        self.zasieg_akt = 100

    def laduj (self):
        self.zasieg_akt = self.zasieg_max
#        return zasieg_act

    def jedz (self,trasa):
        if self.zasieg_akt < trasa:
            print (f"nie starczy energii na całą trasę, mamy {self.zasieg_max}km zasięgu, podłącz ładowanie. ")
        elif self.zasieg_akt > trasa:
            zasieg_po = self.zasieg_akt - trasa
            print(f"jedziemy do celu, po wycieczce zostanie {zasieg_po}km zasięgu :) ")
            self.zasieg_akt = zasieg_po

    def sprawdz_zasieg(self):
        print(f'aktualny zasięg: {self.zasieg_akt}')

tesla = ElectricCar(200)
tesla.laduj()
tesla.sprawdz_zasieg()
tesla.jedz(20)
tesla.sprawdz_zasieg()
tesla.jedz(100)
tesla.sprawdz_zasieg()
tesla.jedz(100)
tesla.sprawdz_zasieg()
tesla.laduj()
tesla.sprawdz_zasieg()
#print(wycieczka)
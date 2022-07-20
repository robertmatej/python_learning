class ElectricCar:
    def __init__(self, range, distance_remaining):
        self.range = range
#        self.charge_level = chcarge_level
        self.distance_remaining = distance_remaining

    def drive(self, distance):
        #dist_to_drive = self.distance_remininig - distance
        if distance > self.distance_remaining:
            print(f"Distance too far, you can drive max {self.distance_remaining}km. Bettter charge batteries ;)")
        if distance > self.range:
            print(f"Max range is {self.range}km, actual charge last for{self.distance_remaining}km ")
        if distance <= self.distance_remaining:
            self.distance_remaining-= distance
            print(f"You drived {distance}km, remain {self.distance_remaining}km.")

    def charge(self):
        self.distance_remaining = 300
        print ("Charging complete! You can drive 300 km.")

evo = ElectricCar(300,300)
evo.drive(30)
evo.drive(180)
evo.charge()
evo.drive(300)

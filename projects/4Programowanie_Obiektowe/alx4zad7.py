"""
PremiumEmployee pochodna po Employee
klasa powinna umożliwiać przyznawanie bonusów pracownikowi
employee.give_bonus(1000.0)
Wyświetlanie wypłaty w funkcji bazowej jak i dziedziczącej, rozwiązaniem może być dodanie jakiejś bunkcj drukującej?
Albo testy assert zamiast wydruków.

"""

class Employee:

    def __init__(self, name, surname, hour_rate, work_time):
        self.name = name
        self.surname = surname
        self.hour_rate = hour_rate
        self.work_time = work_time

    def register_time(self, time):
        self.work_time = time

    def pay_salary(self):
        if self.work_time <= 8:
            pay = self.work_time * self.hour_rate

        elif self.work_time > 8:
            overhours = self.work_time - 8
            pay = overhours * 2 * self.hour_rate + (self.work_time - overhours) * self.hour_rate

        print(f"{self.name} {self.surname} salary is: {pay}")
        self.work_time = 0
        return pay

class PremiumEmployee(Employee):

    def __init__(self, name, surname, hour_rate, work_hour, bonus):
        super().__init__(name, surname, hour_rate, work_hour)
        self.bonus = bonus

    def give_bonus(self, bonus):
        self.bonus = bonus

    def pay_salary(self):
        pay_salary_with_bonus = super().pay_salary() + self.bonus
        print(f"{self.name} {self.surname} salary with bonus is: {pay_salary_with_bonus}")
        self.bonus = 0
        return pay_salary_with_bonus



antek = Employee("Antek", "Noga", 100, 0)
antek.register_time(10)
antek.pay_salary()
antek.pay_salary()
antek.register_time(5)
antek.pay_salary()
antek.pay_salary()

adam = PremiumEmployee("Adam", "Domino", 100, 0, 0)
#print (adam.hour_rate)

adam.register_time(10)
adam.give_bonus(500)
adam.pay_salary()
adam.pay_salary()
adam.register_time(5)
adam.give_bonus(1050)
adam.pay_salary()
adam.pay_salary()

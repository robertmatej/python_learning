class Employee:

#    name = ""
#    surname = ""
#    hour_rate = None
#    work_time = None


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

adam = Employee("Adam", "Domino", 100, 0)
print (adam.hour_rate)

adam.register_time(10)
adam.pay_salary()
adam.pay_salary()
adam.register_time(5)
adam.pay_salary()
adam.pay_salary()
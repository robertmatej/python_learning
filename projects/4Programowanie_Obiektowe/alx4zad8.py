"""
W kalsie CashMachine rzucanie wyjątków w sytuacjach:
- brak miejsca na banknoty - ustalić limit banknotów w bankomacie
- zła wartość wypłacanej sumy (musi być podzielna przez 10)
- brak odpowiednich banknotów w bankomacie
prosty interfejs tekstowy do klasay bankomat, wyświetlanie wyjątków również przez podanie złych danyh przez usera

"""

class CashMachine:

    def __init__(self):
        self._money_avaliable = [100, 200, 10, 20, 50]
        self.avaliable = True
        self.max_input_size = 10

    def avaliable_amount(self):
        amount = 0
        for key in self._money_avaliable:
            amount += key
        print(f"Avaliable amount: {amount}")
        return amount

    def is_avaliable(self):
        amount = self.avaliable_amount()
        if (amount > 0 and self.avaliable == True):
            print("Cash Mashine avaliable")
            return True
        else:
            print("ATM not avaliable")
            return False

    def put_money(self, put_mon):
        for money in put_mon:
            try:
                if (len(self._money_avaliable) >= self.max_input_size):
                    raise ValueError
            except ValueError:
                print("No more space in ATM to add greenbacks")
                break
            else:
                print(f"Putting greenbacks")
                self._money_avaliable.append(money)

    def withdraw_money(self, amount):
        self.amount = amount
        sum_w = []
        try:
            if amount %10 != 0:
                raise ValueError
        except ValueError:
            print(f"Wrong sum to withdraw ({amount}), minimal greenback in ATM is 10")
        else:
            for bill in sorted(self._money_avaliable, reverse = True):
                if sum(sum_w) + bill <= amount:
                    sum_w.append(bill)

            if sum(sum_w) == amount:
                for bill in sum_w:
                    self._money_avaliable.remove(bill)
                print(f"Withdrawing amount: {sum_w}")
            else:
                print("Not enough money in ATM")


def main():
    euronet = CashMachine()
    while True:
        user = input("What do you want to do? with, put, aval\n")
        try:
            if user == "with":
                euronet.withdraw_money(int(input("Type amount: ")))
            elif user == "put":
                euronet.put_money([100, 200, 500])
            elif user == "aval":
                euronet.avaliable_amount()
            else:
                raise ValueError
        except ValueError:
            print("Wrong input")


    euronet.avaliable_amount()
    euronet.is_avaliable()
    euronet.put_money([100,200,500,100,50,20,10,10,20])
    euronet.avaliable_amount()
    euronet.withdraw_money(125)
    #euronet.avaliable_amount()
    euronet.withdraw_money(1980)
    #euronet.avaliable_amount()
    euronet.withdraw_money(200)
    euronet.avaliable_amount()

main()
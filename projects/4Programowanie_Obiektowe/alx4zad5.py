
class CashMachine:

    def __init__(self):
        self._money_avaliable = [100, 200]
        self.avaliable = True

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
            print("Cash Mashine not avaliable")
            return False

    def put_money(self,put_mon):
        self.put_mon = put_mon

        for money in put_mon:
            self._money_avaliable.append(money)

    def withdraw_money(self, amount):
        self.amount = amount
        sum_w = []

        for bill in sorted(self._money_avaliable, reverse = True):
            if sum(sum_w) + bill <= amount:
                sum_w.append(bill)

        if sum(sum_w) == amount:
            for bill in sum_w:
                self._money_avaliable.remove(bill)
            print(f"withdrawed money: {sum_w}")
        else:
            print("Not enough bills in ATM")


euronet = CashMachine()

euronet.avaliable_amount()
euronet.is_avaliable()
euronet.put_money([100,200,500,100,50,20,10,10,20])
euronet.avaliable_amount()
euronet.withdraw_money(120)
#euronet.avaliable_amount()
euronet.withdraw_money(1980)
#euronet.avaliable_amount()
euronet.withdraw_money(200)
euronet.avaliable_amount()

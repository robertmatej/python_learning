"""
Zaimplementować metodę statyczną tworżacą koszyk na podstawie listy podanych produktów,
każdy z nich powineine zostac dodany do koszyka tylko raz

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ UNDONE $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""

class Product:

    id = 1
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def ids(cls):
        cls.id += 1
        print(cls.id)


class Basket:

    def __init__(self, basket_worth):
        self.basket_worth = basket_worth


    def get_products(self, name):
        return [self.name, self.price]

    @staticmethod
    def with_products(list):
        bask = {"apotato": 1}
        for key in list:
            if key not in bask:
                bask[key] = 1
            elif key in bask:
                bask[key] += 1
        return Basket.count_value_of_basket(bask)

    def count_value_of_basket(dict_):
        sum_ = 0
        for key in dict_:
            sum_ += dict_[key] * Product.price

        return sum_

    def print_basket(self):
        pass

    def add_discount(self, discount):
        return discount * Basket.count_value_of_basket()


class ValueDiscount:

    def __init__(self,discount):
        self.discount = discount

    def get_dicsount(self):
        return self.discount


class PercentageDiscount:

    def __init__(self, discount):
        self.discount = discount

    def get_discount(self):
        return 0.01 * self.discount




potato = Product("potato", 3.5)
Product.ids()
carrot = Product("carrot", 4.2)
carrot.ids()
carrot.ids()
tomato = Product("tomato", 9)
apple = Product("apple", 4)

basket1 = Basket.with_products([potato, apple, tomato])
print(basket1)

#print(basket1)

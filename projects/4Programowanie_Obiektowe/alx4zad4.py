class Product:

    def __init__(self, name, price, prod_id):
        self.name = name
        self.price = price
        self.prod_id = prod_id

class BasketEntry:
    def __init__(self, product, quantity):
        self.quantity = quantity
        self.product = product

    def count_price(self):
        price = self.product.price * self.quantity
        return price

    def generate_report(self):
        return f"- {self.product.name} ({self.product.prod_id}), price: {self.product.price} x {self.quantity}\n"

class Basket:

    def __init__(self):
        self.entries = []

    def add_product(self, price, quantity):
        basket_entry = BasketEntry(price, quantity)
        self.entries.append(basket_entry)

    def count_total_price(self):
        total = 0
        for entry in self.entries:
            total += entry.count_price()
        return total

    def generate_report(self):
        total_price = self.count_total_price()
        report = ""
        for entry in self.entries:
            report += entry.generate_report()

        output = f"Products in basket:\n" \
               f"{report}" \
               f"Total price: {total_price}"

        print(output)
        return output

basket = Basket()
product1 = Product("carrot", 4, 1)
product2 = Product("apple", 3, 2)
product3 = Product("banana", 2, 3)
basket.add_product(product1, 2)
basket.add_product(product2, 1)
basket.add_product(product2, 1)
basket.add_product(product3, 3)
basket.generate_report()
'''
basket.add_product("carrot", 2)
basket.add_product("carrot", 3)
basket.add_product("banana", 5)
basket.add_product("apple", 2)
'''
#basket.count_total_price()
#print(f"basket in: {basket.product_list.items()}")

def test_product():
    product = Product("carrot", 4.2, 2)
    assert hasattr(product, "name")
    assert hasattr(product, "price")
    assert hasattr(product, "prod_id")

    assert product.name == "carrot"
    assert product.price == 4.2
    assert product.prod_id == 2




def test_basket():
    basket = Basket()
    product1 = Product("carrot", 4.2, 1)
    product2 = Product("banana", 3.1, 2)
    basket.add_product(product1, 2)
    basket.add_product(product2, 1)

#    basket.add_product("carrot", 1)
#    basket.add_product("banana", 1)
#    basket.add_product("apple", 1)
    assert basket.count_total_price() == 11,5

def test_final_report():
    basket = Basket()
    product1 = Product("carrot", 4.2, 1)
    product2 = Product("banana", 3.1, 2)
    basket.add_product(product1, 2)
    basket.add_product(product2, 1)
    assert basket.generate_report() == 'Products in basket:\n' \
                                       '- carrot (1), price: 4.2 x 2\n' \
                                       '- banana (2), price: 3.1 x 1\n' \
                                       'Total price: 11.5'
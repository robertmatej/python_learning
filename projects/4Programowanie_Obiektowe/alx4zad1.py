class Product:
    price = None
    name = ""
    id = None


    def print_info(self):
        print(f"Product: {self.name}, ID: {self.id}, price: {self.price}")
        print("test")

pr = Product()
pr.name = "marchew"
pr.id = 1
pr.price = 2.2

pr.print_info()

class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("price can not be negative")
        self.__price = price

    price1 = property(get_price, set_price)


prd = Product(100)
print(prd.price1)
print(prd.get_price())

print(prd.price1)
prd.price1 = 200
print(prd.price1)

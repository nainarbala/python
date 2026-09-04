class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Value can not be negative")
        self.__price = price


prd = Product(11)
print(prd.price)
prd.price = -10

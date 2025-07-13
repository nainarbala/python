class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Not valid")
        self.__price = price


try:
    prd = Product(-10)
except ValueError as e:
    print(e)
# print(prd.price)
# prd.price = 20
# print(prd.price)
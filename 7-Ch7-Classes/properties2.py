class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price can not be negative")
        self.__price = price


try:
    prd = Product(-50)
except ValueError as err:
    print(err)

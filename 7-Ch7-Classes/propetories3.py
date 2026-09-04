class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            raise ValueError("price can not be negative")
        self._price = price


prd = Product(100)
print(prd.get_price())

prd = Product(-10)
print(prd.get_price())

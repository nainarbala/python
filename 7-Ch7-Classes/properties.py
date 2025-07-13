class Product:
    def __init__(self, price):
        self.set_price(price)
    
    def get_product(self):
        return self.__price
    
    def set_price(self, price):
        if(price < 0):
            raise ValueError("not a valid")
        self.__price = price

    

prd = Product(50)
print(prd.get_product())

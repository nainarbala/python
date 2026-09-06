class Animal:
    def __init__(self):
        print("Calling Animal construcotr")
        self.age = 1

    def walk(self):
        print("Wak")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Calling Mamal constructor")


m = Mammal()

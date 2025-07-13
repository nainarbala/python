class Animal:
    def __init__(self):
        self.age = 10
    
    def eat(self):
        print("Eat...")

class Mammal(Animal):
    def __init__(self):
        self.weight = 50
        super().__init__()

    def fly(self):
        print("Fly...")

class Fish(Animal):
    def swim(self):
        print("Swim...")

m = Mammal()
print(m.age)
print(m.weight)
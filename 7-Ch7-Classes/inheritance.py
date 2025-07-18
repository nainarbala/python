class Animal:
    def __init__(self, value):
        self.x = value
    
    def eat(self):
        print("Eat...")

class Mammal(Animal):
    def fly(self):
        print("Fly...")

class Fish(Animal):
    def swim(self):
        print("Swim...")


m = Mammal(10)
print(m.x)
print(m.eat())
print(m.fly())
# print(m.swim())
class Animal:
    def __init__(self, value):
        self.x = value
    
    def eat(self):
        print("Eat...")

class Mammal(Animal):
    def fly(self):
        print("Fly...")

class Fish(Mammal):
    def swim(self):
        print("fissss...")


m = Fish(10)
print(m.x)
print(m.eat())
print(m.fly())
print(m.swim())
# print(m.swim())
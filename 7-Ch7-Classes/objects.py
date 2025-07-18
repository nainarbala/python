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
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))
print(isinstance(m, Fish))

print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
print(issubclass(Animal, Mammal))
print(issubclass(Mammal, Mammal))


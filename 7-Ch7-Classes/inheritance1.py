class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def walk(self):
        print("Walk")


class Fish(Animal):
    def swim(self):
        print("Swim")


m = Mammal()
print(m.age)
print(m.eat())
print(m.walk())
print(m.__dict__)
print(isinstance(m, object))

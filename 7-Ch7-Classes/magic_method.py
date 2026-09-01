class Point:
    defecul_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"

    def __eq__(self, value):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        return cls(1, 's')

    def draw(self):
        print(f"Point({self.x}, {self.y})")


point = Point.zero()
print(point)
print(point.draw())

other = Point.zero()

print(point == other)
print(point > other)
print(point < other)
print(point + other)

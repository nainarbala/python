class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"drwaing:{self.x}, {self.y}")

point1 = Point(12,13)
point2 = Point(1,1)
adding = point1 + point2
print(adding.x)

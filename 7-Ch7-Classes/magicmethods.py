class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __gt__(self, value):
        return self.x > value.x and self.y > value.y

    def draw(self):
        print(f"drwaing:{self.x}, {self.y}")

point1 = Point(12,13)
point2 = Point(1,1)
print(point1 == point2)
print(point1 > point2)
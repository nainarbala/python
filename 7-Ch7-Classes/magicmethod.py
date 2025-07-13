class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x}, y:{self.y}"

    def draw(self):
        print(f"drwaing:{self.x}, {self.y}")

point = Point(2,3)
print(str(point))
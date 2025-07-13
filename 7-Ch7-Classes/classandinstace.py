class Point:
    default_color = "Red"
    def __init__(self, x, y):
        self.a = x
        self.b = y
    
    def draw(self):
        print(f"Point x:{self.a}, y:{self.b}")

    

point = Point(1,2)
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
point.draw()

point.z = 10

point1 = Point(2,3)
print(type(point1))
print(isinstance(point1, Point))
print(isinstance(point1, int))
point1.draw()

print(point1.default_color)

print(Point.default_color)
class Point:
    default_color = "Yellow"
    # 'self' refers to the instance object itself, allowing access to instance variables
    # and methods. Each object has its own copy of x, y attributes via self.

    def __init__(self, x, y):
        self.x = x  # self stores x value unique to this Point instance
        self.y = y  # self stores y value unique to this Point instance

    def draw(self):
        # pass

        # self accesses the instance's x and y values
        print(f"Point({self.x}, {self.y})")


point = Point(11, 22)
point.draw()

point.default_color = "red"
point.z = 20

point1 = Point(20, 30)

point1.z = 30

print(point.z)
print(point1.z)
print(point.default_color)
print(point1.default_color)
print(Point.default_color)

print(Point.draw(point1))

print(Point.draw(point))

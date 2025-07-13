class Point:
    def __init__(self, x, y):
        self.a = x
        self.b = y
    
    def draw(self):
        print(f"Point x:{self.a}, y:{self.b}")


point = Point(1,2)
point.draw()
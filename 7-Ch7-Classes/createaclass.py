class Point:
    def draw(self):
        print("draw")
    

point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
point.draw()
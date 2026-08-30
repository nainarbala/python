class Point:
    def draw(self):
        print("drwa")


point = Point()
print(point.draw())
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, str))
# <class '__main__.Point'>

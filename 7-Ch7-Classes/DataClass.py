from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

point1 = Point(x=1, y=3)
point2 = Point(x=1, y=3)
point3 = Point(x=1, y=2)

print(point1 == point2)
print(point1 == point3)

lists = [point3, point1, point2]
print(lists)

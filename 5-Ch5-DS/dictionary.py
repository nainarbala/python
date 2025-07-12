point = {"x": 1, "y":2}
print(type(point))
print(point)

point = dict(m=10, n=81)
print(type(point))
print(point)

print(point["m"])
print(point.get("0", "Nothig"))

for key in point:
    print(key)
    print(point[key])


print("*" * 20)

for x,y in point.items():
    print(x, y)

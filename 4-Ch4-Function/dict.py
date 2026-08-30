point = {"x": 1, "y": 3, "z": 10}

print(point)
point1 = dict(w=10, r=4)
print(point1)
print(point["x"])
print(point.get("dfsdf", 0))

if "x" in point:
    print("yes")

for key in point:
    print(key)
    print(point[key])

for key, value in point.items():
    print(key, ":", value)

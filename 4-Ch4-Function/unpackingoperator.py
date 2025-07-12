list1 = [1,3,5,6,6]
print(list1)
print(*list1)

values = list(range(5))
print(values)

values = [*range(5), *"Tesing123"]
print(values)

first = dict(x=1, y=2)
second = dict(x=10, z=4)
combined = {**first, **second, "m":200}

print(combined)
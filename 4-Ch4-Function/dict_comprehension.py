values = []

for x in range(5):
    values.append(x * 2)
print(values)


values1 = [x*2 for x in values]

print(values1)

print({x * 2 for x in range(10)})


dic1 = {x: x*2 for x in range(10)}
print(dic1)

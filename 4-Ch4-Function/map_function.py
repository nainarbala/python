items = [
    ("Prouct9", 10),
    ("Product1", 8),
    ("Product8", 100)
]

prices = []
for item in items:
    prices.append(item[1])

print(type(prices))
print(prices)

prices = map(lambda item: item[1], items)
print(type(prices))
print(prices)
print(tuple(prices))
print(list(prices))

items = [
    ("Prouct9", 10),
    ("Product1", 8),
    ("Product8", 100)
]

items.sort(key=lambda item: item[1])
print(items)

items.sort(key=lambda item: item[0])
print(items)


print(sorted(items, key=lambda item: item[1], reverse=True))

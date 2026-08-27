items = [
    ("Prouct9", 10),
    ("Product1", 8),
    ("Product8", 100)
]

filters = []

for item in items:
    if item[1] >= 10:
        filters.append(item[1])

print(filters)


def filter_item(item):
    if item[1] >= 10:
        return item[1]


print(list(filter(lambda item: item[1] >= 10, items)))
print(list(map(lambda item: item[1], (filter(filter_item, items)))))

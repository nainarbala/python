numbers = [10, 3, 5, 7, 13, 657, 1, 6, 0, 856]
print(numbers.sort(reverse=True))
print(numbers)
print(sorted(numbers))


items = [
    ("product10", 10),
    ("product12", 1),
    ("product19", 23)
]

print(items)
print(type(items))
print(type(items[0]))

items.sort()
print(items)


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


def sort_item1(item1):
    return item1[0]


items.sort(key=sort_item1)
print(items)

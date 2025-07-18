numbers = [2,1,4,14,6,26]

print(numbers.sort(reverse=True))
print(numbers)

print(sorted(numbers, reverse=True))

product = [
    ("Prd1", 89),
    ("Prd2", 10),
    ("Prd3",30),
    ("Prd4", 1),
]

print(product)


def sort_prd(product1):
    return product1[1]

sort_prd(product)

print(product.sort(key=sort_prd))
print(product)

product.sort(key=lambda item: item[1])
print(product)
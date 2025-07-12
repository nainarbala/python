product = [
    ("Prd1", 89),
    ("Prd2", 10),
    ("Prd3",30),
    ("Prd4", 1),
]

#prices = list(map(lambda item: item[1], product))
prices = [item[1] for item in product]
print(prices)

product = [item for item in product if item[1]  >= 10]
print(product)
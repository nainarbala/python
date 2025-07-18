product = [
    ("Prd1", 89),
    ("Prd2", 10),
    ("Prd3",30),
    ("Prd4", 1),
]


product.sort(key= lambda item: item[1])
print(product)
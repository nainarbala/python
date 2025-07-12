product = [
    ("Prd1", 89),
    ("Prd2", 10),
    ("Prd3",30),
    ("Prd4", 1),
]


print(list(filter(lambda prd: prd[1] >= 10, product)))
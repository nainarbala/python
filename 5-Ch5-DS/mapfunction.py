product = [
    ("Prd1", 89),
    ("Prd2", 10),
    ("Prd3",30),
    ("Prd4", 1),
]

# prices = []
# for prd in product:
#     prices.append(prd[1])

# print(prices)

def get_proce(prd):
    return prd[1]

x = map(get_proce, product)
print(list(x))

x = map(lambda prd: prd[1], product)
print(list(x))

print(list(map(lambda prd: prd[1], product)))
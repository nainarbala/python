items = [
    ("Prouct9", 10),
    ("Product1", 8),
    ("Product8", 100)
]

prices = list(map(lambda item: item[1], items))
print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

prices = [item[1] for item in items]
print(f"x:{prices}")

filtered = [item[1]
            for item in items
            if item[1] >= 10 and item[0].startswith("Pro")
            ]

print(f"filterd {filtered}")

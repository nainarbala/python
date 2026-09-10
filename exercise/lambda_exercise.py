def restaurant(restaurants):
    return list(filter(lambda restaurant: restaurant["rating"] >= 4.2, restaurants))


print(restaurant([
    {"name": "Burger Joint", "rating": 4.1, "delivery_fee": 5.00},
    {"name": "Sushi Master", "rating": 4.7, "delivery_fee": 0.00},
    {"name": "Pizza Palace", "rating": 3.9, "delivery_fee": 2.50},
    {"name": "Taco Corner", "rating": 4.5, "delivery_fee": 3.00}
]))

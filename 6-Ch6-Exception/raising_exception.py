def age_calculator(age):
    if age <= 0:
        raise ValueError("Age cant be zero or lessthan")
    return age / 10


try:
    print(age_calculator(0))
except ValueError as err:
    print(err)

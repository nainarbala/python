def calc(x):
    if x <= 0:
        raise ValueError("Value cant be zero or less")
    return x * 2
try:
    calc(0)
except ValueError as e:
    print(e)
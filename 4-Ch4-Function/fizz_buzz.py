def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "FIZZ BUZZ"
    elif num % 3 == 0:
        return "FIZZ"
    elif num % 5 == 0:
        return "BUZZ"
    else:
        return num


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))

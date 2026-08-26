def multiply(*numbers):
    print(type(numbers))
    print(numbers)
    for number in numbers:
        print(number)
    print("==================")
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

numbers = [1, 2, 1, 4, 5]
print(numbers)
numbers = set(numbers)
print(set(numbers))

second = {1, 3}

print(second)

print(numbers | second)
print(numbers & second)
print(numbers - second)
print(numbers ^ second)

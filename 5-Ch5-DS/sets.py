numbers1 = set([1,2,3,5])
print(type(numbers1))

first = {1,1,2,3,4}
second = {1,5}

print(first | second, second | first)
print(first & second, second & first)
print(first - second, second - first)
print(first ^ second, second ^ first)


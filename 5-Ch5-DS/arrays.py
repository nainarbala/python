from array import array

number = array("i", [1,2,3])

print(number.append(10))
print(number)
print(number.insert(0,89))
print(number.pop())
if 1 in number:
    number.remove(1)

print(number)

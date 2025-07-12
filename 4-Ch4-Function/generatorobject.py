from sys import getsizeof

tuple1 = (item for item in range(999999))
print(getsizeof(tuple1))

list1 = [item for item in range(999999)]
print(getsizeof(list1))
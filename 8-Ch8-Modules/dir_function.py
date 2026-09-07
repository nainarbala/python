from ecommerce.shopping import sales1

print()
print()
# print(sales1.__dict__)
# print(sales1.init)
# print(sales1.__cached__)
# print(sales1.__doc__)
# print(sales1.__file__)
# print(sales1.__name__)
# print(sales1.__package__)


# print("dir:", dir(sales1))
# print(sales1.__builtins__)


print("Cached:", sales1.__cached__)
print("doc:", sales1.__doc__)
print("file:", sales1.__file__)
print("loader:", sales1.__loader__)
print("name:", sales1.__name__)
print("package:", sales1.__package__)
print("spec:", sales1.__spec__)
print("init:", sales1.init)
print("sales1:", sales1.sales1)

print(__name__)

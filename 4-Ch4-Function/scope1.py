message = "a"


def greet(name):
    global message
    message = name


print(greet("one"))
print(message)

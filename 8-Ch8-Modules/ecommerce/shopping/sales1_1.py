def sales1():
    return "this is sales1"

def init():
    return "init method"

print(__name__)

if __name__ == "__main__":
    print(init())
else:
    print(sales1())



try:
    with open("finally.py") as file:
        print(file)
    age = 10
    print(age)
except (ValueError, ZeroDivisionError, BaseException) as ex:
    print(ex)
else:
    print("exception not occured")

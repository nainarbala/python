file = ""
try:
    file = open("exception.py")
    age = int(input("enter age: "))
    print("age is", age)
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as er:
    print("Wrong input")
    print(er)
    print(er.args)
    print(type(er))
else:
    print("Not enter except")
finally:
    file.close()
print("Execution continue")

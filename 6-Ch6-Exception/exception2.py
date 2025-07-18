try:
    age = int(input("enter a age:"))
    print("age is", age)
    print("xfactios is ", age/0)
except (ValueError, ZeroDivisionError) as ex:
    print("not enter valid age")
    print(ex)
    print(type(ex))
else:
    print("Not enter excpetion")
print("End program")
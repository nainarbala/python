
file = None
try:
    file = open("/workspaces/python/6-Ch6-Exception/exception2.py")
    print("file open sccuess")
except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print("File Not found")
finally:
    if file:
        print(file)
        file.close()
        print("file close success")
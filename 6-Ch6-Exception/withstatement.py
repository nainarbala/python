try:
    with open("/workspaces/python/6-Ch6-Exception/exception2.py") as file:
        print("File opnened")
    print("111")
except ValueError as error:
    print("Exceoption occured")
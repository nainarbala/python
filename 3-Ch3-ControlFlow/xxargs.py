def save_user(**user):
    print(type(user))
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=1, name="sdfsdf", age=50)

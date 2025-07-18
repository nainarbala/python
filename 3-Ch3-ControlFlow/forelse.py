success = False
for number in range(3):
    print("Attempt", number + 1, "*" * (number + 1))
    if success:
        print("Success")
        break
else:
    print("Failed")
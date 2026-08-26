success = True

for number in range(3):
    print("Attempt")
    if success:
        print("send successfully")
        break
else:
    print("Ateempt not reached")

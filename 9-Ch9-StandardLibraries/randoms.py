import random
import string

print(random.random())
print(random.randint(1,10))
print(random.choice([2,3,45,67,8,0]))
print(random.choices([2,3,5,6,71], k=3))
print("".join(random.choices(string.ascii_letters + string.hexdigits, k=10)))

numnbers = [9,3,4,6,6,1]
random.shuffle(numnbers)
print(numnbers)


lists = ["a1", "b", "c", "d"]

for letter in lists:
    print(letter)


for letter in enumerate(lists):
    print(letter)

for index, letter in enumerate(lists):
    print(f"{index}, {letter}") 
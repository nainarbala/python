letters = ["a", "b", "c", "d"]

# Add

letters.append("e")
letters.insert(0, "_")
print(letters)
print(letters.index("c"))

# remove
del letters[0]
letters.pop()
letters.remove("d")
print(letters)

if "sfsd" in letters:
    print(letters.remove("sfsd"))
    print(letters.index("sfsd"))

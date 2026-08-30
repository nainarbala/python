from pprint import pprint

sentence = "This is a common interview question"

sentence = [*sentence]
# print(sentence)
char_count = {}

for char in sentence:
    if char_count.get(char) == None:
        char_count[char] = 1
    else:
        char_count[char] = char_count.get(char) + 1


print(char_count)


char_count = {}
for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


print(char_count)
pprint(char_count)

print(sorted(char_count.items(), key=lambda kv: kv[1], reverse=True))

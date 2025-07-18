str = "find the Most repeated character"

char_count = {}
for char in str:
    # print(char)
    if char not in ' ':
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1

most_repeated_chars = sorted(char_count.items(), key= lambda kv: kv[1], reverse=True)
print(most_repeated_chars[0])




class TagCloud:
    __defaulr_color = "red"

    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, key):
        return self.__tags.get(key.lower())

    def __setitem__(self, key, value):
        self.__tags[key.lower()] = value

    def __len__(self):
        return len(self.__tags)


cloud = TagCloud()
print(cloud.__dict__)
cloud.add("1")
cloud.add("1")
cloud.add("2")

print(cloud._TagCloud__tags)
print(len(cloud))
cloud["tt"] = 5

print(cloud._TagCloud__tags)
print(cloud._TagCloud__defaulr_color)

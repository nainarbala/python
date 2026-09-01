class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, key):
        return self.tags.get(key.lower())

    def __setitem__(self, key, value):
        self.tags[key.lower()] = value

    def __len__(self):
        return len(self.tags)


cloud = TagCloud()
cloud.add("1")
cloud.add("1")
cloud.add("2")

print(cloud.tags)
print(len(cloud))
cloud["tt"] = 5

print(cloud.tags)

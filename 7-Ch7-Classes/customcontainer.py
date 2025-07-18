class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags[tag.lower()]
    
    def __setitem__(self, tag, count):
        self.tags[tag] = count

    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        iter(self.tags)


    

tag = TagCloud()
tag.add("aa")
tag.add("xxxx")
tag.add("xxxx")
tag.add("xxxx111")

print(tag.tags)

print(tag["aa"]) # this calls get method
tag["aa1"] = 10 # this calls set method
print(tag.tags)

print(len(tag))

print(tag)




class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags[tag.lower()]
    
    def __setitem__(self, tag, count):
        self.__tags[tag] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        iter(self.__tags)


    

tag = TagCloud()
# print(tag.__tags)
print(tag.__dict__)
print(tag._TagCloud__tags)

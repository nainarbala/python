class Text(str):
    def duplicates(self):
        return self + self
    
txt = Text("One")
print(txt.lower())
print(txt.duplicates())


class TrackableList(list):
    def append(self, object):
        print("append called")
        return super().append(object)


lst = TrackableList()
print(lst.append("1111"))
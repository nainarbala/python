class Text(str):
    def duplicate(self):
        return self + self


class ListClass(list):
    def append(self, object):
        print("append calle")
        return super().append(object)


txt = Text("Python")
print(txt.duplicate())


list1 = ListClass()
print(list1.append("sss"))

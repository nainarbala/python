
class TextBox:
    def draw(self):
        print("TextBox...")

class DropDownList:
    def draw(self):
        print("DropDownList")



def draw(contols):
    for control in contols:
        control.draw()


tb = TextBox()
dw = DropDownList()

draw([tb, dw])
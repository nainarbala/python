from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox...")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")



def draw(contols):
    for control in contols:
        control.draw()


tb = TextBox()
dw = DropDownList()

draw([tb, dw])
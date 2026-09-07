from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class Textbox(UIControl):
    def draw(self):
        print("TextBox")


class DropDown(UIControl):
    def draw(self):
        print("DropDown")


text = Textbox()
text.draw()

ddl = DropDown()
ddl.draw()


def draw(controls):
    for control in controls:
        control.draw()


draw([ddl, text, text])

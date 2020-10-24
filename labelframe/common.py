from tkinter import LabelFrame
from item import Item6, Item7, Item8


class CommonFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Общие данные')
        self.paragraph_6 = Item6(self)
        self.paragraph_7 = Item7(self)
        self.paragraph_8 = Item8(self)

    def init(self):
        pass

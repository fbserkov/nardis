from tkinter import LabelFrame
from item import Item0, Item1, Item2, Item4, Item5, Item16


class PassportFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Паспортная часть')
        self.paragraph_0 = Item0(self)
        self.paragraph_4 = Item4(self)
        self.paragraph_16 = Item16(self)
        self.paragraph_1 = Item1(self)
        self.paragraph_2 = Item2(self)
        self.paragraph_5 = Item5(self, database)

    def init(self):
        pass

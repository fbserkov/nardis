from tkinter import LabelFrame
from item import Item13, Item14, Item15, Item17


class ExaminationFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold',
            text='Данные освидетельствования',
        )
        self.paragraph_13 = Item13(self, database)
        self.paragraph_14 = Item14(self, database)
        self.paragraph_15 = Item15(self)
        self.paragraph_17 = Item17(self)

    def init(self):
        pass

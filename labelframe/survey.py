from tkinter import LabelFrame
from item import Item9, Item10, Item11, Item12


class SurveyFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Объективный осмотр')
        self.paragraph_9 = Item9(self)
        self.paragraph_10 = Item10(self)
        self.paragraph_11 = Item11(self)
        self.paragraph_12 = Item12(self)

    def init(self):
        pass

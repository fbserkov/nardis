from tkinter import LabelFrame
from item import (
    Item0, Item1, Item2, Item4, Item5, Item6, Item7, Item8, Item9,
    Item10, Item11, Item12, Item13, Item14, Item15, Item16, Item17,
)


class CommonFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Общие данные')
        self.paragraph_6 = Item6(self)
        self.paragraph_7 = Item7(self)
        self.paragraph_8 = Item8(self)

    def init(self):
        pass


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

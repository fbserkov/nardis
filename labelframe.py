from tkinter import LabelFrame
from item import create_item


class CommonFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Общие данные')
        self.item_6 = create_item(self, 6)
        self.item_7 = create_item(self, 7)
        self.item_8 = create_item(self, 8)

    def init(self):
        pass


class ExaminationFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold',
            text='Данные освидетельствования',
        )
        self.item_13 = create_item(self, 13, database)
        self.item_14 = create_item(self, 14, database)
        self.item_15 = create_item(self, 15)
        self.item_17 = create_item(self, 17)

    def init(self):
        pass


class PassportFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Паспортная часть')
        self.item_0 = create_item(self, 0)
        self.item_4 = create_item(self, 4)
        self.item_16 = create_item(self, 16)
        self.item_1 = create_item(self, 1)
        self.item_2 = create_item(self, 2)
        self.item_5 = create_item(self, 5, database)

    def init(self):
        pass


class SurveyFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Объективный осмотр')
        self.item_9 = create_item(self, 9)
        self.item_10 = create_item(self, 10)
        self.item_11 = create_item(self, 11)
        self.item_12 = create_item(self, 12)

    def init(self):
        pass

from tkinter import LabelFrame
from item import create_item


class CommonFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Общие данные')
        self.items = (
            create_item(self, 6), create_item(self, 7), create_item(self, 8))

    def init(self):
        for item in self.items:
            item.init()


class ExaminationFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold',
            text='Данные освидетельствования',
        )
        self.items = (
            create_item(self, 13, database), create_item(self, 14, database),
            create_item(self, 15), create_item(self, 17),
        )

    def init(self):
        for item in self.items:
            item.init()


class PassportFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Паспортная часть')
        self.items = (
            create_item(self, 0), create_item(self, 4), create_item(self, 16),
            create_item(self, 1), create_item(self, 2),
            create_item(self, 5, database),
        )

    def init(self):
        for item in self.items:
            item.init()


class SurveyFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Объективный осмотр')
        self.items = (
            create_item(self, 9), create_item(self, 10),
            create_item(self, 11), create_item(self, 12),
        )

    def init(self):
        for item in self.items:
            item.init()

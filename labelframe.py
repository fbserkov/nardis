from tkinter import LabelFrame
from item import create_item


class PartBase(LabelFrame):
    def __init__(self, label):
        self.items = ()
        LabelFrame.__init__(self, font='-size 10 -weight bold', text=label)

    def init(self):
        for item in self.items:
            item.init()


class CommonPart(PartBase):
    def __init__(self):
        PartBase.__init__(self, 'Общие данные')
        self.items = (
            create_item(self, 6), create_item(self, 7), create_item(self, 8))


class ExaminationPart(PartBase):
    def __init__(self, data):
        PartBase.__init__(self, 'Данные освидетельствования')
        self.items = (
            create_item(self, 13, data), create_item(self, 14, data),
            create_item(self, 15), create_item(self, 17),
        )


class PassportPart(PartBase):
    def __init__(self, data):
        PartBase.__init__(self, 'Паспортная часть')
        self.items = (
            create_item(self, 0), create_item(self, 4), create_item(self, 16),
            create_item(self, 1), create_item(self, 2),
            create_item(self, 5, data),
        )

    def update_user(self):
        self.items[-1].update_user()


class SurveyPart(PartBase):
    def __init__(self):
        PartBase.__init__(self, 'Объективный осмотр')
        self.items = (
            create_item(self, 9), create_item(self, 10),
            create_item(self, 11), create_item(self, 12),
        )

from tkinter import LabelFrame
from item import create_item


class PartBase(LabelFrame):
    def __init__(self, master, label):
        self.items = {}
        LabelFrame.__init__(
            self, master, font='-size 10 -weight bold', text=label)

    def check(self):
        for i, item in self.items.items():
            item.check(i)

    def init(self):
        for item in self.items.values():
            item.init()


class CommonPart(PartBase):
    def __init__(self, master):
        PartBase.__init__(self, master, 'Общие данные')
        self.items = {i: create_item(self, i) for i in (6, 7, 8)}


class ExaminationPart(PartBase):
    def __init__(self, master):
        PartBase.__init__(self, master, 'Данные освидетельствования')
        self.items = {i: create_item(self, i) for i in (13, 14, 15, 17)}


class PassportPart(PartBase):
    def __init__(self, master):
        PartBase.__init__(self, master, 'Паспортная часть')
        self.items = {i: create_item(self, i) for i in (0, 1, 2, 3, 4, 5, 16)}

    def update(self):
        self.items[0].update_act_number()
        self.items[5].update_user()


class SurveyPart(PartBase):
    def __init__(self, master):
        PartBase.__init__(self, master, 'Объективный осмотр')
        self.items = {i: create_item(self, i) for i in (9, 10, 11, 12)}

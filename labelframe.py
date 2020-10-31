from tkinter import LabelFrame
from item import create_item


class PartBase(LabelFrame):
    def __init__(self, master, label):
        self.items = {}
        LabelFrame.__init__(
            self, master, font='-size 10 -weight bold', text=label)

    def init(self):
        for item in self.items.values():
            item.init()


class CommonPart(PartBase):
    def __init__(self, master):
        PartBase.__init__(self, master, 'Общие данные')
        self.items = {i: create_item(self, i) for i in (6, 7, 8)}


class ExaminationPart(PartBase):
    def __init__(self, master, data):
        PartBase.__init__(self, master, 'Данные освидетельствования')
        self.items = {i: create_item(self, i, data) for i in (13, 14)}
        self.items.update({i: create_item(self, i) for i in (15, 17)})


class PassportPart(PartBase):
    def __init__(self, master, data):
        PartBase.__init__(self, master, 'Паспортная часть')
        self.items = {i: create_item(self, i, data) for i in (0, 3, 5)}
        self.items.update({i: create_item(self, i) for i in (1, 2, 4, 16)})

    def update(self):
        self.items[0].update_index()
        self.items[5].update_user()


class SurveyPart(PartBase):
    def __init__(self, master):
        PartBase.__init__(self, master, 'Объективный осмотр')
        self.items = {i: create_item(self, i) for i in (9, 10, 11, 12)}

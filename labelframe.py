from tkinter import LabelFrame
from item import create_item


class PartBase(LabelFrame):
    def __init__(self, label):
        self.items = {}
        LabelFrame.__init__(self, font='-size 10 -weight bold', text=label)

    def init(self):
        for item in self.items.values():
            item.init()


class CommonPart(PartBase):
    def __init__(self):
        PartBase.__init__(self, 'Общие данные')
        self.items = {i: create_item(self, i) for i in (6, 7, 8)}


class ExaminationPart(PartBase):
    def __init__(self, data):
        PartBase.__init__(self, 'Данные освидетельствования')
        self.items = {i: create_item(self, i, data) for i in (13, 14)}
        self.items.update({i: create_item(self, i) for i in (15, 17)})


class PassportPart(PartBase):
    def __init__(self, data):
        PartBase.__init__(self, 'Паспортная часть')
        self.items = {i: create_item(self, i, data) for i in (0, 5)}
        self.items.update({i: create_item(self, i) for i in (1, 2, 4, 16)})

    def update(self):
        self.items[0].update_index()
        self.items[5].update_user()


class SurveyPart(PartBase):
    def __init__(self):
        PartBase.__init__(self, 'Объективный осмотр')
        self.items = {i: create_item(self, i) for i in (9, 10, 11, 12)}

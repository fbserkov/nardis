import time
from tkinter import Frame, Label, LEFT, RIGHT, X

from widget.entry import (
    EntryBase, EntryDate, EntryDisabled, EntryTime, EntryYear)
from widget.label import LabelAdd, LabelReplace
from widget.option_menu import OptionMenuSmart


class ItemBase:
    frame = None

    def __init__(self, master, frames_number=None):
        frame = Frame(master, bd=4)
        frame.pack(fill=X)
        if frames_number:
            self.frames = self.get_frames(frame, frames_number)
        else:
            if not ItemBase.frame:
                ItemBase.frame = Frame(master, bd=4)
                ItemBase.frame.pack(fill=X)
                ItemBase.frame.columnconfigure(1, weight=1)
                ItemBase.frame.columnconfigure(3, weight=1)
            self.frame = Frame(ItemBase.frame)

    @staticmethod
    def get_frames(master, length):
        frames = []
        for i in range(length):
            frame = Frame(master)
            frame.pack(fill=X)
            frames.append(frame)
        return frames


class Item0(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=0)
        Label(self.frame, text='Акт №').grid(row=0, column=0, columnspan=2)
        EntryDisabled(self.frame, width=4).grid(row=1, column=0)
        Label(self.frame, text='/').grid(row=1, column=1)
        EntryYear(
            self.frame, default=time.strftime('%y')).grid(row=1, column=2)


class Item1(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=7)
        Label(
            self.frames[0],
            text='1. Сведения об освидетельствуемом лице',
        ).pack(side=LEFT)
        Label(self.frames[0], text='Дата рождения').pack(side=RIGHT)
        Label(self.frames[1], text='Фамилия, имя, отчество').pack(side=LEFT)
        EntryBase(self.frames[1]).pack(side=LEFT, expand=True, fill=X)
        EntryDate(self.frames[1])

        Label(self.frames[2], text='Адрес места жительства').pack(side=LEFT)
        entry = EntryBase(self.frames[4])
        entry.pack(fill=X)
        LabelAdd(self.frames[3], text='г. Комсомольск-на-Амуре', bind=entry)
        LabelAdd(self.frames[3], text='Комсомольский район', bind=entry)
        LabelAdd(self.frames[3], text='Хабаровский край', bind=entry)

        line = 'Сведения об освидетельствуемом лице заполнены на основании'
        Label(self.frames[5], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[6])
        entry.pack(side=LEFT, expand=True, fill=X)
        LabelReplace(self.frames[5], text='протокола', bind=entry)
        line = 'водительского удостоверения'
        LabelReplace(self.frames[6], text=line, bind=entry, place=LEFT)
        LabelReplace(self.frames[6], text='паспорта', bind=entry, place=LEFT)


class Item2(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=5)
        line = '2. Основание для медицинского освидетельствования'
        Label(self.frames[0], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[3])
        entry.pack(fill=X)
        line = 'протокол о направлении на медицинское освидетельствование'
        LabelReplace(self.frames[1], text=line, bind=entry)
        LabelReplace(self.frames[2], text='личное заявление', bind=entry)
        line = 'письменное направление работодателя'
        LabelReplace(self.frames[2], text=line, bind=entry)
        Label(self.frames[4], text='Кем направлен (ФИО)').pack(side=LEFT)
        EntryBase(self.frames[4]).pack(side=LEFT, expand=True, fill=X)


class Item3(ItemBase):
    pass


class Item4(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=2)
        Label(self.frame, text='4. Начало освидетельствования').pack()
        Label(self.frame, text='Дата').pack(side=LEFT)
        EntryDate(self.frame, time.strftime('%d.%m.%Y'))
        Label(self.frame, text='Время').pack(side=LEFT)
        EntryTime(self.frame, time.strftime('%H:%M'))


class Item5(ItemBase):
    def __init__(self, master, database):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='5. Кем освидетельствован').pack(side=LEFT)
        doctors = database.get_doctors()
        OptionMenuSmart(
            self.frames[1], doctors, doctors[0] if len(doctors) == 1 else None)


class Item6(ItemBase):
    pass


class Item7(ItemBase):
    pass


class Item8(ItemBase):
    pass


class Item9(ItemBase):
    pass


class Item10(ItemBase):
    pass


class Item11(ItemBase):
    pass


class Item12(ItemBase):
    pass


class Item13(ItemBase):
    pass


class Item14(ItemBase):
    pass


class Item15(ItemBase):
    pass


class Item16(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=4)
        Label(self.frame, text='16. Окончание освидетельствования').pack()
        Label(self.frame, text='Дата').pack(side=LEFT)
        EntryDate(self.frame, time.strftime('%d.%m.%Y'))
        Label(self.frame, text='Время').pack(side=LEFT)
        EntryTime(self.frame, time.strftime('%H:%M'))

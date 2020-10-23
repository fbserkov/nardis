import time
from tkinter import Frame, Label, LabelFrame, LEFT, RIGHT, X

from labelframe import get_frames
from widget.entry import (
    EntryBase, EntryDate, EntryDisabled, EntryTime, EntryYear)
from widget.label import LabelAdd, LabelReplace
from widget.option_menu import OptionMenuSmart


class PassportFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Паспортная часть')
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(3, weight=1)
        self.paragraph_0(frame)
        self.paragraph_4(frame)
        self.paragraph_16(frame)
        self.paragraph_1()
        self.paragraph_2()
        self.paragraph_5(database)

    @staticmethod
    def paragraph_0(frame):
        frame = Frame(frame)
        frame.grid(row=0, column=0)
        Label(frame, text='Акт №').grid(row=0, column=0, columnspan=2)
        EntryDisabled(frame, width=4).grid(row=1, column=0)
        Label(frame, text='/').grid(row=1, column=1)
        EntryYear(frame, default=time.strftime('%y')).grid(row=1, column=2)

    def paragraph_1(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 7)

        Label(frames[0], text='1. Сведения об освидетельствуемом лице').pack(
            side=LEFT)
        Label(frames[0], text='Дата рождения').pack(side=RIGHT)
        Label(frames[1], text='Фамилия, имя, отчество').pack(side=LEFT)
        EntryBase(frames[1]).pack(side=LEFT, expand=True, fill=X)
        EntryDate(frames[1])

        Label(frames[2], text='Адрес места жительства').pack(side=LEFT)
        entry = EntryBase(frames[4])
        entry.pack(fill=X)
        LabelAdd(frames[3], text='г. Комсомольск-на-Амуре', bind=entry)
        LabelAdd(frames[3], text='Комсомольский район', bind=entry)
        LabelAdd(frames[3], text='Хабаровский край', bind=entry)

        line = 'Сведения об освидетельствуемом лице заполнены на основании'
        Label(frames[5], text=line).pack(side=LEFT)
        entry = EntryBase(frames[6])
        entry.pack(side=LEFT, expand=True, fill=X)
        LabelReplace(frames[5], text='протокола', bind=entry)
        line = 'водительского удостоверения'
        LabelReplace(frames[6], text=line, bind=entry, place=LEFT)
        LabelReplace(frames[6], text='паспорта', bind=entry, place=LEFT)

    def paragraph_2(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 5)
        line = '2. Основание для медицинского освидетельствования'
        Label(frames[0], text=line).pack(side=LEFT)
        entry = EntryBase(frames[3])
        entry.pack(fill=X)
        line = 'протокол о направлении на медицинское освидетельствование'
        LabelReplace(frames[1], text=line, bind=entry)
        LabelReplace(frames[2], text='личное заявление', bind=entry)
        line = 'письменное направление работодателя'
        LabelReplace(frames[2], text=line, bind=entry)
        Label(frames[4], text='Кем направлен (ФИО)').pack(side=LEFT)
        EntryBase(frames[4]).pack(side=LEFT, expand=True, fill=X)

    @staticmethod
    def paragraph_4(frame):
        frame = Frame(frame)
        frame.grid(row=0, column=2)
        Label(frame, text='4. Начало освидетельствования').pack()
        Label(frame, text='Дата').pack(side=LEFT)
        EntryDate(frame, time.strftime('%d.%m.%Y'))
        Label(frame, text='Время').pack(side=LEFT)
        EntryTime(frame, time.strftime('%H:%M'))

    def paragraph_5(self, database):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 2)
        Label(frames[0], text='5. Кем освидетельствован').pack(side=LEFT)
        doctors = database.get_doctors()
        OptionMenuSmart(
            frames[1], doctors, doctors[0] if len(doctors) == 1 else None)

    @staticmethod
    def paragraph_16(frame):
        frame = Frame(frame)
        frame.grid(row=0, column=4)
        Label(frame, text='16. Окончание освидетельствования').pack()
        Label(frame, text='Дата').pack(side=LEFT)
        EntryDate(frame, time.strftime('%d.%m.%Y'))
        Label(frame, text='Время').pack(side=LEFT)
        EntryTime(frame, time.strftime('%H:%M'))

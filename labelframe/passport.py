import time
from tkinter import (
    Entry, Frame, Label, LabelFrame, LEFT, OptionMenu, RIGHT, StringVar, X)

from labelframe import get_frames
from widget.entry import EntryDate, EntryTime
from widget.label import LabelBase


class PassportFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(self, text='Паспортная часть')

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
        Entry(
            frame, width=4, font='-size 10', fg='#800000',
            state='disabled', disabledforeground='#800000'
        ).grid(row=1, column=0)
        Label(frame, text=time.strftime('/%y')).grid(row=1, column=1)

    def paragraph_1(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 7)

        Label(frames[0], text='1. Сведения об освидетельствуемом лице').pack(
            side=LEFT)
        Label(frames[0], text='Дата рождения').pack(side=RIGHT)
        Label(frames[1], text='Фамилия, имя, отчество').pack(side=LEFT)
        Entry(frames[1], font='-size 10', fg='#800000').pack(
            side=LEFT, expand=True, fill=X)
        EntryDate(frames[1])

        Label(frames[2], text='Адрес места жительства').pack(side=LEFT)
        entry = Entry(frames[4], font='-size 10', fg='#800000')
        entry.pack(fill=X)
        LabelBase(
            frames[3], text='г. Комсомольск-на-Амуре', bind=('add', entry))
        LabelBase(frames[3], text='Комсомольский район', bind=('add', entry))
        LabelBase(frames[3], text='Хабаровский край', bind=('add', entry))

        line = 'Сведения об освидетельствуемом лице заполнены на основании'
        Label(frames[5], text=line).pack(side=LEFT)
        entry = Entry(frames[6], font='-size 10', fg='#800000')
        entry.pack(side=LEFT, expand=True, fill=X)
        LabelBase(frames[5], text='протокола', bind=('replace', entry))
        line = 'водительского удостоверения'
        LabelBase(frames[6], text=line, bind=('replace', entry), place=LEFT)
        LabelBase(
            frames[6], text='паспорта', bind=('replace', entry), place=LEFT)

    def paragraph_2(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 5)

        line = '2. Основание для медицинского освидетельствования'
        Label(frames[0], text=line).pack(side=LEFT)
        entry = Entry(frames[3], font='-size 10', fg='#800000')
        entry.pack(fill=X)
        line = 'протокол о направлении на медицинское освидетельствование'
        LabelBase(frames[1], text=line, bind=('replace', entry))
        LabelBase(frames[2], text='личное заявление', bind=('replace', entry))
        line = 'письменное направление работодателя'
        LabelBase(frames[2], text=line, bind=('replace', entry))
        Label(frames[4], text='Кем направлен (ФИО)').pack(side=LEFT)
        Entry(frames[4], font='-size 10', fg='#800000').pack(
            side=LEFT, expand=True, fill=X)

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
        string_var_10 = StringVar(frames[1])
        if len(doctors) == 1:
            string_var_10.set(doctors[0])
        option_menu_10 = OptionMenu(frames[1], string_var_10, *doctors)
        option_menu_10.config(font='-size 10', fg='#800000')
        option_menu_10.pack(fill=X)

    @staticmethod
    def paragraph_16(frame):
        frame = Frame(frame)
        frame.grid(row=0, column=4)

        Label(frame, text='16. Окончание освидетельствования').pack()
        Label(frame, text='Дата').pack(side=LEFT)
        EntryDate(frame, time.strftime('%d.%m.%Y'))
        Label(frame, text='Время').pack(side=LEFT)
        EntryTime(frame, time.strftime('%H:%M'))

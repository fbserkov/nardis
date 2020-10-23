import time
from tkinter import (
    Checkbutton, E, Frame, IntVar, Label, LabelFrame, LEFT, RIGHT, W, X)

from labelframe import get_frames
from widget.entry import (
    EntryBase, EntryDate, EntryDisabled, EntryResult, EntryTime, EntryYear)
from widget.label import LabelReplaceSmart, LabelReplaceSmartDate
from widget.option_menu import OptionMenuSmart

minus, plus = '«-»', '«+»'


class ExaminationFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold',
            text='Данные освидетельствования',
        )
        self.paragraph_13(database)
        self.paragraph_14(database)
        self.paragraph_15()
        self.paragraph_17()

    def init(self):
        pass

    def paragraph_13(self, database):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 6)
        for i in 1, 4:
            frames[i].columnconfigure(1, weight=1)
            frames[i].columnconfigure(3, weight=1)

        line = '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого'
        Label(frames[0], text=line).pack(side=LEFT)
        Label(frames[1], text='13.1. Первое исследование').grid(
            row=0, column=0)
        frame = Frame(frames[1])
        frame.grid(row=0, column=2)
        Label(frame, text='Время').pack(side=LEFT)
        EntryTime(frame, time.strftime('%H:%M'))
        frame = Frame(frames[1])
        frame.grid(row=0, column=4)
        Label(frame, text='Результат').pack(side=LEFT)
        EntryResult(frame)
        Label(frame, text='мг/л').pack(side=LEFT)
        Label(frames[2], text='техническое средство').pack(side=LEFT)
        technical_means = database.get_technical_means()
        OptionMenuSmart(frames[2], technical_means)
        Checkbutton(
            frames[3], variable=IntVar(frames[3]), onvalue=1, offvalue=0,
            text='фальсификация выдоха',
        ).pack(side=RIGHT)

        Label(frames[4], text='13.2. Второе исследование').grid(
            row=0, column=0)
        frame = Frame(frames[4])
        frame.grid(row=0, column=2)
        Label(frame, text='Время').pack(side=LEFT)
        EntryTime(frame)
        frame = Frame(frames[4])
        frame.grid(row=0, column=4)
        Label(frame, text='Результат').pack(side=LEFT)
        EntryResult(frame)
        Label(frame, text='мг/л').pack(side=LEFT)
        Label(frames[5], text='техническое средство').pack(side=LEFT)
        OptionMenuSmart(frames[5], technical_means)

    def paragraph_14(self, database):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 5)

        line = '14. Время отбора биологического объекта'
        Label(frames[0], text=line).pack(side=LEFT)
        EntryTime(frames[0])
        default = 'моча'
        entry = EntryDisabled(frames[0], width=5, default=default)
        LabelReplaceSmart(frames[0], text='кровь', bind=(entry, default))
        entry.pack(side=RIGHT)
        Label(frames[0], text='среда').pack(side=RIGHT)
        frame = Frame(frames[1])
        frame.pack(side=RIGHT)
        checkbutton = Checkbutton(
            frame, variable=IntVar(frame), onvalue=1, offvalue=0,
            text='отказ от сдачи пробы биологического объекта (мочи)',
        )
        checkbutton.grid(row=0, sticky=W)
        checkbutton = Checkbutton(
            frame, variable=IntVar(frame), onvalue=1, offvalue=0,
            text='фальсификация пробы биологического объекта (мочи)',
        )
        checkbutton.grid(row=1)
        Label(frames[2], text='метод исследования').pack(side=LEFT)
        OptionMenuSmart(frames[2], database.get_methods())

        line = 'Результаты химико-токсикологических исследований'
        Label(frames[3], text=line).pack(side=LEFT)
        EntryYear(frames[3], default=time.strftime('%y')).pack(side=RIGHT)
        Label(frames[3], text=time.strftime('/')).pack(side=RIGHT)
        EntryBase(frames[3], width=5).pack(side=RIGHT)
        Label(frames[3], text='номер справки').pack(side=RIGHT)
        frames[4].columnconfigure(0, weight=1)
        frames[4].columnconfigure(2, weight=1)
        frames[4].columnconfigure(4, weight=1)
        chemicals = database.get_chemicals()
        for i in range(11):
            row, column = int(i / 2), (i % 2) * 2 + 1
            frame = Frame(frames[4])
            frame.grid(row=row, column=column, sticky=W+E)
            Label(frame, text=chemicals[i]).pack(side=LEFT)
            entry = EntryDisabled(frame, width=4)
            LabelReplaceSmart(frame, text=plus, bind=(entry, ''))
            LabelReplaceSmart(frame, text=minus, bind=(entry, ''))
            entry.pack(side=RIGHT)

    def paragraph_15(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 2)
        Label(frames[0], text='15. Другие данные').pack(side=LEFT)
        entry = EntryBase(frames[1])
        entry.pack(fill=X)
        entry.insert(0, 'нет')

    def paragraph_17(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 3)
        Label(frames[0], text='17. Заключение').pack(side=LEFT)
        entry = EntryDisabled(frames[2])
        entry.pack(side=LEFT, expand=True, fill=X)
        Label(frames[2], text='Дата').pack(side=LEFT)
        date = EntryDate(frames[2])
        for i, text in (
                (0, 'от медицинского освидетельствования отказался'),
                (1, 'состояние опьянения не установлено'),
                (1, 'установлено состояние опьянения'),
        ):
            LabelReplaceSmartDate(frames[i], text, bind=(entry, '', date))

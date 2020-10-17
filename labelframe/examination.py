import time
from tkinter import (
    Checkbutton, E, Entry, Frame, IntVar, Label, LabelFrame, LEFT, OptionMenu,
    RIGHT, StringVar, W, X
)
from widget.widget import (
    DateEntry, get_frames, ResultEntry, SmartLabel, TimeEntry)

minus, plus = '«-»', '«+»'


class ExaminationFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(self, text='Данные освидетельствования')
        self.paragraph_13(database)
        self.paragraph_14(database)
        self.paragraph_15()
        self.paragraph_17()

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
        frame_10 = Frame(frames[1])
        frame_10.grid(row=0, column=2)
        Label(frame_10, text='Время').pack(side=LEFT)
        TimeEntry(frame_10, time.strftime('%H:%M'))
        frame_11 = Frame(frames[1])
        frame_11.grid(row=0, column=4)
        Label(frame_11, text='Результат').pack(side=LEFT)
        ResultEntry(frame_11)
        Label(frame_11, text='мг/л').pack(side=LEFT)

        Label(frames[2], text='техническое средство').pack(side=LEFT)
        technical_means = database.get_technical_means()
        string_var_20 = StringVar(frames[2])
        option_menu_20 = OptionMenu(
            frames[2], string_var_20, *technical_means)
        option_menu_20.config(font='-size 10', fg='#800000')
        option_menu_20.pack(fill=X)

        int_var_30 = IntVar(frames[3])
        checkbutton_30 = Checkbutton(
            frames[3], variable=int_var_30, onvalue=1, offvalue=0,
            text='фальсификация выдоха',
        )
        checkbutton_30.pack(side=RIGHT)

        Label(frames[4], text='13.2. Второе исследование').grid(
            row=0, column=0)
        frame_40 = Frame(frames[4])
        frame_40.grid(row=0, column=2)
        Label(frame_40, text='Время').pack(side=LEFT)
        TimeEntry(frame_40)
        frame_41 = Frame(frames[4])
        frame_41.grid(row=0, column=4)
        Label(frame_41, text='Результат').pack(side=LEFT)
        ResultEntry(frame_41)
        Label(frame_41, text='мг/л').pack(side=LEFT)

        Label(frames[5], text='техническое средство').pack(side=LEFT)
        string_var_50 = StringVar(frames[5])
        option_menu_50 = OptionMenu(
            frames[5], string_var_50, *technical_means)
        option_menu_50.config(font='-size 10', fg='#800000')
        option_menu_50.pack(fill=X)

    def paragraph_14(self, database):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 5)
        frames[4].columnconfigure(0, weight=1)
        frames[4].columnconfigure(2, weight=1)
        frames[4].columnconfigure(4, weight=1)

        line = '14. Время отбора биологического объекта'
        Label(frames[0], text=line).pack(side=LEFT)
        TimeEntry(frames[0])
        SmartLabel(frames[0], text='кровь')
        entry_01 = Entry(frames[0], width=5, font='-size 10', fg='#800000')
        entry_01.pack(side=RIGHT)
        entry_01.insert(0, 'моча')
        entry_01.config(state='disabled', disabledforeground='#800000')
        Label(frames[0], text='среда').pack(side=RIGHT)

        frame_10 = Frame(frames[1])
        frame_10.pack(side=RIGHT)
        int_var_100 = IntVar(frame_10)
        checkbutton_100 = Checkbutton(
            frame_10, variable=int_var_100, onvalue=1, offvalue=0,
            text='отказ от сдачи пробы биологического объекта (мочи)',
        )
        checkbutton_100.grid(row=0, sticky=W)
        int_var_101 = IntVar(frame_10)
        checkbutton_101 = Checkbutton(
            frame_10, variable=int_var_101, onvalue=1, offvalue=0,
            text='фальсификация пробы биологического объекта (мочи)',
        )
        checkbutton_101.grid(row=1)

        Label(frames[2], text='метод исследования').pack(side=LEFT)
        methods = database.get_methods()
        string_var_20 = StringVar(frames[2])
        option_menu_20 = OptionMenu(
            frames[2], string_var_20, *methods)
        option_menu_20.config(font='-size 10', fg='#800000')
        option_menu_20.pack(fill=X)

        line = 'Результаты химико-токсикологических исследований'
        Label(frames[3], text=line).pack(side=LEFT)
        Label(frames[3], text=time.strftime('/%y')).pack(side=RIGHT)
        Entry(frames[3], width=5, font='-size 10', fg='#800000').pack(
            side=RIGHT)
        Label(frames[3], text='номер справки').pack(side=RIGHT)

        chemicals = database.get_chemicals()
        frames_4 = []
        for i in range(11):
            row, column = int(i / 2), (i % 2) * 2 + 1
            frames_4.append(Frame(frames[4]))
            frames_4[i].grid(row=row, column=column, sticky=W+E)
            Label(frames_4[i], text=chemicals[i]).pack(side=LEFT)
            SmartLabel(frames_4[i], text=plus)
            SmartLabel(frames_4[i], text=minus)
            Entry(
                frames_4[i], width=3, font='-size 10', fg='#800000',
                state='disabled', disabledforeground='#800000',
            ).pack(side=RIGHT)

    def paragraph_15(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 2)

        Label(frames[0], text='15. Другие данные').pack(side=LEFT)
        entry_10 = Entry(frames[1], font='-size 10', fg='#800000')
        entry_10.pack(fill=X)
        entry_10.insert(0, 'нет')

    def paragraph_17(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 3)

        Label(frames[0], text='17. Заключение').pack(side=LEFT)
        entry = Entry(
            frames[2], font='-size 10', fg='#800000',
            state='disabled', disabledforeground='#800000',
        )
        entry.pack(side=LEFT, expand=True, fill=X)
        Label(frames[2], text='Дата').pack(side=LEFT)
        date = DateEntry(frames[2])
        SmartLabel(
            frames[0], text='от медицинского освидетельствования отказался',
            bind=('replace_2', entry, date),
        )
        SmartLabel(
            frames[1], text='состояние опьянения не установлено',
            bind=('replace_2', entry, date),
        )
        SmartLabel(
            frames[1], text='установлено состояние опьянения',
            bind=('replace_2', entry, date),
        )

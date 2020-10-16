import time
from tkinter import (
    Entry, Frame, Label, LabelFrame, LEFT, OptionMenu, RIGHT, StringVar, X)
from widget.widget import DateEntry, SmartLabel, TimeEntry


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
        frame_0 = Frame(frame)
        frame_0.grid(row=0, column=0)
        label_00 = Label(frame_0, text='Акт №')
        label_00.grid(row=0, column=0, columnspan=2)
        entry_00 = Entry(frame_0, width=4, font='-size 10', fg='#800000',
                          state='disabled', disabledforeground='#800000')
        entry_00.grid(row=1, column=0)
        label_01 = Label(frame_0, text=time.strftime('/%y'))
        label_01.grid(row=1, column=1)

    def paragraph_1(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)

        frame_0 = Frame(frame)
        frame_0.pack(fill=X)
        label_00 = Label(
            frame_0, text='1. Сведения об освидетельствуемом лице')
        label_00.pack(side=LEFT)
        label_01 = Label(frame_0, text='Дата рождения')
        label_01.pack(side=RIGHT)

        frame_1 = Frame(frame)
        frame_1.pack(fill=X)
        label_10 = Label(frame_1, text='Фамилия, имя, отчество')
        label_10.pack(side=LEFT)
        entry_10 = Entry(frame_1, font='-size 10', fg='#800000')
        entry_10.pack(side=LEFT, expand=True, fill=X)
        DateEntry(frame_1)

        frame_2 = Frame(frame)
        frame_2.pack(fill=X)
        label_20 = Label(frame_2, text='Адрес места жительства')
        label_20.pack(side=LEFT)

        frame_3 = Frame(frame)
        frame_3.pack(fill=X)
        SmartLabel(frame_3, text='г. Комсомольск-на-Амуре')
        SmartLabel(frame_3, text='Комсомольский район')
        SmartLabel(frame_3, text='Хабаровский край')

        frame_4 = Frame(frame)
        frame_4.pack(fill=X)
        entry_40 = Entry(frame_4, font='-size 10', fg='#800000')
        entry_40.pack(fill=X)

        frame_5 = Frame(frame)
        frame_5.pack(fill=X)
        line = 'Сведения об освидетельствуемом лице заполнены на основании'
        label_50 = Label(frame_5, text=line)
        label_50.pack(side=LEFT)
        SmartLabel(frame_5, text='протокола')

        frame_6 = Frame(frame)
        frame_6.pack(fill=X)
        entry_60 = Entry(frame_6, font='-size 10', fg='#800000')
        entry_60.pack(side=LEFT, expand=True, fill=X)
        SmartLabel(frame_6, text='водительского удостоверения', place=LEFT)
        SmartLabel(frame_6, text='паспорта', place=LEFT)

    def paragraph_2(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)

        frame_0 = Frame(frame)
        frame_0.pack(fill=X)
        line = '2. Основание для медицинского освидетельствования'
        label_00 = Label(frame_0, text=line)
        label_00.pack(side=LEFT)

        frame_1 = Frame(frame)
        frame_1.pack(fill=X)
        SmartLabel(
            frame_1,
            text='протокол о направлении на медицинское освидетельствование'
        )

        frame_2 = Frame(frame)
        frame_2.pack(fill=X)
        SmartLabel(frame_2, text='личное заявление')
        SmartLabel(frame_2, text='письменное направление работодателя')

        frame_3 = Frame(frame)
        frame_3.pack(fill=X)
        entry_30 = Entry(frame_3, font='-size 10', fg='#800000')
        entry_30.pack(fill=X)

        frame_4 = Frame(frame)
        frame_4.pack(fill=X)
        label_40 = Label(frame_4, text='Кем направлен (ФИО)')
        label_40.pack(side=LEFT)
        entry_40 = Entry(frame_4, font='-size 10', fg='#800000')
        entry_40.pack(side=LEFT, expand=True, fill=X)

    @staticmethod
    def paragraph_4(frame):
        frame_1 = Frame(frame)
        frame_1.grid(row=0, column=2)
        label_10 = Label(frame_1, text='4. Начало освидетельствования')
        label_10.pack()
        label_11 = Label(frame_1, text='Дата')
        label_11.pack(side=LEFT)
        DateEntry(frame_1, time.strftime('%d.%m.%Y'))
        label_12 = Label(frame_1, text='Время')
        label_12.pack(side=LEFT)
        TimeEntry(frame_1, time.strftime('%H:%M'))

    def paragraph_5(self, database):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)

        frame_0 = Frame(frame)
        frame_0.pack(fill=X)
        label_00 = Label(frame_0, text='5. Кем освидетельствован')
        label_00.pack(side=LEFT)

        frame_1 = Frame(frame)
        frame_1.pack(fill=X)
        doctors = database.get_doctors()
        string_var_10 = StringVar(frame_1)
        if len(doctors) == 1:
            string_var_10.set(doctors[0])
        option_menu_10 = OptionMenu(frame_1, string_var_10, *doctors)
        option_menu_10.config(font='-size 10', fg='#800000')
        option_menu_10.pack(fill=X)

    @staticmethod
    def paragraph_16(frame):
        frame_2 = Frame(frame)
        frame_2.grid(row=0, column=4)
        label_20 = Label(frame_2, text='16. Окончание освидетельствования')
        label_20.pack()
        label_21 = Label(frame_2, text='Дата')
        label_21.pack(side=LEFT)
        DateEntry(frame_2, time.strftime('%d.%m.%Y'))
        label_22 = Label(frame_2, text='Время')
        label_22.pack(side=LEFT)
        TimeEntry(frame_2, time.strftime('%H:%M'))

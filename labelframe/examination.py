import time
from tkinter import (Checkbutton, E, Entry, Frame, IntVar, Label, LabelFrame,
                     LEFT, OptionMenu, RIGHT, StringVar, W, X)
from widget.func import key_release_result, key_release_time
from widget.widget import DateEntry, SmartLabel

minus, plus = '«-»', '«+»'


class ExaminationFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(self, text='Данные освидетельствования')
        self.paragraph_13(database)
        self.paragraph_14(database)
        self.paragraph_15()
        self.paragraph_17()

    def paragraph_13(self, database):
        frame_a = Frame(self, bd=4)
        frame_a.pack(fill=X)

        frame_a0 = Frame(frame_a)
        frame_a0.pack(fill=X)
        line = '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого'
        label_a00 = Label(frame_a0, text=line)
        label_a00.pack(side=LEFT)

        frame_a1 = Frame(frame_a)
        frame_a1.pack(fill=X)
        frame_a1.columnconfigure(1, weight=1)
        frame_a1.columnconfigure(3, weight=1)
        label_a10 = Label(frame_a1, text='13.1. Первое исследование')
        label_a10.grid(row=0, column=0)

        frame_a10 = Frame(frame_a1)
        frame_a10.grid(row=0, column=2)
        label_a100 = Label(frame_a10, text='Время')
        label_a100.pack(side=LEFT)
        entry_a100 = Entry(frame_a10, width=5, font='-size 10', fg='#800000')
        entry_a100.pack(side=LEFT)
        entry_a100.insert(0, time.strftime('%H:%M'))
        entry_a100.bind('<KeyRelease>', key_release_time)

        frame_a11 = Frame(frame_a1)
        frame_a11.grid(row=0, column=4)
        label_a110 = Label(frame_a11, text='Результат')
        label_a110.pack(side=LEFT)
        entry_a110 = Entry(frame_a11, width=4, font='-size 10', fg='#800000')
        entry_a110.pack(side=LEFT)
        entry_a110.bind('<KeyRelease>', key_release_result)
        label_a111 = Label(frame_a11, text='мг/л')
        label_a111.pack(side=LEFT)

        frame_a2 = Frame(frame_a)
        frame_a2.pack(fill=X)
        label_a20 = Label(frame_a2, text='техническое средство')
        label_a20.pack(side=LEFT)
        technical_means = database.get_technical_means()
        string_var_a20 = StringVar(frame_a2)
        option_menu_a20 = OptionMenu(
            frame_a2, string_var_a20, *technical_means)
        option_menu_a20.config(font='-size 10', fg='#800000')
        option_menu_a20.pack(fill=X)

        frame_a3 = Frame(frame_a)
        frame_a3.pack(fill=X)
        int_var_a30 = IntVar(frame_a3)
        checkbutton_a30 = Checkbutton(
            frame_a3, variable=int_var_a30, onvalue=1, offvalue=0,
            text='фальсификация выдоха')
        checkbutton_a30.pack(side=RIGHT)

        frame_a4 = Frame(frame_a)
        frame_a4.pack(fill=X)
        frame_a4.columnconfigure(1, weight=1)
        frame_a4.columnconfigure(3, weight=1)
        label_a40 = Label(frame_a4, text='13.2. Второе исследование')
        label_a40.grid(row=0, column=0)

        frame_a40 = Frame(frame_a4)
        frame_a40.grid(row=0, column=2)
        label_a400 = Label(frame_a40, text='Время')
        label_a400.pack(side=LEFT)
        entry_a400 = Entry(frame_a40, width=5, font='-size 10', fg='#800000')
        entry_a400.pack(side=LEFT)
        entry_a400.bind('<KeyRelease>', key_release_time)

        frame_a41 = Frame(frame_a4)
        frame_a41.grid(row=0, column=4)
        label_a410 = Label(frame_a41, text='Результат')
        label_a410.pack(side=LEFT)
        entry_a410 = Entry(frame_a41, width=4, font='-size 10', fg='#800000')
        entry_a410.pack(side=LEFT)
        entry_a410.bind('<KeyRelease>', key_release_result)
        label_a411 = Label(frame_a41, text='мг/л')
        label_a411.pack(side=LEFT)

        frame_a5 = Frame(frame_a)
        frame_a5.pack(fill=X)
        label_a50 = Label(frame_a5, text='техническое средство')
        label_a50.pack(side=LEFT)
        string_var_a50 = StringVar(frame_a5)
        option_menu_a50 = OptionMenu(
            frame_a5, string_var_a50, *technical_means)
        option_menu_a50.config(font='-size 10', fg='#800000')
        option_menu_a50.pack(fill=X)

    def paragraph_14(self, database):
        frame_b = Frame(self, bd=4)
        frame_b.pack(fill=X)

        frame_b0 = Frame(frame_b)
        frame_b0.pack(fill=X)
        line = '14. Время отбора биологического объекта'
        label_b00 = Label(frame_b0, text=line)
        label_b00.pack(side=LEFT)
        entry_b00 = Entry(frame_b0, width=5, font='-size 10', fg='#800000')
        entry_b00.pack(side=LEFT)
        entry_b00.bind('<KeyRelease>', key_release_time)
        smart_label_b00 = SmartLabel(frame_b0, text='кровь')
        smart_label_b00.pack(side=RIGHT)
        entry_b01 = Entry(frame_b0, width=5, font='-size 10', fg='#800000')
        entry_b01.pack(side=RIGHT)
        entry_b01.insert(0, 'моча')
        entry_b01.config(state='disabled', disabledforeground='#800000')
        label_b01 = Label(frame_b0, text='среда')
        label_b01.pack(side=RIGHT)

        frame_b1 = Frame(frame_b)
        frame_b1.pack(fill=X)
        frame_b10 = Frame(frame_b1)
        frame_b10.pack(side=RIGHT)
        int_var_b100 = IntVar(frame_b10)
        checkbutton_b100 = Checkbutton(
            frame_b10, variable=int_var_b100, onvalue=1, offvalue=0,
            text='отказ от сдачи пробы биологического объекта (мочи)')
        checkbutton_b100.grid(row=0, sticky=W)
        int_var_b101 = IntVar(frame_b10)
        checkbutton_b101 = Checkbutton(
            frame_b10, variable=int_var_b101, onvalue=1, offvalue=0,
            text='фальсификация пробы биологического объекта (мочи)')
        checkbutton_b101.grid(row=1)

        frame_b2 = Frame(frame_b)
        frame_b2.pack(fill=X)
        label_b20 = Label(frame_b2, text='метод исследования')
        label_b20.pack(side=LEFT)
        methods = database.get_methods()
        string_var_b20 = StringVar(frame_b2)
        option_menu_b20 = OptionMenu(
            frame_b2, string_var_b20, *methods)
        option_menu_b20.config(font='-size 10', fg='#800000')
        option_menu_b20.pack(fill=X)

        frame_b3 = Frame(frame_b)
        frame_b3.pack(fill=X)
        line = 'Результаты химико-токсикологических исследований'
        label_b30 = Label(frame_b3, text=line)
        label_b30.pack(side=LEFT)
        label_b31 = Label(frame_b3, text=time.strftime('/%y'))
        label_b31.pack(side=RIGHT)
        entry_b30 = Entry(frame_b3, width=5, font='-size 10', fg='#800000')
        entry_b30.pack(side=RIGHT)
        label_b32 = Label(frame_b3, text='номер справки')
        label_b32.pack(side=RIGHT)

        chemicals = database.get_chemicals()
        frame_b4 = Frame(frame_b)
        frame_b4.pack(fill=X)
        frame_b4.columnconfigure(0, weight=1)
        frame_b4.columnconfigure(2, weight=1)
        frame_b4.columnconfigure(4, weight=1)

        frames_b4, labels_b4, entries_b4 = [], [], []
        smart_labels_b4 = [[], []]
        for i in range(11):
            row, column = int(i / 2), (i % 2) * 2 + 1
            frames_b4.append(Frame(frame_b4))
            frames_b4[i].grid(row=row, column=column, sticky=W+E)
            labels_b4.append(Label(frames_b4[i], text=chemicals[i]))
            labels_b4[i].pack(side=LEFT)
            smart_labels_b4[0].append(SmartLabel(frames_b4[i], text=plus))
            smart_labels_b4[0][i].pack(side=RIGHT)
            smart_labels_b4[1].append(SmartLabel(frames_b4[i], text=minus))
            smart_labels_b4[1][i].pack(side=RIGHT)
            entries_b4.append(Entry(
                frames_b4[i], width=3, font='-size 10', fg='#800000',
                state='disabled', disabledforeground='#800000')
            )
            entries_b4[i].pack(side=RIGHT)

    def paragraph_15(self):
        frame_c = Frame(self, bd=4)
        frame_c.pack(fill=X)

        frame_c0 = Frame(frame_c)
        frame_c0.pack(fill=X)
        label_c00 = Label(frame_c0, text='15. Другие данные')
        label_c00.pack(side=LEFT)

        frame_c1 = Frame(frame_c)
        frame_c1.pack(fill=X)
        entry_c10 = Entry(frame_c1, font='-size 10', fg='#800000')
        entry_c10.pack(fill=X)
        entry_c10.insert(0, 'нет')

    def paragraph_17(self):
        frame_d = Frame(self, bd=4)
        frame_d.pack(fill=X)

        frame_d0 = Frame(frame_d)
        frame_d0.pack(fill=X)
        label_d00 = Label(frame_d0, text='17. Заключение')
        label_d00.pack(side=LEFT)
        line = 'от медицинского освидетельствования отказался'
        smart_label_d00 = SmartLabel(frame_d0, text=line)
        smart_label_d00.pack(side=RIGHT)

        frame_d1 = Frame(frame_d)
        frame_d1.pack(fill=X)
        line = 'состояние опьянения не установлено'
        smart_label_d10 = SmartLabel(frame_d1, text=line)
        smart_label_d10.pack(side=RIGHT)
        line = 'установлено состояние опьянения'
        smart_label_d11 = SmartLabel(frame_d1, text=line)
        smart_label_d11.pack(side=RIGHT)

        frame_d2 = Frame(frame_d)
        frame_d2.pack(fill=X)
        entry_d20 = Entry(frame_d2, font='-size 10', fg='#800000',
                          state='disabled', disabledforeground='#800000')
        entry_d20.pack(side=LEFT, expand=True, fill=X)
        label_d20 = Label(frame_d2, text='Дата')
        label_d20.pack(side=LEFT)
        DateEntry(frame_d2)

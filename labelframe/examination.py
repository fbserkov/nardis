import time
from tkinter import (Checkbutton, Entry, Frame, IntVar, Label, LabelFrame,
                     LEFT, OptionMenu, RIGHT, StringVar, W, X)
from widget.smartlabel import SmartLabel


class ExaminationFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(self, text='Данные освидетельствования')

        # пункт 13
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

        frame_a11 = Frame(frame_a1)
        frame_a11.grid(row=0, column=4)
        label_a110 = Label(frame_a11, text='Результат')
        label_a110.pack(side=LEFT)
        entry_a110 = Entry(frame_a11, width=4, font='-size 10', fg='#800000')
        entry_a110.pack(side=LEFT)
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

        frame_a41 = Frame(frame_a4)
        frame_a41.grid(row=0, column=4)
        label_a410 = Label(frame_a41, text='Результат')
        label_a410.pack(side=LEFT)
        entry_a410 = Entry(frame_a41, width=4, font='-size 10', fg='#800000')
        entry_a410.pack(side=LEFT)
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

        # пункт 14
        frame_b = Frame(self, bd=4)
        frame_b.pack(fill=X)

        frame_b0 = Frame(frame_b)
        frame_b0.pack(fill=X)
        line = '14. Время отбора биологического объекта'
        label_b00 = Label(frame_b0, text=line)
        label_b00.pack(side=LEFT)
        entry_b00 = Entry(frame_b0, width=5, font='-size 10', fg='#800000')
        entry_b00.pack(side=LEFT)
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

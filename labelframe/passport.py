import time
from tkinter import (Entry, Frame, Label, LabelFrame, LEFT,
                     OptionMenu, RIGHT, StringVar, X)
from widget.func import key_release_time
from widget.widget import DateEntry, SmartLabel


class PassportFrame(LabelFrame):
    def __init__(self, database):
        LabelFrame.__init__(self, text='Паспортная часть')
        self.paragraphs_0_4_16()
        self.paragraph_1()
        self.paragraph_2()
        self.paragraph_5(database)

    def paragraphs_0_4_16(self):
        frame_a = Frame(self, bd=4)
        frame_a.pack(fill=X)
        frame_a.columnconfigure(1, weight=1)
        frame_a.columnconfigure(3, weight=1)

        frame_a0 = Frame(frame_a)
        frame_a0.grid(row=0, column=0)
        label_a00 = Label(frame_a0, text='Акт №')
        label_a00.grid(row=0, column=0, columnspan=2)
        entry_a00 = Entry(frame_a0, width=4, font='-size 10', fg='#800000',
                          state='disabled', disabledforeground='#800000')
        entry_a00.grid(row=1, column=0)
        label_a01 = Label(frame_a0, text=time.strftime('/%y'))
        label_a01.grid(row=1, column=1)

        frame_a1 = Frame(frame_a)
        frame_a1.grid(row=0, column=2)
        label_a10 = Label(frame_a1, text='4. Начало освидетельствования')
        label_a10.pack()
        label_a11 = Label(frame_a1, text='Дата')
        label_a11.pack(side=LEFT)
        DateEntry(frame_a1, time.strftime('%d.%m.%Y'))
        label_a12 = Label(frame_a1, text='Время')
        label_a12.pack(side=LEFT)
        entry_a11 = Entry(frame_a1, width=5, font='-size 10', fg='#800000')
        entry_a11.pack(side=LEFT)
        entry_a11.insert(0, time.strftime('%H:%M'))
        entry_a11.bind('<KeyRelease>', key_release_time)

        frame_a2 = Frame(frame_a)
        frame_a2.grid(row=0, column=4)
        label_a20 = Label(frame_a2, text='16. Окончание освидетельствования')
        label_a20.pack()
        label_a21 = Label(frame_a2, text='Дата')
        label_a21.pack(side=LEFT)
        DateEntry(frame_a2, time.strftime('%d.%m.%Y'))
        label_a22 = Label(frame_a2, text='Время')
        label_a22.pack(side=LEFT)
        entry_a21 = Entry(frame_a2, width=5, font='-size 10', fg='#800000')
        entry_a21.pack(side=LEFT)
        entry_a21.insert(0, time.strftime('%H:%M'))
        entry_a21.bind('<KeyRelease>', key_release_time)

    def paragraph_1(self):
        frame_b = Frame(self, bd=4)
        frame_b.pack(fill=X)

        frame_b0 = Frame(frame_b)
        frame_b0.pack(fill=X)
        label_b00 = Label(
            frame_b0, text='1. Сведения об освидетельствуемом лице')
        label_b00.pack(side=LEFT)
        label_b01 = Label(frame_b0, text='Дата рождения')
        label_b01.pack(side=RIGHT)

        frame_b1 = Frame(frame_b)
        frame_b1.pack(fill=X)
        label_b10 = Label(frame_b1, text='Фамилия, имя, отчество')
        label_b10.pack(side=LEFT)
        entry_b10 = Entry(frame_b1, font='-size 10', fg='#800000')
        entry_b10.pack(side=LEFT, expand=True, fill=X)
        DateEntry(frame_b1)

        frame_b2 = Frame(frame_b)
        frame_b2.pack(fill=X)
        label_b20 = Label(frame_b2, text='Адрес места жительства')
        label_b20.pack(side=LEFT)

        frame_b3 = Frame(frame_b)
        frame_b3.pack(fill=X)
        smart_label_b32 = SmartLabel(frame_b3, text='г. Комсомольск-на-Амуре')
        smart_label_b32.pack(side=RIGHT)
        smart_label_b31 = SmartLabel(frame_b3, text='Комсомольский район')
        smart_label_b31.pack(side=RIGHT)
        smart_label_b30 = SmartLabel(frame_b3, text='Хабаровский край')
        smart_label_b30.pack(side=RIGHT)

        frame_b4 = Frame(frame_b)
        frame_b4.pack(fill=X)
        entry_b40 = Entry(frame_b4, font='-size 10', fg='#800000')
        entry_b40.pack(fill=X)

        frame_b5 = Frame(frame_b)
        frame_b5.pack(fill=X)
        line = 'Сведения об освидетельствуемом лице заполнены на основании'
        label_b50 = Label(frame_b5, text=line)
        label_b50.pack(side=LEFT)
        smart_label_b50 = SmartLabel(frame_b5, text='протокола')
        smart_label_b50.pack(side=RIGHT)

        frame_b6 = Frame(frame_b)
        frame_b6.pack(fill=X)
        entry_b60 = Entry(frame_b6, font='-size 10', fg='#800000')
        entry_b60.pack(side=LEFT, expand=True, fill=X)
        smart_label_b60 = SmartLabel(
            frame_b6, text='водительского удостоверения')
        smart_label_b60.pack(side=LEFT)
        smart_label_b61 = SmartLabel(frame_b6, text='паспорта')
        smart_label_b61.pack(side=LEFT)

    def paragraph_2(self):
        frame_c = Frame(self, bd=4)
        frame_c.pack(fill=X)

        frame_c0 = Frame(frame_c)
        frame_c0.pack(fill=X)
        line = '2. Основание для медицинского освидетельствования'
        label_c00 = Label(frame_c0, text=line)
        label_c00.pack(side=LEFT)

        frame_c1 = Frame(frame_c)
        frame_c1.pack(fill=X)
        line = 'протокол о направлении на медицинское освидетельствование'
        smart_label_c10 = SmartLabel(frame_c1, text=line)
        smart_label_c10.pack(side=RIGHT)

        frame_c2 = Frame(frame_c)
        frame_c2.pack(fill=X)
        smart_label_c21 = SmartLabel(frame_c2, text='личное заявление')
        smart_label_c21.pack(side=RIGHT)
        line = 'письменное направление работодателя'
        smart_label_c20 = SmartLabel(frame_c2, text=line)
        smart_label_c20.pack(side=RIGHT)

        frame_c3 = Frame(frame_c)
        frame_c3.pack(fill=X)
        entry_c30 = Entry(frame_c3, font='-size 10', fg='#800000')
        entry_c30.pack(fill=X)

        frame_c4 = Frame(frame_c)
        frame_c4.pack(fill=X)
        label_c40 = Label(frame_c4, text='Кем направлен (ФИО)')
        label_c40.pack(side=LEFT)
        entry_c40 = Entry(frame_c4, font='-size 10', fg='#800000')
        entry_c40.pack(side=LEFT, expand=True, fill=X)

    def paragraph_5(self, database):
        frame_d = Frame(self, bd=4)
        frame_d.pack(fill=X)

        frame_d0 = Frame(frame_d)
        frame_d0.pack(fill=X)
        label_d00 = Label(frame_d0, text='5. Кем освидетельствован')
        label_d00.pack(side=LEFT)

        frame_d1 = Frame(frame_d)
        frame_d1.pack(fill=X)
        doctors = database.get_doctors()
        string_var_d10 = StringVar(frame_d1)
        if len(doctors) == 1:
            string_var_d10.set(doctors[0])
        option_menu_d10 = OptionMenu(frame_d1, string_var_d10, *doctors)
        option_menu_d10.config(font='-size 10', fg='#800000')
        option_menu_d10.pack(fill=X)

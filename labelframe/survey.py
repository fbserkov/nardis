from tkinter import E, Entry, Frame, Label, LabelFrame, LEFT, W, X
from widget.widget import SmartLabel


class SurveyFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text='Объективный осмотр')

        # пункт 9
        frame_a = Frame(self, bd=4)
        frame_a.pack(fill=X)

        frame_a0 = Frame(frame_a)
        frame_a0.pack(fill=X)
        line = '9. Вегетативно-сосудистые реакции освидетельствуемого'
        label_a00 = Label(frame_a0, text=line)
        label_a00.pack(side=LEFT)

        frame_a1 = Frame(frame_a)
        frame_a1.pack(fill=X)
        frame_a1.columnconfigure(1, weight=1)

        label_a10 = Label(frame_a1, text='зрачки')
        label_a10.grid(row=0, column=0, sticky=W)
        label_a11 = Label(frame_a1, text='реакция на свет')
        label_a11.grid(row=1, column=0, sticky=W)
        label_a12 = Label(frame_a1, text='склеры')
        label_a12.grid(row=2, column=0, sticky=W)
        label_a13 = Label(frame_a1, text='нистагм')
        label_a13.grid(row=3, column=0, sticky=W)

        entry_a10 = Entry(frame_a1, font='-size 10', fg='#800000')
        entry_a10.grid(row=0, column=1, sticky=W+E)
        entry_a10.insert(0, 'в норме')
        entry_a10.config(state='disabled', disabledforeground='#800000')
        entry_a11 = Entry(frame_a1, font='-size 10', fg='#800000')
        entry_a11.grid(row=1, column=1, sticky=W+E)
        entry_a11.insert(0, 'живая')
        entry_a11.config(state='disabled', disabledforeground='#800000')
        entry_a12 = Entry(frame_a1, font='-size 10', fg='#800000')
        entry_a12.grid(row=2, column=1, sticky=W+E)
        entry_a12.insert(0, 'обычные')
        entry_a12.config(state='disabled', disabledforeground='#800000')
        entry_a13 = Entry(frame_a1, font='-size 10', fg='#800000')
        entry_a13.grid(row=3, column=1, sticky=W+E)
        entry_a13.insert(0, 'нет')
        entry_a13.config(state='disabled', disabledforeground='#800000')

        frame_a10 = Frame(frame_a1)
        frame_a10.grid(row=0, column=2, sticky=E)
        SmartLabel(frame_a10, text='расширены')
        SmartLabel(frame_a10, text='сужены')

        SmartLabel(
            frame_a1, text='вялая', place=dict(row=1, column=2, sticky=E))
        SmartLabel(
            frame_a1, text='инъекция сосудов конъюнктивы',
            place=dict(row=2, column=2, sticky=E)
        )
        SmartLabel(
            frame_a1, text='есть', place=dict(row=3, column=2, sticky=E))

        # пункт 10
        frame_b = Frame(self, bd=4)
        frame_b.pack(fill=X)

        frame_b0 = Frame(frame_b)
        frame_b0.pack(fill=X)
        line = '10. Двигательная сфера освидетельствуемого'
        label_b00 = Label(frame_b0, text=line)
        label_b00.pack(side=LEFT)

        frame_b1 = Frame(frame_b)
        frame_b1.pack(fill=X)
        label_b10 = Label(frame_b1, text='речь')
        label_b10.pack(side=LEFT)
        SmartLabel(frame_b1, text='речь бессвязная')
        SmartLabel(frame_b1, text='смазанность речи')
        SmartLabel(frame_b1, text='нарушение артикуляции')

        frame_b2 = Frame(frame_b)
        frame_b2.pack(fill=X)
        entry_b20 = Entry(frame_b2, font='-size 10', fg='#800000')
        entry_b20.pack(fill=X)
        entry_b20.insert(0, 'речевая способность сохранена')
        entry_b20.config(state='disabled', disabledforeground='#800000')

        frame_b3 = Frame(frame_b)
        frame_b3.pack(fill=X)
        label_b30 = Label(frame_b3, text='походка')
        label_b30.pack(side=LEFT)
        SmartLabel(frame_b3, text='пошатывание при поворотах')
        SmartLabel(frame_b3, text='шатающаяся')

        frame_b4 = Frame(frame_b)
        frame_b4.pack(fill=X)
        entry_b40 = Entry(frame_b4, font='-size 10', fg='#800000')
        entry_b40.pack(fill=X)
        entry_b40.insert(0, 'уверенная')
        entry_b40.config(state='disabled', disabledforeground='#800000')

        frame_b5 = Frame(frame_b)
        frame_b5.pack(fill=X)
        label_b50 = Label(frame_b5, text='устойчивость в позе Ромберга')
        label_b50.pack(side=LEFT)
        entry_b50 = Entry(frame_b5, font='-size 10', fg='#800000')
        entry_b50.pack(side=LEFT, expand=True, fill=X)
        entry_b50.insert(0, 'не проводилось')
        entry_b50.config(state='disabled', disabledforeground='#800000')
        SmartLabel(frame_b5, text='устойчив', place=LEFT)
        SmartLabel(frame_b5, text='неустойчив', place=LEFT)
        SmartLabel(frame_b5, text='падает', place=LEFT)

        frame_b6 = Frame(frame_b)
        frame_b6.pack(fill=X)
        line = 'точность выполнения координационных проб'
        label_b60 = Label(frame_b6, text=line)
        label_b60.pack(side=LEFT)

        frame_b7 = Frame(frame_b)
        frame_b7.pack(fill=X)
        entry_b70 = Entry(frame_b7, font='-size 10', fg='#800000')
        entry_b70.pack(side=LEFT, expand=True, fill=X)
        entry_b70.insert(0, 'не проводилось')
        entry_b70.config(state='disabled', disabledforeground='#800000')
        SmartLabel(frame_b7, text='выполняет точно', place=LEFT)
        SmartLabel(frame_b7, text='промахивание', place=LEFT)
        SmartLabel(frame_b7, text='не выполняет', place=LEFT)

        frame_b8 = Frame(frame_b)
        frame_b8.pack(fill=X)
        label_b80 = Label(frame_b8, text='результат пробы Ташена')
        label_b80.pack(side=LEFT)
        entry_b80 = Entry(frame_b8, width=2, font='-size 10', fg='#800000')
        entry_b80.pack(side=LEFT)
        label_b81 = Label(frame_b8, text='сек.')
        label_b81.pack(side=LEFT)

        # пункт 11
        frame_c = Frame(self, bd=4)
        frame_c.pack(fill=X)

        frame_c0 = Frame(frame_c)
        frame_c0.pack(fill=X)
        line = ('11. Наличие заболеваний нервной системы' +
                ', психических расстройств,')
        label_c00 = Label(frame_c0, text=line)
        label_c00.pack(side=LEFT)

        frame_c1 = Frame(frame_c)
        frame_c1.pack(fill=X)
        line = 'перенесённых травм (со слов освидетельствуемого)'
        label_c10 = Label(frame_c1, text=line)
        label_c10.pack(side=LEFT)

        frame_c2 = Frame(frame_c)
        frame_c2.pack(fill=X)
        entry_c20 = Entry(frame_c2, font='-size 10', fg='#800000')
        entry_c20.pack(fill=X)
        entry_c20.insert(0, 'нет')

        # пункт 12
        frame_d = Frame(self, bd=4)
        frame_d.pack(fill=X)

        frame_d0 = Frame(frame_d)
        frame_d0.pack(fill=X)
        line = ('12. Сведения о последнем употреблении алкоголя' +
                ', лекарственных средств,')
        label_d00 = Label(frame_d0, text=line)
        label_d00.pack(side=LEFT)

        frame_d1 = Frame(frame_d)
        frame_d1.pack(fill=X)
        line = ('наркотических средств и психотропных веществ' +
                ' (со слов освидетельствуемого)')
        label_d10 = Label(frame_d1, text=line)
        label_d10.pack(side=LEFT)

        frame_d2 = Frame(frame_d)
        frame_d2.pack(fill=X)
        entry_d20 = Entry(frame_d2, font='-size 10', fg='#800000')
        entry_d20.pack(side=LEFT, expand=True, fill=X)
        SmartLabel(frame_d2, text='отрицает', place=LEFT)
        SmartLabel(frame_d2, text='употреблял спиртное', place=LEFT)

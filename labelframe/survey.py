from tkinter import E, Entry, Frame, Label, LabelFrame, LEFT, W, X
from widget.widget import get_frames, SmartLabel


class SurveyFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text='Объективный осмотр')
        self.paragraph_9()
        self.paragraph_10()
        self.paragraph_11()
        self.paragraph_12()

    def paragraph_9(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 2)
        frames[1].columnconfigure(1, weight=1)

        line = '9. Вегетативно-сосудистые реакции освидетельствуемого'
        Label(frames[0], text=line).pack(side=LEFT)
        Label(frames[1], text='зрачки').grid(row=0, column=0, sticky=W)
        Label(frames[1], text='реакция на свет').grid(row=1, column=0, sticky=W)
        Label(frames[1], text='склеры').grid(row=2, column=0, sticky=W)
        Label(frames[1], text='нистагм').grid(row=3, column=0, sticky=W)

        entry_10 = Entry(frames[1], font='-size 10', fg='#800000')
        entry_10.grid(row=0, column=1, sticky=W+E)
        entry_10.insert(0, 'в норме')
        entry_10.config(state='disabled', disabledforeground='#800000')
        entry_11 = Entry(frames[1], font='-size 10', fg='#800000')
        entry_11.grid(row=1, column=1, sticky=W+E)
        entry_11.insert(0, 'живая')
        entry_11.config(state='disabled', disabledforeground='#800000')
        entry_12 = Entry(frames[1], font='-size 10', fg='#800000')
        entry_12.grid(row=2, column=1, sticky=W+E)
        entry_12.insert(0, 'обычные')
        entry_12.config(state='disabled', disabledforeground='#800000')
        entry_13 = Entry(frames[1], font='-size 10', fg='#800000')
        entry_13.grid(row=3, column=1, sticky=W+E)
        entry_13.insert(0, 'нет')
        entry_13.config(state='disabled', disabledforeground='#800000')

        frame_10 = Frame(frames[1])
        frame_10.grid(row=0, column=2, sticky=E)
        SmartLabel(frame_10, text='расширены')
        SmartLabel(frame_10, text='сужены')

        SmartLabel(
            frames[1], text='вялая', place=dict(row=1, column=2, sticky=E))
        SmartLabel(
            frames[1], text='инъекция сосудов конъюнктивы',
            place=dict(row=2, column=2, sticky=E),
        )
        SmartLabel(
            frames[1], text='есть', place=dict(row=3, column=2, sticky=E))

    def paragraph_10(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 9)

        line = '10. Двигательная сфера освидетельствуемого'
        Label(frames[0], text=line).pack(side=LEFT)
        Label(frames[1], text='речь').pack(side=LEFT)
        SmartLabel(frames[1], text='речь бессвязная')
        SmartLabel(frames[1], text='смазанность речи')
        SmartLabel(frames[1], text='нарушение артикуляции')
        entry_20 = Entry(frames[2], font='-size 10', fg='#800000')
        entry_20.pack(fill=X)
        entry_20.insert(0, 'речевая способность сохранена')
        entry_20.config(state='disabled', disabledforeground='#800000')

        Label(frames[3], text='походка').pack(side=LEFT)
        SmartLabel(frames[3], text='пошатывание при поворотах')
        SmartLabel(frames[3], text='шатающаяся')
        entry_40 = Entry(frames[4], font='-size 10', fg='#800000')
        entry_40.pack(fill=X)
        entry_40.insert(0, 'уверенная')
        entry_40.config(state='disabled', disabledforeground='#800000')
        Label(frames[5], text='устойчивость в позе Ромберга').pack(side=LEFT)
        entry_50 = Entry(frames[5], font='-size 10', fg='#800000')
        entry_50.pack(side=LEFT, expand=True, fill=X)
        entry_50.insert(0, 'не проводилось')
        entry_50.config(state='disabled', disabledforeground='#800000')
        SmartLabel(frames[5], text='устойчив', place=LEFT)
        SmartLabel(frames[5], text='неустойчив', place=LEFT)
        SmartLabel(frames[5], text='падает', place=LEFT)

        line = 'точность выполнения координационных проб'
        Label(frames[6], text=line).pack(side=LEFT)
        entry_70 = Entry(frames[7], font='-size 10', fg='#800000')
        entry_70.pack(side=LEFT, expand=True, fill=X)
        entry_70.insert(0, 'не проводилось')
        entry_70.config(state='disabled', disabledforeground='#800000')
        SmartLabel(frames[7], text='выполняет точно', place=LEFT)
        SmartLabel(frames[7], text='промахивание', place=LEFT)
        SmartLabel(frames[7], text='не выполняет', place=LEFT)
        Label(frames[8], text='результат пробы Ташена').pack(side=LEFT)
        Entry(frames[8], width=2, font='-size 10', fg='#800000').pack(side=LEFT)
        Label(frames[8], text='сек.').pack(side=LEFT)

    def paragraph_11(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 3)

        line = (
            '11. Наличие заболеваний нервной системы, ' +
            'психических расстройств,'
        )
        Label(frames[0], text=line).pack(side=LEFT)
        line = 'перенесённых травм (со слов освидетельствуемого)'
        Label(frames[1], text=line).pack(side=LEFT)
        entry_20 = Entry(frames[2], font='-size 10', fg='#800000')
        entry_20.pack(fill=X)
        entry_20.insert(0, 'нет')

    def paragraph_12(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 3)

        line = (
            '12. Сведения о последнем употреблении алкоголя, ' +
            'лекарственных средств,'
        )
        Label(frames[0], text=line).pack(side=LEFT)
        line = (
            'наркотических средств и психотропных веществ ' +
            '(со слов освидетельствуемого)'
        )
        Label(frames[1], text=line).pack(side=LEFT)
        entry = Entry(frames[2], font='-size 10', fg='#800000')
        entry.pack(side=LEFT, expand=True, fill=X)
        SmartLabel(
            frames[2], text='отрицает', place=LEFT, bind=(entry, 'replace'))
        SmartLabel(
            frames[2], text='употреблял спиртное',
            place=LEFT, bind=(entry, 'replace'),
        )

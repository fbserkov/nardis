from tkinter import E, Entry, Frame, Label, LabelFrame, LEFT, W, X

from labelframe import get_frames
from widget.label import SmartLabel


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
        Label(frames[1], text='реакция на свет').grid(
            row=1, column=0, sticky=W)
        Label(frames[1], text='склеры').grid(row=2, column=0, sticky=W)
        Label(frames[1], text='нистагм').grid(row=3, column=0, sticky=W)
        entries, defaults = [], ('в норме', 'живая', 'обычные', 'нет')
        for i, text in enumerate(defaults):
            entries.append(Entry(frames[1], font='-size 10', fg='#800000'))
            entries[i].grid(row=i, column=1, sticky=W + E)
            entries[i].insert(0, text)
            entries[i].config(state='disabled', disabledforeground='#800000')
        frame = Frame(frames[1])
        frame.grid(row=0, column=2, sticky=E)
        SmartLabel(
            frame, text='расширены',
            bind=('replace_smart', entries[0], defaults[0]),
        )
        SmartLabel(
            frame, text='сужены',
            bind=('replace_smart', entries[0], defaults[0]),
        )
        for i, text in enumerate(
                ('вялая', 'инъекция сосудов конъюнктивы', 'есть')):
            SmartLabel(
                frames[1], text,
                bind=('replace_smart', entries[i + 1], defaults[i + 1]),
                place=dict(row=i + 1, column=2, sticky=E),
            )

    def paragraph_10(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 9)
        line = '10. Двигательная сфера освидетельствуемого'
        Label(frames[0], text=line).pack(side=LEFT)

        default = 'речевая способность сохранена'
        entry = Entry(frames[2], font='-size 10', fg='#800000')
        entry.pack(fill=X)
        entry.insert(0, default)
        entry.config(state='disabled', disabledforeground='#800000')
        Label(frames[1], text='речь').pack(side=LEFT)
        for text in \
                'речь бессвязная', 'смазанность речи', 'нарушение артикуляции':
            SmartLabel(frames[1], text, bind=('add_smart', entry, default))

        default = 'уверенная'
        entry = Entry(frames[4], font='-size 10', fg='#800000')
        entry.pack(fill=X)
        entry.insert(0, default)
        entry.config(state='disabled', disabledforeground='#800000')
        Label(frames[3], text='походка').pack(side=LEFT)
        for text in 'пошатывание при поворотах', 'шатающаяся':
            SmartLabel(frames[3], text, bind=('add_smart', entry, default))

        Label(frames[5], text='устойчивость в позе Ромберга').pack(side=LEFT)
        default = 'не проводилось'
        entry = Entry(frames[5], font='-size 10', fg='#800000')
        entry.pack(side=LEFT, expand=True, fill=X)
        entry.insert(0, default)
        entry.config(state='disabled', disabledforeground='#800000')
        for text in 'устойчив', 'неустойчив', 'падает':
            SmartLabel(
                frames[5], text,
                bind=('replace_smart', entry, default), place=LEFT,
            )

        line = 'точность выполнения координационных проб'
        Label(frames[6], text=line).pack(side=LEFT)
        entry = Entry(frames[7], font='-size 10', fg='#800000')
        entry.pack(side=LEFT, expand=True, fill=X)
        entry.insert(0, default)
        entry.config(state='disabled', disabledforeground='#800000')
        for text in 'выполняет точно', 'промахивание', 'не выполняет':
            SmartLabel(
                frames[7], text,
                bind=('replace_smart', entry, default), place=LEFT,
            )

        Label(frames[8], text='результат пробы Ташена').pack(side=LEFT)
        Entry(frames[8], width=2, font='-size 10', fg='#800000').pack(
            side=LEFT)
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
        entry = Entry(frames[2], font='-size 10', fg='#800000')
        entry.pack(fill=X)
        entry.insert(0, 'нет')

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
            frames[2], text='отрицает', bind=('replace', entry), place=LEFT)
        SmartLabel(
            frames[2], text='употреблял спиртное',
            bind=('replace', entry), place=LEFT,
        )

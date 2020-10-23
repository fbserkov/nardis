from tkinter import E, Frame, Label, LabelFrame, LEFT, W, X

from item import ItemBase
from widget.entry import EntryBase, EntryDisabled
from widget.label import LabelAddSmart, LabelReplace, LabelReplaceSmart


class SurveyFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Объективный осмотр')
        self.paragraph_9()
        self.paragraph_10()
        self.paragraph_11()
        self.paragraph_12()

    def init(self):
        pass

    def paragraph_9(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = ItemBase.get_frames(frame, length=2)
        frames[1].columnconfigure(1, weight=1)
        line = '9. Вегетативно-сосудистые реакции освидетельствуемого'
        Label(frames[0], text=line).pack(side=LEFT)

        Label(frames[1], text='зрачки').grid(row=0, column=0, sticky=W)
        Label(frames[1], text='реакция на свет').grid(
            row=1, column=0, sticky=W)
        Label(frames[1], text='склеры').grid(row=2, column=0, sticky=W)
        Label(frames[1], text='нистагм').grid(row=3, column=0, sticky=W)
        entries, defaults = [], ('в норме', 'живая', 'обычные', 'нет')
        for i, default in enumerate(defaults):
            entries.append(EntryDisabled(frames[1], default=default))
            entries[i].grid(row=i, column=1, sticky=W + E)
        frame = Frame(frames[1])
        frame.grid(row=0, column=2, sticky=E)
        LabelReplaceSmart(
            frame, text='расширены', bind=(entries[0], defaults[0]))
        LabelReplaceSmart(frame, text='сужены', bind=(entries[0], defaults[0]))
        for i, text in enumerate(
                ('вялая', 'инъекция сосудов конъюнктивы', 'есть')):
            LabelReplaceSmart(
                frames[1], text, bind=(entries[i + 1], defaults[i + 1]),
                place=dict(row=i + 1, column=2, sticky=E),
            )

    def paragraph_10(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = ItemBase.get_frames(frame, length=9)
        line = '10. Двигательная сфера освидетельствуемого'
        Label(frames[0], text=line).pack(side=LEFT)

        default = 'речевая способность сохранена'
        entry = EntryDisabled(frames[2], default=default)
        entry.pack(fill=X)
        Label(frames[1], text='речь').pack(side=LEFT)
        for text in \
                'речь бессвязная', 'смазанность речи', 'нарушение артикуляции':
            LabelAddSmart(frames[1], text, bind=(entry, default))

        default = 'уверенная'
        entry = EntryDisabled(frames[4], default=default)
        entry.pack(fill=X)
        Label(frames[3], text='походка').pack(side=LEFT)
        for text in 'пошатывание при поворотах', 'шатающаяся':
            LabelAddSmart(frames[3], text, bind=(entry, default))

        Label(frames[5], text='устойчивость в позе Ромберга').pack(side=LEFT)
        default = 'не проводилось'
        entry = EntryDisabled(frames[5], default=default)
        entry.pack(side=LEFT, expand=True, fill=X)
        for text in 'устойчив', 'неустойчив', 'падает':
            LabelReplaceSmart(
                frames[5], text, bind=(entry, default), place=LEFT)

        line = 'точность выполнения координационных проб'
        Label(frames[6], text=line).pack(side=LEFT)
        entry = EntryDisabled(frames[7], default=default)
        entry.pack(side=LEFT, expand=True, fill=X)
        for text in 'выполняет точно', 'промахивание', 'не выполняет':
            LabelReplaceSmart(
                frames[7], text, bind=(entry, default), place=LEFT)

        Label(frames[8], text='результат пробы Ташена').pack(side=LEFT)
        EntryBase(frames[8], width=2).pack(side=LEFT)
        Label(frames[8], text='сек.').pack(side=LEFT)

    def paragraph_11(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = ItemBase.get_frames(frame, length=3)

        line = (
            '11. Наличие заболеваний нервной системы, ' +
            'психических расстройств,'
        )
        Label(frames[0], text=line).pack(side=LEFT)
        line = 'перенесённых травм (со слов освидетельствуемого)'
        Label(frames[1], text=line).pack(side=LEFT)
        entry = EntryBase(frames[2])
        entry.pack(fill=X)
        entry.insert(0, 'нет')

    def paragraph_12(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = ItemBase.get_frames(frame, length=3)

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
        entry = EntryBase(frames[2])
        entry.pack(side=LEFT, expand=True, fill=X)
        LabelReplace(frames[2], text='отрицает', bind=entry, place=LEFT)
        LabelReplace(
            frames[2], text='употреблял спиртное', bind=entry, place=LEFT)

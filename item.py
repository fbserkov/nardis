import time
from tkinter import Checkbutton, E, Frame, IntVar, Label, LEFT, RIGHT, W, X

from widget.entry import (
    EntryBase, EntryDate, EntryDisabled, EntryResult, EntryTime, EntryYear)
from widget.label import (
    LabelAdd, LabelAddSmart, LabelReplace,
    LabelReplaceSmart, LabelReplaceSmartDate,
)
from widget.option_menu import OptionMenuSmart


class ItemBase:
    frame = None

    def __init__(self, master, frames_number=None):
        frame = Frame(master, bd=4)
        frame.pack(fill=X)
        if frames_number:
            self.frames = self.get_frames(frame, frames_number)
        else:
            if not ItemBase.frame:
                ItemBase.frame = Frame(master, bd=4)
                ItemBase.frame.pack(fill=X)
                ItemBase.frame.columnconfigure(1, weight=1)
                ItemBase.frame.columnconfigure(3, weight=1)
            self.frame = Frame(ItemBase.frame)

    @staticmethod
    def get_frames(master, length):
        frames = []
        for i in range(length):
            frame = Frame(master)
            frame.pack(fill=X)
            frames.append(frame)
        return frames


class Item0(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=0)
        Label(self.frame, text='Акт №').grid(row=0, column=0, columnspan=2)
        EntryDisabled(self.frame, width=4).grid(row=1, column=0)
        Label(self.frame, text='/').grid(row=1, column=1)
        EntryYear(
            self.frame, default=time.strftime('%y')).grid(row=1, column=2)


class Item1(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=7)
        Label(
            self.frames[0],
            text='1. Сведения об освидетельствуемом лице',
        ).pack(side=LEFT)
        Label(self.frames[0], text='Дата рождения').pack(side=RIGHT)
        Label(self.frames[1], text='Фамилия, имя, отчество').pack(side=LEFT)
        EntryBase(self.frames[1]).pack(side=LEFT, expand=True, fill=X)
        EntryDate(self.frames[1])

        Label(self.frames[2], text='Адрес места жительства').pack(side=LEFT)
        entry = EntryBase(self.frames[4])
        entry.pack(fill=X)
        LabelAdd(self.frames[3], text='г. Комсомольск-на-Амуре', bind=entry)
        LabelAdd(self.frames[3], text='Комсомольский район', bind=entry)
        LabelAdd(self.frames[3], text='Хабаровский край', bind=entry)

        line = 'Сведения об освидетельствуемом лице заполнены на основании'
        Label(self.frames[5], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[6])
        entry.pack(side=LEFT, expand=True, fill=X)
        LabelReplace(self.frames[5], text='протокола', bind=entry)
        line = 'водительского удостоверения'
        LabelReplace(self.frames[6], text=line, bind=entry, place=LEFT)
        LabelReplace(self.frames[6], text='паспорта', bind=entry, place=LEFT)


class Item2(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=5)
        line = '2. Основание для медицинского освидетельствования'
        Label(self.frames[0], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[3])
        entry.pack(fill=X)
        line = 'протокол о направлении на медицинское освидетельствование'
        LabelReplace(self.frames[1], text=line, bind=entry)
        LabelReplace(self.frames[2], text='личное заявление', bind=entry)
        line = 'письменное направление работодателя'
        LabelReplace(self.frames[2], text=line, bind=entry)
        Label(self.frames[4], text='Кем направлен (ФИО)').pack(side=LEFT)
        EntryBase(self.frames[4]).pack(side=LEFT, expand=True, fill=X)


class Item3(ItemBase):
    pass


class Item4(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=2)
        Label(self.frame, text='4. Начало освидетельствования').pack()
        Label(self.frame, text='Дата').pack(side=LEFT)
        EntryDate(self.frame, time.strftime('%d.%m.%Y'))
        Label(self.frame, text='Время').pack(side=LEFT)
        EntryTime(self.frame, time.strftime('%H:%M'))


class Item5(ItemBase):
    def __init__(self, master, database):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='5. Кем освидетельствован').pack(side=LEFT)
        doctors = database.get_doctors()
        OptionMenuSmart(
            self.frames[1], doctors, doctors[0] if len(doctors) == 1 else None)


class Item6(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='6. Внешний вид освидетельствуемого').pack(
            side=LEFT)
        entry = EntryBase(self.frames[1], width=69)
        entry.pack(fill=X)
        entry.insert(
            0, 'внешний вид и кожные покровы без особенностей, ' +
            'видимых повреждений нет',
        )


class Item7(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        line = '7. Жалобы освидетельствуемого на своё состояние'
        Label(self.frames[0], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[1])
        entry.pack(fill=X)
        entry.insert(0, 'не предъявляет')


class Item8(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=8)
        line = '8. Изменения психической деятельности освидетельствуемого'
        Label(self.frames[0], text=line).pack(side=LEFT)

        Label(self.frames[1], text='состояние сознания').pack(side=LEFT)
        entry = EntryBase(self.frames[1])
        entry.pack(side=LEFT, expand=True, fill=X)
        for text in 'ясное', 'оглушение', 'сопор', 'кома':
            LabelReplace(self.frames[1], text, bind=entry, place=LEFT)

        default = 'без особенностей'
        entry = EntryDisabled(self.frames[4], default=default)
        entry.pack(fill=X)
        Label(self.frames[2], text='поведение').pack(side=LEFT)
        for text in (
                'эйфоричен', 'агрессивен', 'возбуждён',
                'раздражён', 'замкнут', 'напряжён'
        ):
            LabelAddSmart(self.frames[2], text, bind=(entry, default))
        for text in (
                'заторможен', 'сонлив', 'настроение '
                                        'неустойчиво', 'суетлив', 'болтлив',
        ):
            LabelAddSmart(self.frames[3], text, bind=(entry, default))

        line = 'ориентировка в месте, времени, ситуации'
        Label(self.frames[5], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[6])
        entry.pack(side=LEFT, expand=True, fill=X)
        for text in 'ориентирован', 'ориентация снижена', 'дезориентирован':
            LabelReplace(self.frames[6], text, bind=entry, place=LEFT)

        Label(self.frames[7], text='результат пробы Шульте').pack(side=LEFT)
        EntryBase(self.frames[7], width=2).pack(side=LEFT)
        Label(self.frames[7], text='сек.').pack(side=LEFT)


class Item9(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        self.frames[1].columnconfigure(1, weight=1)
        line = '9. Вегетативно-сосудистые реакции освидетельствуемого'
        Label(self.frames[0], text=line).pack(side=LEFT)

        Label(self.frames[1], text='зрачки').grid(row=0, column=0, sticky=W)
        Label(self.frames[1], text='реакция на свет').grid(
            row=1, column=0, sticky=W)
        Label(self.frames[1], text='склеры').grid(row=2, column=0, sticky=W)
        Label(self.frames[1], text='нистагм').grid(row=3, column=0, sticky=W)
        entries, defaults = [], ('в норме', 'живая', 'обычные', 'нет')
        for i, default in enumerate(defaults):
            entries.append(EntryDisabled(self.frames[1], default=default))
            entries[i].grid(row=i, column=1, sticky=W + E)
        frame = Frame(self.frames[1])
        frame.grid(row=0, column=2, sticky=E)
        LabelReplaceSmart(
            frame, text='расширены', bind=(entries[0], defaults[0]))
        LabelReplaceSmart(frame, text='сужены', bind=(entries[0], defaults[0]))
        for i, text in enumerate(
                ('вялая', 'инъекция сосудов конъюнктивы', 'есть')):
            LabelReplaceSmart(
                self.frames[1], text, bind=(entries[i + 1], defaults[i + 1]),
                place=dict(row=i + 1, column=2, sticky=E),
            )


class Item10(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=9)
        line = '10. Двигательная сфера освидетельствуемого'
        Label(self.frames[0], text=line).pack(side=LEFT)

        default = 'речевая способность сохранена'
        entry = EntryDisabled(self.frames[2], default=default)
        entry.pack(fill=X)
        Label(self.frames[1], text='речь').pack(side=LEFT)
        for text in \
                'речь бессвязная', 'смазанность речи', 'нарушение артикуляции':
            LabelAddSmart(self.frames[1], text, bind=(entry, default))

        default = 'уверенная'
        entry = EntryDisabled(self.frames[4], default=default)
        entry.pack(fill=X)
        Label(self.frames[3], text='походка').pack(side=LEFT)
        for text in 'пошатывание при поворотах', 'шатающаяся':
            LabelAddSmart(self.frames[3], text, bind=(entry, default))

        Label(self.frames[5], text='устойчивость в позе Ромберга').pack(
            side=LEFT)
        default = 'не проводилось'
        entry = EntryDisabled(self.frames[5], default=default)
        entry.pack(side=LEFT, expand=True, fill=X)
        for text in 'устойчив', 'неустойчив', 'падает':
            LabelReplaceSmart(
                self.frames[5], text, bind=(entry, default), place=LEFT)

        line = 'точность выполнения координационных проб'
        Label(self.frames[6], text=line).pack(side=LEFT)
        entry = EntryDisabled(self.frames[7], default=default)
        entry.pack(side=LEFT, expand=True, fill=X)
        for text in 'выполняет точно', 'промахивание', 'не выполняет':
            LabelReplaceSmart(
                self.frames[7], text, bind=(entry, default), place=LEFT)

        Label(self.frames[8], text='результат пробы Ташена').pack(side=LEFT)
        EntryBase(self.frames[8], width=2).pack(side=LEFT)
        Label(self.frames[8], text='сек.').pack(side=LEFT)


class Item11(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=3)
        line = '11. Наличие заболеваний нервной системы, '\
            'психических расстройств,'
        Label(self.frames[0], text=line).pack(side=LEFT)
        line = 'перенесённых травм (со слов освидетельствуемого)'
        Label(self.frames[1], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[2])
        entry.pack(fill=X)
        entry.insert(0, 'нет')


class Item12(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=3)
        line = '12. Сведения о последнем употреблении алкоголя, '\
            'лекарственных средств,'
        Label(self.frames[0], text=line).pack(side=LEFT)
        line = (
                'наркотических средств и психотропных веществ ' +
                '(со слов освидетельствуемого)'
        )
        Label(self.frames[1], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[2])
        entry.pack(side=LEFT, expand=True, fill=X)
        LabelReplace(self.frames[2], text='отрицает', bind=entry, place=LEFT)
        LabelReplace(
            self.frames[2], text='употреблял спиртное', bind=entry, place=LEFT)


class Item13(ItemBase):
    def __init__(self, master, database):
        ItemBase.__init__(self, master, frames_number=6)
        for i in 1, 4:
            self.frames[i].columnconfigure(1, weight=1)
            self.frames[i].columnconfigure(3, weight=1)
        line = '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого'
        Label(self.frames[0], text=line).pack(side=LEFT)

        Label(self.frames[1], text='13.1. Первое исследование').grid(
            row=0, column=0)
        frame = Frame(self.frames[1])
        frame.grid(row=0, column=2)
        Label(frame, text='Время').pack(side=LEFT)
        EntryTime(frame, time.strftime('%H:%M'))
        frame = Frame(self.frames[1])
        frame.grid(row=0, column=4)
        Label(frame, text='Результат').pack(side=LEFT)
        EntryResult(frame)
        Label(frame, text='мг/л').pack(side=LEFT)
        Label(self.frames[2], text='техническое средство').pack(side=LEFT)
        technical_means = database.get_technical_means()
        OptionMenuSmart(self.frames[2], technical_means)
        Checkbutton(
            self.frames[3], variable=IntVar(self.frames[3]),
            onvalue=1, offvalue=0, text='фальсификация выдоха',
        ).pack(side=RIGHT)

        Label(self.frames[4], text='13.2. Второе исследование').grid(
            row=0, column=0)
        frame = Frame(self.frames[4])
        frame.grid(row=0, column=2)
        Label(frame, text='Время').pack(side=LEFT)
        EntryTime(frame)
        frame = Frame(self.frames[4])
        frame.grid(row=0, column=4)
        Label(frame, text='Результат').pack(side=LEFT)
        EntryResult(frame)
        Label(frame, text='мг/л').pack(side=LEFT)
        Label(self.frames[5], text='техническое средство').pack(side=LEFT)
        OptionMenuSmart(self.frames[5], technical_means)


class Item14(ItemBase):
    def __init__(self, master, database):
        ItemBase.__init__(self, master, frames_number=5)
        line = '14. Время отбора биологического объекта'
        Label(self.frames[0], text=line).pack(side=LEFT)
        EntryTime(self.frames[0])
        default = 'моча'
        entry = EntryDisabled(self.frames[0], width=5, default=default)
        LabelReplaceSmart(self.frames[0], text='кровь', bind=(entry, default))
        entry.pack(side=RIGHT)
        Label(self.frames[0], text='среда').pack(side=RIGHT)
        frame = Frame(self.frames[1])
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
        Label(self.frames[2], text='метод исследования').pack(side=LEFT)
        OptionMenuSmart(self.frames[2], database.get_methods())

        line = 'Результаты химико-токсикологических исследований'
        Label(self.frames[3], text=line).pack(side=LEFT)
        EntryYear(self.frames[3], default=time.strftime('%y')).pack(side=RIGHT)
        Label(self.frames[3], text=time.strftime('/')).pack(side=RIGHT)
        EntryBase(self.frames[3], width=5).pack(side=RIGHT)
        Label(self.frames[3], text='номер справки').pack(side=RIGHT)
        self.frames[4].columnconfigure(0, weight=1)
        self.frames[4].columnconfigure(2, weight=1)
        self.frames[4].columnconfigure(4, weight=1)
        chemicals = database.get_chemicals()
        for i in range(11):
            row, column = int(i / 2), (i % 2) * 2 + 1
            frame = Frame(self.frames[4])
            frame.grid(row=row, column=column, sticky=W + E)
            Label(frame, text=chemicals[i]).pack(side=LEFT)
            entry = EntryDisabled(frame, width=4)
            LabelReplaceSmart(frame, text='«+»', bind=(entry, ''))
            LabelReplaceSmart(frame, text='«-»', bind=(entry, ''))
            entry.pack(side=RIGHT)


class Item15(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='15. Другие данные').pack(side=LEFT)
        entry = EntryBase(self.frames[1])
        entry.pack(fill=X)
        entry.insert(0, 'нет')


class Item16(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=4)
        Label(self.frame, text='16. Окончание освидетельствования').pack()
        Label(self.frame, text='Дата').pack(side=LEFT)
        EntryDate(self.frame, time.strftime('%d.%m.%Y'))
        Label(self.frame, text='Время').pack(side=LEFT)
        EntryTime(self.frame, time.strftime('%H:%M'))


class Item17(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=3)
        Label(self.frames[0], text='17. Заключение').pack(side=LEFT)
        entry = EntryDisabled(self.frames[2])
        entry.pack(side=LEFT, expand=True, fill=X)
        Label(self.frames[2], text='Дата').pack(side=LEFT)
        date = EntryDate(self.frames[2])
        for i, text in (
                (0, 'от медицинского освидетельствования отказался'),
                (1, 'состояние опьянения не установлено'),
                (1, 'установлено состояние опьянения'),
        ):
            LabelReplaceSmartDate(self.frames[i], text, bind=(entry, '', date))
from datetime import datetime

from tkinter import E, Frame, Label, LEFT, N, S, Scrollbar, RIGHT, W, X

from convert import date2str, str2date, str2datetime, str2time, time2str
from widget import (
    CheckbuttonSmart, EntryBase, EntryDate, EntryDisabled, EntryResult,
    EntryTime, EntryTimer, EntryYear, LabelAdd, LabelAddSmart, LabelReplace,
    LabelReplaceSmart, LabelReplaceSmartDate, ListboxSmart, OptionMenuSmart,
)


def create_item(master, i):
    cls_name = 'Item' + str(i)
    cls = globals()[cls_name]
    return cls(master)


class CheckException(Exception):
    def __init__(self, text=''):
        self.text = text

    def add(self, text):
        self.text += text


class ItemBase:
    db, frame = None, None

    def __init__(self, master, frames_number=None):
        self.widgets = []
        if frames_number:
            frame = Frame(master, bd=4)
            frame.pack(fill=X)
            self.frames = self.get_frames(frame, frames_number)
        else:
            if not ItemBase.frame:
                ItemBase.frame = Frame(master, bd=4)
                ItemBase.frame.pack(fill=X)
                ItemBase.frame.columnconfigure(1, weight=1)
                ItemBase.frame.columnconfigure(3, weight=1)
            self.frame = Frame(ItemBase.frame)

    def check(self, index):
        try:
            for widget in self.widgets:
                widget.check(CheckException())
        except CheckException as exc:
            exc.add('\nв пункте ' + str(index) + '.')
            raise exc

    @staticmethod
    def get_frames(master, length):
        frames = []
        for i in range(length):
            frame = Frame(master)
            frame.pack(fill=X)
            frames.append(frame)
        return frames

    def init(self):
        for widget in self.widgets:
            widget.init()


class Item0(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=0)

        Label(self.frame, text='Акт №').pack()
        entry = EntryDisabled(self.frame, width=4)
        entry.pack(side=LEFT)
        self.widgets.append(entry)

        Label(self.frame, text='/').pack(side=LEFT)
        entry = EntryYear(self.frame, '%y')
        entry.pack(side=LEFT)
        self.widgets.append(entry)

    def check(self, index):
        ItemBase.check(self, index)
        if not self.widgets[1].get():
            raise CheckException('Не указан год\nв пункте 0.')

    def insert(self):
        self.db.insert(0, 'organization', self.db.select('organization'))
        self.db.insert(0, 'number', int(self.widgets[0].get()))
        self.db.insert(0, 'year', int(self.widgets[1].get()))

    def select(self):
        self.widgets[0].init(self.db.select(0, 'number'))
        self.widgets[1].init(self.db.select(0, 'year'))

    def update_number(self):
        self.widgets[0].config(state='normal')
        self.widgets[0].insert(0, self.db.select('next_number'))
        self.widgets[0].config(state='disabled')


class Item1(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=7)
        Label(
            self.frames[0],
            text='1. Сведения об освидетельствуемом лице',
        ).pack(side=LEFT)
        Label(self.frames[0], text='Дата рождения').pack(side=RIGHT)
        Label(self.frames[1], text='Фамилия, имя, отчество').pack(side=LEFT)
        entry = EntryBase(self.frames[1])
        entry.pack(side=LEFT, expand=True, fill=X)
        self.widgets.append(entry)
        self.widgets.append(EntryDate(self.frames[1]))

        Label(self.frames[2], text='Адрес места жительства').pack(side=LEFT)
        entry = EntryBase(self.frames[4])
        entry.pack(fill=X)
        self.widgets.append(entry)
        LabelAdd(self.frames[3], text='г. Комсомольск-на-Амуре', bind=entry)
        LabelAdd(self.frames[3], text='Комсомольский район', bind=entry)
        LabelAdd(self.frames[3], text='Хабаровский край', bind=entry)

        line = 'Сведения об освидетельствуемом лице заполнены на основании'
        Label(self.frames[5], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[6])
        entry.pack(side=LEFT, expand=True, fill=X)
        self.widgets.append(entry)
        LabelReplace(self.frames[5], text='протокола', bind=entry)
        line = 'водительского удостоверения'
        LabelReplace(self.frames[6], text=line, bind=entry, place=LEFT)
        LabelReplace(self.frames[6], text='паспорта', bind=entry, place=LEFT)

    def check(self, index):
        ItemBase.check(self, index)
        if not self.widgets[0].get():
            raise CheckException('Не указано ФИО\nв пункте 1.')

    def insert(self):
        self.db.insert(1, 'full_name', self.widgets[0].get())
        self.db.insert(1, 'date', str2date(self.widgets[1].get()))
        self.db.insert(1, 'address', self.widgets[2].get())
        self.db.insert(1, 'document', self.widgets[3].get())

    def select(self):
        self.widgets[0].init(self.db.select(1, 'full_name'))
        self.widgets[1].init(date2str(self.db.select(1, 'date')))
        self.widgets[2].init(self.db.select(1, 'address'))
        self.widgets[3].init(self.db.select(1, 'document'))


class Item2(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=5)
        line = '2. Основание для медицинского освидетельствования'
        Label(self.frames[0], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[3])
        entry.pack(fill=X)
        self.widgets.append(entry)
        line = 'протокол о направлении на медицинское освидетельствование'
        LabelReplace(self.frames[1], text=line, bind=entry)
        LabelReplace(self.frames[2], text='личное заявление', bind=entry)
        line = 'письменное направление работодателя'
        LabelReplace(self.frames[2], text=line, bind=entry)

        Label(self.frames[4], text='Кем направлен (ФИО)').pack(side=LEFT)
        entry = EntryBase(self.frames[4])
        entry.pack(side=LEFT, expand=True, fill=X)
        self.widgets.append(entry)

    def insert(self):
        self.db.insert(2, 'document', self.widgets[0].get())
        self.db.insert(2, 'full_name', self.widgets[1].get())

    def select(self):
        self.widgets[0].init(self.db.select(2, 'document'))
        self.widgets[1].init(self.db.select(2, 'full_name'))


class Item3(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)

    def insert(self):
        self.db.insert(3, 'subdivision', self.db.select('subdivision'))

    @staticmethod
    def select():
        pass


class Item4(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=2)
        Label(self.frame, text='4. Начало освидетельствования').pack()
        Label(self.frame, text='Дата').pack(side=LEFT)
        self.widgets.append(EntryDate(self.frame, '%d.%m.%Y'))
        Label(self.frame, text='Время').pack(side=LEFT)
        self.widgets.append(EntryTime(self.frame, '%H:%M'))

    def check(self, index):
        ItemBase.check(self, index)
        if not self.widgets[0].get():
            raise CheckException('Не указана дата\nв пункте 4.')
        if not self.widgets[1].get():
            raise CheckException('Не указано время\nв пункте 4.')

    def insert(self):
        self.db.insert(4, 'datetime', datetime.combine(
            str2date(self.widgets[0].get()), str2time(self.widgets[1].get())))

    def select(self):
        temp = self.db.select(4, 'datetime')
        self.widgets[0].init(date2str(temp.date()))
        self.widgets[1].init(time2str(temp.time()))


class Item5(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='5. Кем освидетельствован').pack(side=LEFT)
        self.widgets.append(OptionMenuSmart(
            self.frames[1], self.db.get_doctors()))

    def check(self, index):
        ItemBase.check(self, index)
        if not self.widgets[0].string_var.get():
            raise CheckException('Не указан врач\nв пункте 5.')

    def insert(self):
        doctor, *training = self.widgets[0].string_var.get().split(', ')
        self.db.insert(5, 'doctor', doctor)
        self.db.insert(5, 'training', ', '.join(training))

    def select(self):
        self.widgets[0].string_var.set(
            self.db.select(5, 'doctor') + ', ' + self.db.select(5, 'training'))

    def update_doctor(self):
        if self.db.current_doctor:
            self.widgets[0].string_var.set(self.db.current_doctor)
            self.widgets[0]['state'] = 'disabled'
        else:
            self.widgets[0].string_var.set('')
            self.widgets[0]['state'] = 'normal'

    def update_menu(self):
        self.widgets[0].forget()
        self.widgets[0] = OptionMenuSmart(
            self.frames[1], self.db.get_doctors())


class Item6(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='6. Внешний вид освидетельствуемого').pack(
            side=LEFT)
        line = 'внешний вид и кожные покровы без особенностей, '\
            'видимых повреждений нет'
        entry = EntryBase(self.frames[1], width=69, default=line)
        entry.pack(fill=X)
        self.widgets.append(entry)

    def insert(self):
        self.db.insert(6, 'appearance', self.widgets[0].get())

    def select(self):
        self.widgets[0].init(self.db.select(6, 'appearance'))


class Item7(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        line = '7. Жалобы освидетельствуемого на своё состояние'
        Label(self.frames[0], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[1], default='не предъявляет')
        entry.pack(fill=X)
        self.widgets.append(entry)

    def insert(self):
        self.db.insert(7, 'complaints', self.widgets[0].get())

    def select(self):
        self.widgets[0].init(self.db.select(7, 'complaints'))


class Item8(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=8)
        line = '8. Изменения психической деятельности освидетельствуемого'
        Label(self.frames[0], text=line).pack(side=LEFT)

        Label(self.frames[1], text='состояние сознания').pack(side=LEFT)
        entry = EntryBase(self.frames[1])
        entry.pack(side=LEFT, expand=True, fill=X)
        self.widgets.append(entry)
        for text in 'ясное', 'оглушение', 'сопор', 'кома':
            LabelReplace(self.frames[1], text, bind=entry, place=LEFT)

        default = 'без особенностей'
        entry = EntryDisabled(self.frames[4], default=default)
        self.widgets.append(entry)
        entry.pack(fill=X)
        Label(self.frames[2], text='поведение').pack(side=LEFT)
        for text in (
                'эйфоричен', 'агрессивен', 'возбуждён',
                'раздражён', 'замкнут', 'напряжён'
        ):
            LabelAddSmart(self.frames[2], text, bind=(entry, default))
        for text in (
                'заторможен', 'сонлив', 'настроение неустойчиво',
                'суетлив', 'болтлив',
        ):
            LabelAddSmart(self.frames[3], text, bind=(entry, default))

        line = 'ориентировка в месте, времени, ситуации'
        Label(self.frames[5], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[6])
        entry.pack(side=LEFT, expand=True, fill=X)
        self.widgets.append(entry)
        for text in 'ориентирован', 'ориентация снижена', 'дезориентирован':
            LabelReplace(self.frames[6], text, bind=entry, place=LEFT)

        Label(self.frames[7], text='результат пробы Шульте').pack(side=LEFT)
        entry = EntryTimer(self.frames[7])
        self.widgets.append(entry)
        entry.pack(side=LEFT)
        Label(self.frames[7], text='сек.').pack(side=LEFT)

    def insert(self):
        schulte = self.widgets[3].get()
        self.db.insert(8, 'consciousness', self.widgets[0].get())
        self.db.insert(8, 'behavior', self.widgets[1].get())
        self.db.insert(8, 'orientation', self.widgets[2].get())
        self.db.insert(8, 'schulte', schulte + ' сек.' if schulte else '')

    def select(self):
        self.widgets[0].init(self.db.select(8, 'consciousness'))
        self.widgets[1].init(self.db.select(8, 'behavior'))
        self.widgets[2].init(self.db.select(8, 'orientation'))
        self.widgets[3].init(self.db.select(8, 'schulte').split(' ')[0])


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
            entry = EntryDisabled(self.frames[1], default=default)
            self.widgets.append(entry)
            entry.grid(row=i, column=1, sticky=W + E)
            entries.append(entry)
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

    def insert(self):
        self.db.insert(9, 'pupils', self.widgets[0].get())
        self.db.insert(9, 'reaction', self.widgets[1].get())
        self.db.insert(9, 'scleras', self.widgets[2].get())
        self.db.insert(9, 'nystagmus', self.widgets[3].get())

    def select(self):
        self.widgets[0].init(self.db.select(9, 'pupils'))
        self.widgets[1].init(self.db.select(9, 'reaction'))
        self.widgets[2].init(self.db.select(9, 'scleras'))
        self.widgets[3].init(self.db.select(9, 'nystagmus'))


class Item10(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=9)
        line = '10. Двигательная сфера освидетельствуемого'
        Label(self.frames[0], text=line).pack(side=LEFT)

        default = 'речевая способность сохранена'
        entry = EntryDisabled(self.frames[2], default=default)
        entry.pack(fill=X)
        self.widgets.append(entry)
        Label(self.frames[1], text='речь').pack(side=LEFT)
        for text in \
                'речь бессвязная', 'смазанность речи', 'нарушение артикуляции':
            LabelAddSmart(self.frames[1], text, bind=(entry, default))

        default = 'уверенная'
        entry = EntryDisabled(self.frames[4], default=default)
        entry.pack(fill=X)
        self.widgets.append(entry)
        Label(self.frames[3], text='походка').pack(side=LEFT)
        for text in 'пошатывание при поворотах', 'шатающаяся':
            LabelAddSmart(self.frames[3], text, bind=(entry, default))

        Label(self.frames[5], text='устойчивость в позе Ромберга').pack(
            side=LEFT)
        default = 'не проводилось'
        entry = EntryDisabled(self.frames[5], default=default)
        entry.pack(side=LEFT, expand=True, fill=X)
        self.widgets.append(entry)
        for text in 'устойчив', 'неустойчив', 'падает':
            LabelReplaceSmart(
                self.frames[5], text, bind=(entry, default), place=LEFT)

        line = 'точность выполнения координационных проб'
        Label(self.frames[6], text=line).pack(side=LEFT)
        entry = EntryDisabled(self.frames[7], default=default)
        entry.pack(side=LEFT, expand=True, fill=X)
        self.widgets.append(entry)
        for text in 'выполняет точно', 'промахивание', 'не выполняет':
            LabelReplaceSmart(
                self.frames[7], text, bind=(entry, default), place=LEFT)

        Label(self.frames[8], text='результат пробы Ташена').pack(side=LEFT)
        entry = EntryTimer(self.frames[8])
        entry.pack(side=LEFT)
        self.widgets.append(entry)
        Label(self.frames[8], text='сек.').pack(side=LEFT)

    def insert(self):
        tashen = self.widgets[4].get()
        self.db.insert(10, 'speech', self.widgets[0].get())
        self.db.insert(10, 'gait', self.widgets[1].get())
        self.db.insert(10, 'romberg', self.widgets[2].get())
        self.db.insert(10, 'coordination', self.widgets[3].get())
        self.db.insert(10, 'tashen', tashen + ' сек.' if tashen else '')

    def select(self):
        self.widgets[0].init(self.db.select(10, 'speech'))
        self.widgets[1].init(self.db.select(10, 'gait'))
        self.widgets[2].init(self.db.select(10, 'romberg'))
        self.widgets[3].init(self.db.select(10, 'coordination'))
        self.widgets[4].init(self.db.select(10, 'tashen').split(' ')[0])


class Item11(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=3)
        line = '11. Наличие заболеваний нервной системы, '\
            'психических расстройств,'
        Label(self.frames[0], text=line).pack(side=LEFT)
        line = 'перенесённых травм (со слов освидетельствуемого)'
        Label(self.frames[1], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[2], default='нет')
        entry.pack(fill=X)
        self.widgets.append(entry)

    def insert(self):
        self.db.insert(11, 'comorbidity', self.widgets[0].get())

    def select(self):
        self.widgets[0].init(self.db.select(11, 'comorbidity'))


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
        self.widgets.append(entry)
        LabelReplace(self.frames[2], text='отрицает', bind=entry, place=LEFT)
        LabelReplace(
            self.frames[2], text='употреблял спиртное', bind=entry, place=LEFT)

    def insert(self):
        self.db.insert(12, 'drug_use', self.widgets[0].get())

    def select(self):
        self.widgets[0].init(self.db.select(12, 'drug_use'))


class SubItem13:
    def __init__(self, n, frames, devices):
        self.frames = frames[1:3] if n == 1 else frames[4:]
        title = 'Первое' if n == 1 else 'Второе'
        default = '%H:%M' if n == 1 else None
        self.n, self.widgets = n, []

        for i in 1, 3, 5:
            self.frames[0].columnconfigure(i, weight=1)
        Label(self.frames[0], text=f'13.{n}. {title} исследование').grid(
            row=0, column=0)

        frame = Frame(self.frames[0])
        frame.grid(row=0, column=2)
        Label(frame, text='Дата').pack(side=LEFT)
        self.widgets.append(EntryDate(frame, '%d.%m.%Y'))

        frame = Frame(self.frames[0])
        frame.grid(row=0, column=4)
        Label(frame, text='Время').pack(side=LEFT)
        self.widgets.append(EntryTime(frame, default))

        frame = Frame(self.frames[0])
        frame.grid(row=0, column=6)
        Label(frame, text='Результат').pack(side=LEFT)
        self.widgets.append(EntryResult(frame))
        Label(frame, text='мг/л').pack(side=LEFT)

        Label(self.frames[1], text='техническое средство').pack(side=LEFT)
        self.widgets.append(OptionMenuSmart(self.frames[1], devices))

    def check(self):
        if self.widgets[2].get() and not self.widgets[0].get():
            raise CheckException(f'Не указана дата\nв пункте 13 ({self.n}).')
        if self.widgets[2].get() and not self.widgets[1].get():
            raise CheckException(f'Не указано время\nв пункте 13 ({self.n}).')
        if self.widgets[2].get() and not self.widgets[3].string_var.get():
            raise CheckException(f'Не указано ТС\nв пункте 13 ({self.n}).')

    def insert(self, db):
        result = self.widgets[2].get()
        db.insert(
            13, f'datetime_{self.n}',
            str2datetime(self.widgets[0].get() + ' ' + self.widgets[1].get()),
        )
        db.insert(13, f'result_{self.n}', result + ' мг/л' if result else '')
        db.insert(13, f'device_{self.n}', self.widgets[3].string_var.get())

    def select(self, db):
        temp = db.select(13, f'datetime_{self.n}')
        self.widgets[0].init(date2str(temp.date()) if temp else '')
        self.widgets[1].init(time2str(temp.time()) if temp else '')
        self.widgets[2].init(db.select(13, f'result_{self.n}').split(' ')[0])
        self.widgets[3].string_var.set(db.select(13, f'device_{self.n}'))

    def update_menu(self, devices):
        self.widgets[3].forget()
        self.widgets[3] = OptionMenuSmart(self.frames[1], devices)


class Item13(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=6)
        line = '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого'
        Label(self.frames[0], text=line).pack(side=LEFT)

        devices = self.db.select('devices')
        self.sub_item_1 = SubItem13(1, self.frames, devices)
        self.sub_item_2 = SubItem13(2, self.frames, devices)
        self.widgets.extend(self.sub_item_1.widgets + self.sub_item_2.widgets)

        self.forgery = 'фальсификация выдоха'
        checkbutton = CheckbuttonSmart(self.frames[3], line=self.forgery)
        checkbutton.pack(side=RIGHT)
        self.widgets.append(checkbutton)

    def check(self, index):
        ItemBase.check(self, index)
        self.sub_item_1.check()
        self.sub_item_2.check()

    def insert(self):
        self.sub_item_1.insert(self.db)
        self.sub_item_2.insert(self.db)
        if self.widgets[8].get():
            self.db.insert(13, 'result_1', self.forgery)

    def select(self):
        self.sub_item_1.select(self.db)
        self.sub_item_2.select(self.db)
        if self.db.select(13, 'result_1') == self.forgery:
            self.widgets[2].init('')
            self.widgets[8].set(1)

    def update_menu(self):
        devices = self.db.select('devices')
        self.sub_item_1.update_menu(devices)
        self.sub_item_2.update_menu(devices)


class Item14(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=5)
        line = '14. Время отбора биологического объекта'
        Label(self.frames[0], text=line).pack(side=LEFT)
        self.widgets.append(EntryTime(self.frames[0]))

        default = 'моча'
        entry = EntryDisabled(self.frames[0], width=5, default=default)
        LabelReplaceSmart(self.frames[0], text='кровь', bind=(entry, default))
        entry.pack(side=RIGHT)
        Label(self.frames[0], text='среда').pack(side=RIGHT)
        self.widgets.append(entry)

        frame = Frame(self.frames[1])
        frame.pack(side=RIGHT)
        self.refusal = 'отказ от сдачи пробы биологического объекта (мочи)'
        self.forgery = 'фальсификация пробы биологического объекта (мочи)'
        btn_1 = CheckbuttonSmart(frame, line=self.refusal)
        btn_2 = CheckbuttonSmart(frame, line=self.forgery)
        btn_1.bind('<Button-1>', lambda _: self._uncheck_extra(btn_1, btn_2))
        btn_2.bind('<Button-1>', lambda _: self._uncheck_extra(btn_2, btn_1))
        btn_1.grid(row=0, sticky=W)
        btn_2.grid(row=1)
        self.widgets.append(btn_1)
        self.widgets.append(btn_2)

        Label(self.frames[2], text='метод исследования').pack(side=LEFT)
        self.widgets.append(
            OptionMenuSmart(self.frames[2], self.db.select('methods')))

        line = 'Результаты химико-токсикологических исследований'
        Label(self.frames[3], text=line).pack(side=LEFT)
        entry = EntryYear(self.frames[3], '%y')
        entry.pack(side=RIGHT)
        self.widgets.append(entry)
        Label(self.frames[3], text='/').pack(side=RIGHT)
        entry = EntryBase(self.frames[3], width=5)
        entry.pack(side=RIGHT)
        self.widgets.append(entry)
        Label(self.frames[3], text='номер справки').pack(side=RIGHT)

        signs = '«-»', '«+»'
        lines = f'Отрицательные {signs[0]}:', f'Положительные {signs[1]}:'
        for i in range(2):
            self.frames[4].columnconfigure(i, weight=1)
            Label(self.frames[4], text=lines[i]).grid(row=0, column=i)
            listbox = ListboxSmart(
                self.frames[4], sign=signs[i],
                choices=self.db.select('substances'),
            )
            listbox.grid(row=1, column=i, sticky=E + W)
            self.widgets.append(listbox)

        def yview2(*args):
            self.widgets[7].yview(*args)
            self.widgets[8].yview(*args)
        scrollbar = Scrollbar(self.frames[4], command=yview2)
        scrollbar.grid(row=1, column=2, sticky=N + S)
        self.widgets[7]['yscrollcommand'] = scrollbar.set
        self.widgets[8]['yscrollcommand'] = scrollbar.set

    def _get_result(self):
        result = {}
        self.widgets[7].get_result(result)
        self.widgets[8].get_result(result)
        return result

    def _set_result(self, result):
        self.widgets[7].set_result(result)
        self.widgets[8].set_result(result)

    @staticmethod
    def _uncheck_extra(btn_1, btn_2):
        if btn_1.get():
            return
        if btn_2.get():
            btn_2.set(0)

    def _update_choices(self):
        substances = self.db.select('substances')
        self.widgets[7].update_choices(substances)
        self.widgets[8].update_choices(substances)

    def check(self, index):
        ItemBase.check(self, index)
        if self._get_result() and not self.widgets[0].get():
            raise CheckException('Не указано время\nв пункте 14.')
        if self._get_result() and not self.widgets[4].string_var.get():
            raise CheckException('Не указан метод\nв пункте 14.')
        if self._get_result() and not self.widgets[6].get():
            raise CheckException('Не указан номер справки\nв пункте 14.')
        if self.widgets[6].get() and not self.widgets[5].get():
            raise CheckException('Не указан год\nв пункте 14.')

    def insert(self):
        time, number = self.widgets[0].get(), self.widgets[6].get()
        self.db.insert(14, 'time', str2time(time))
        self.db.insert(14, 'material', self.widgets[1].get() if time else '')
        self.db.insert(
            14, 'laboratory', self.db.select('laboratory') if time else '')
        self.db.insert(14, 'method', self.widgets[4].string_var.get())
        self.db.insert(
            14, 'number',
            number + '/' + self.widgets[5].get() if number else '',
        )
        self.db.insert(14, 'result', self._get_result())

        line = self.refusal if self.widgets[2].get() else ''
        if self.widgets[3].get():
            line = self.forgery
        if line:
            self.db.insert(14, 'result', line)

    def select(self):
        material = self.db.select(14, 'material')
        self.widgets[0].init(time2str(self.db.select(14, 'time')))
        self.widgets[1].init(material if material else None)
        self.widgets[4].string_var.set(self.db.select(14, 'method'))

        temp = self.db.select(14, 'number')
        number, year = temp.split('/') if temp else ('', None)
        self.widgets[5].init(year)
        self.widgets[6].init(number)

        result = self.db.select(14, 'result')
        if result == self.refusal:
            self.widgets[2].set(1)
        elif result == self.forgery:
            self.widgets[3].set(1)
        else:
            self._set_result(result)

    def update_menu(self):
        self.widgets[4].forget()
        self.widgets[4] = OptionMenuSmart(
            self.frames[2], self.db.select('methods'))
        self._update_choices()


class Item15(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='15. Другие данные').pack(side=LEFT)
        entry = EntryBase(self.frames[1], default='нет')
        entry.pack(fill=X)
        self.widgets.append(entry)

    def insert(self):
        self.db.insert(15, 'other', self.widgets[0].get())

    def select(self):
        self.widgets[0].init(self.db.select(15, 'other'))


class Item16(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=4)
        Label(self.frame, text='16. Окончание освидетельствования').pack()
        Label(self.frame, text='Дата').pack(side=LEFT)
        self.widgets.append(EntryDate(self.frame, '%d.%m.%Y'))
        Label(self.frame, text='Время').pack(side=LEFT)
        self.widgets.append(EntryTime(self.frame, '%H:%M'))

    def check(self, index):
        ItemBase.check(self, index)
        if not self.widgets[0].get():
            raise CheckException('Не указана дата\nв пункте 16.')
        if not self.widgets[1].get():
            raise CheckException('Не указано время\nв пункте 16.')

    def insert(self):
        self.db.insert(16, 'datetime', datetime.combine(
            str2date(self.widgets[0].get()), str2time(self.widgets[1].get())))

    def select(self):
        temp = self.db.select(16, 'datetime')
        self.widgets[0].init(date2str(temp.date()))
        self.widgets[1].init(time2str(temp.time()))


class Item17(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=3)
        Label(self.frames[0], text='17. Заключение').pack(side=LEFT)
        entry = EntryDisabled(self.frames[2])
        self.widgets.append(entry)
        entry.pack(side=LEFT, expand=True, fill=X)
        Label(self.frames[2], text='Дата').pack(side=LEFT)
        date = EntryDate(self.frames[2])
        self.widgets.append(date)
        for i, text in (
                (0, 'от медицинского освидетельствования отказался'),
                (1, 'состояние опьянения не установлено'),
                (1, 'установлено состояние опьянения'),
        ):
            LabelReplaceSmartDate(self.frames[i], text, bind=(entry, '', date))

    def check(self, index):
        ItemBase.check(self, index)
        if not self.widgets[0].get():
            raise CheckException('Нет заключения\nв пункте 17.')
        if not self.widgets[1].get():
            raise CheckException('Не указана дата\nв пункте 17.')

    def insert(self):
        self.db.insert(17, 'opinion', self.widgets[0].get())
        self.db.insert(17, 'date', str2date(self.widgets[1].get()))

    def select(self):
        self.widgets[0].init(self.db.select(17, 'opinion'))
        self.widgets[1].init(date2str(self.db.select(17, 'date')))

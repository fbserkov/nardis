from datetime import datetime
from time import mktime, strptime

from tkinter import E, Frame, Label, LEFT, RIGHT, W, X

from widget import (
    CheckbuttonSmart, EntryBase, EntryDate, EntryDisabled, EntryResult,
    EntryTime, EntryTimer, EntryYear, LabelAdd, LabelAddSmart, LabelReplace,
    LabelReplaceSmart, LabelReplaceSmartDate, OptionMenuSmart,
)


def create_item(master, i):
    cls_name = 'Item' + str(i)
    cls = globals()[cls_name]
    return cls(master)


def str2datetime(datetime_):
    date, time = datetime_.split(' ')
    date, time = ItemBase.str2date(date), ItemBase.str2time(time)
    if not (date and time):
        return None
    return datetime.combine(date, time)


class CheckException(Exception):
    def __init__(self, text=''):
        self.text = text

    def add(self, text):
        self.text += text


class ItemBase:
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

    @staticmethod
    def str2date(date):
        if date == '':
            return None
        return datetime.strptime(date, '%d.%m.%Y').date()

    @staticmethod
    def str2time(time):
        if time == '':
            return None
        return datetime.strptime(time, '%H:%M').time()

    db, frame = None, None


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
        self.db.insert(0, 'organization', self.db.get_organization())
        self.db.insert(
            0, 'number', self.widgets[0].get() + '/' + self.widgets[1].get())

    def update_number(self):
        self.widgets[0].config(state='normal')
        self.widgets[0].insert(0, self.db.get_act_number())
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
        self.db.insert(1, 'date', self.str2date(self.widgets[1].get()))
        self.db.insert(1, 'address', self.widgets[2].get())
        self.db.insert(1, 'document', self.widgets[3].get())


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


class Item3(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)

    def insert(self):
        self.db.insert(3, 'subdivision', self.db.get_subdivision())


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
            self.str2date(self.widgets[0].get()),
            self.str2time(self.widgets[1].get()),
        ))


class Item5(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='5. Кем освидетельствован').pack(side=LEFT)
        self.widgets.append(
            OptionMenuSmart(self.frames[1], self.db.get_doctors()))

    def check(self, index):
        ItemBase.check(self, index)
        if not self.widgets[0].string_var.get():
            raise CheckException('Не указан врач\nв пункте 5.')

    def insert(self):
        doctor, *training = self.widgets[0].string_var.get().split(', ')
        self.db.insert(5, 'doctor', doctor)
        self.db.insert(5, 'training', ', '.join(training))

    def update_user(self):
        user = self.db.current_user
        if user == 'admin':
            self.widgets[0].string_var.set('')
            self.widgets[0]['state'] = 'normal'
        else:
            self.widgets[0].string_var.set(user)
            self.widgets[0]['state'] = 'disabled'


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


class SubItem13:
    def __init__(self, n, frames, devices):
        frames = frames[1:3] if n == 1 else frames[4:]
        title = 'Первое' if n == 1 else 'Второе'
        default = '%H:%M' if n == 1 else None
        self.n, self.widgets = n, []

        for i in 1, 3, 5:
            frames[0].columnconfigure(i, weight=1)
        Label(frames[0], text=f'13.1. {title} исследование').grid(
            row=0, column=0)

        frame = Frame(frames[0])
        frame.grid(row=0, column=2)
        Label(frame, text='Дата').pack(side=LEFT)
        self.widgets.append(EntryDate(frame, '%d.%m.%Y'))

        frame = Frame(frames[0])
        frame.grid(row=0, column=4)
        Label(frame, text='Время').pack(side=LEFT)
        self.widgets.append(EntryTime(frame, default))

        frame = Frame(frames[0])
        frame.grid(row=0, column=6)
        Label(frame, text='Результат').pack(side=LEFT)
        self.widgets.append(EntryResult(frame))
        Label(frame, text='мг/л').pack(side=LEFT)

        Label(frames[1], text='техническое средство').pack(side=LEFT)
        self.widgets.append(OptionMenuSmart(frames[1], devices))

    def check_result_basis(self):
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


class Item13(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=6)
        line = '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого'
        Label(self.frames[0], text=line).pack(side=LEFT)

        devices = self.db.get_devices()
        self.sub_item_1 = SubItem13(1, self.frames, devices)
        self.sub_item_2 = SubItem13(2, self.frames, devices)
        self.widgets.extend(self.sub_item_1.widgets + self.sub_item_2.widgets)

        self.forgery = 'фальсификация выдоха'
        checkbutton = CheckbuttonSmart(self.frames[3], text=self.forgery)
        checkbutton.pack(side=RIGHT)
        self.widgets.append(checkbutton)

    def check(self, index):
        ItemBase.check(self, index)
        # self.check_interval()
        self.check_result_basis()

    def check_interval(self):  # TODO move to db.check, (!) date was added
        time_1, time_2 = self.widgets[0].get(), self.widgets[4].get()
        if not (time_1 and time_2):
            return
        seconds_1 = mktime(strptime(time_1, '%H:%M'))
        seconds_2 = mktime(strptime(time_2, '%H:%M'))
        delta = seconds_2 - seconds_1
        cond_1 = delta < 15*60 or delta > 20*60
        cond_2 = delta + 24*3600 < 15*60 or delta + 24*3600 > 20*60
        if cond_1 and cond_2:
            raise CheckException('Интервал в пункте 13\nне равен 15-20 мин.')

    def check_result_basis(self):
        self.sub_item_1.check_result_basis()
        self.sub_item_2.check_result_basis()

    def insert(self):
        self.sub_item_1.insert(self.db)
        self.sub_item_2.insert(self.db)
        if self.widgets[8].int_var.get():
            self.db.insert(13, 'result_1', self.forgery)


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
        button_1 = CheckbuttonSmart(frame, text=self.refusal)
        button_2 = CheckbuttonSmart(frame, text=self.forgery)
        button_1.bind(
            '<Button-1>', lambda _: self.uncheck_extra(button_1, button_2))
        button_2.bind(
            '<Button-1>', lambda _: self.uncheck_extra(button_2, button_1))
        button_1.grid(row=0, sticky=W)
        button_2.grid(row=1)
        self.widgets.append(button_1)
        self.widgets.append(button_2)

        Label(self.frames[2], text='метод исследования').pack(side=LEFT)
        self.widgets.append(
            OptionMenuSmart(self.frames[2], self.db.get_methods()))

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

        self.frames[4].columnconfigure(0, weight=1)
        self.frames[4].columnconfigure(2, weight=1)
        self.frames[4].columnconfigure(4, weight=1)
        self.chemicals = self.db.get_chemicals()
        for i, chemical in enumerate(self.chemicals):
            row, column = int(i / 2), (i % 2) * 2 + 1
            frame = Frame(self.frames[4])
            frame.grid(row=row, column=column, sticky=W + E)
            Label(frame, text=chemical).pack(side=LEFT)
            entry = EntryDisabled(frame, width=4)
            LabelReplaceSmart(frame, text='«+»', bind=(entry, ''))
            LabelReplaceSmart(frame, text='«-»', bind=(entry, ''))
            entry.pack(side=RIGHT)
            self.widgets.append(entry)

    def check(self, index):
        ItemBase.check(self, index)
        if self.get_result() and not self.widgets[0].get():
            raise CheckException('Не указано время\nв пункте 14.')
        if self.get_result() and not self.widgets[4].string_var.get():
            raise CheckException('Не указан метод\nв пункте 14.')
        if self.get_result() and not self.widgets[6].get():
            raise CheckException('Не указан номер справки\nв пункте 14.')
        if self.widgets[6].get() and not self.widgets[5].get():
            raise CheckException('Не указан год\nв пункте 14.')

    def get_result(self):
        result = ''
        for i, chemical in enumerate(self.chemicals):
            temp = self.widgets[7 + i].get()
            if temp:
                result += chemical + ' ' + temp + ', '
        return result

    def insert(self):
        time, number = self.widgets[0].get(), self.widgets[6].get()
        self.db.insert(14, 'time', self.str2time(time))
        self.db.insert(14, 'material', self.widgets[1].get() if time else '')
        self.db.insert(
            14, 'laboratory', self.db.get_laboratory_name() if time else '')
        self.db.insert(14, 'method', self.widgets[4].string_var.get())
        self.db.insert(
            14, 'number',
            number + '/' + self.widgets[5].get() if number else '',
        )
        self.db.insert(14, 'result', self.get_result())

        line = self.refusal if self.widgets[2].int_var.get() else ''
        if self.widgets[3].int_var.get():
            line = self.forgery
        if line:
            self.db.insert(14, 'result', line)

    @staticmethod
    def uncheck_extra(button_1, button_2):
        if button_1.int_var.get():
            return
        if button_2.int_var.get():
            button_2.int_var.set(0)


class Item15(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='15. Другие данные').pack(side=LEFT)
        entry = EntryBase(self.frames[1], default='нет')
        entry.pack(fill=X)
        self.widgets.append(entry)

    def insert(self):
        self.db.insert(15, 'other', self.widgets[0].get())


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
            self.str2date(self.widgets[0].get()),
            self.str2time(self.widgets[1].get()),
        ))


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
        self.db.insert(17, 'date', self.str2date(self.widgets[1].get()))

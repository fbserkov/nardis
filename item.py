from tkinter import E, Frame, Label, LEFT, RIGHT, W, X
from widget import (
    CheckbuttonSmart, EntryBase, EntryDate, EntryDisabled, EntryResult,
    EntryTime, EntryTimer, EntryYear, LabelAdd, LabelAddSmart, LabelReplace,
    LabelReplaceSmart, LabelReplaceSmartDate, OptionMenuSmart,
)


def create_item(master, num, data=None):
    class_ = globals()[f'Item{num}']
    return class_(master, data) if data else class_(master)


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

    @staticmethod
    def dump():  # TODO delete
        return 'dump'

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

    frame = None


class Item0(ItemBase):
    def __init__(self, master, data):
        ItemBase.__init__(self, master)
        self.data = data
        self.frame.grid(row=0, column=0)

        Label(self.frame, text='Акт №').pack()
        entry = EntryDisabled(self.frame, width=4)
        entry.pack(side=LEFT)
        self.widgets.append(entry)

        Label(self.frame, text='/').pack(side=LEFT)
        entry = EntryYear(self.frame, '%y')
        entry.pack(side=LEFT)
        self.widgets.append(entry)

    def dump(self):
        return (
            self.data.settings['Организация'],
            self.widgets[0].get() + '/' + self.widgets[1].get(),
        )

    def update_index(self):
        self.widgets[0].config(state='normal')
        self.widgets[0].insert(0, self.data.get_index())
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

    def dump(self):
        return (
            self.widgets[0].get(), self.widgets[1].get(),
            self.widgets[2].get(), self.widgets[3].get(),
        )


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

    def dump(self):
        return self.widgets[0].get(), self.widgets[1].get()


class Item3(ItemBase):
    def __init__(self, master, data):
        ItemBase.__init__(self, master)
        self.data = data

    def dump(self):
        return self.data.settings['Подразделение']


class Item4(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=2)
        Label(self.frame, text='4. Начало освидетельствования').pack()
        Label(self.frame, text='Дата').pack(side=LEFT)
        self.widgets.append(EntryDate(self.frame, '%d.%m.%Y'))
        Label(self.frame, text='Время').pack(side=LEFT)
        self.widgets.append(EntryTime(self.frame, '%H:%M'))

    def dump(self):
        return self.widgets[0].get(), self.widgets[1].get()


class Item5(ItemBase):
    def __init__(self, master, data):
        ItemBase.__init__(self, master, frames_number=2)
        self.data = data
        Label(self.frames[0], text='5. Кем освидетельствован').pack(side=LEFT)
        self.widgets.append(
            OptionMenuSmart(self.frames[1], self.data.get_doctors()))

    def update_user(self):
        user = self.data.current_user
        if user == 'admin':
            self.widgets[0].string_var.set('')
            self.widgets[0]['state'] = 'normal'
        else:
            self.widgets[0].string_var.set(user)
            self.widgets[0]['state'] = 'disabled'

    def dump(self):
        line = self.widgets[0].string_var.get()
        if not line:
            return '', ''
        names, *tail = line.split(', ')
        return names, ', '.join(tail)


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

    def dump(self):
        return self.widgets[0].get()


class Item7(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        line = '7. Жалобы освидетельствуемого на своё состояние'
        Label(self.frames[0], text=line).pack(side=LEFT)
        entry = EntryBase(self.frames[1], default='не предъявляет')
        entry.pack(fill=X)
        self.widgets.append(entry)

    def dump(self):
        return self.widgets[0].get()


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

    def dump(self):
        temp = self.widgets[3].get()
        return (
            self.widgets[0].get(), self.widgets[1].get(),
            self.widgets[2].get(), temp + ' сек.' if temp else '',
        )


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

    def dump(self):
        return (
            self.widgets[0].get(), self.widgets[1].get(),
            self.widgets[2].get(), self.widgets[3].get(),
        )


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

    def dump(self):
        temp = self.widgets[4].get()
        return (
            self.widgets[0].get(), self.widgets[1].get(),
            self.widgets[2].get(), self.widgets[3].get(),
            temp + ' сек.' if temp else '',
        )


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

    def dump(self):
        return self.widgets[0].get()


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

    def dump(self):
        return self.widgets[0].get()


class Item13(ItemBase):
    def __init__(self, master, data):
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
        self.widgets.append(EntryTime(frame, '%H:%M'))
        frame = Frame(self.frames[1])
        frame.grid(row=0, column=4)
        Label(frame, text='Результат').pack(side=LEFT)
        self.widgets.append(EntryResult(frame))
        Label(frame, text='мг/л').pack(side=LEFT)
        Label(self.frames[2], text='техническое средство').pack(side=LEFT)
        technical_means = data.get_technical_means()
        self.widgets.append(OptionMenuSmart(self.frames[2], technical_means))
        self.line = 'фальсификация выдоха'
        checkbutton = CheckbuttonSmart(self.frames[3], text=self.line)
        checkbutton.pack(side=RIGHT)
        self.widgets.append(checkbutton)

        Label(self.frames[4], text='13.2. Второе исследование').grid(
            row=0, column=0)
        frame = Frame(self.frames[4])
        frame.grid(row=0, column=2)
        Label(frame, text='Время').pack(side=LEFT)
        self.widgets.append(EntryTime(frame))
        frame = Frame(self.frames[4])
        frame.grid(row=0, column=4)
        Label(frame, text='Результат').pack(side=LEFT)
        self.widgets.append(EntryResult(frame))
        Label(frame, text='мг/л').pack(side=LEFT)
        Label(self.frames[5], text='техническое средство').pack(side=LEFT)
        self.widgets.append(
            OptionMenuSmart(self.frames[5], technical_means))

    def dump(self):
        if self.widgets[3].int_var.get():
            return self.line, * 5 * ('',)
        temp_1 = self.widgets[1].get()
        temp_5 = self.widgets[5].get()
        return (
            self.widgets[0].get(), temp_1 + ' мг/л' if temp_1 else '',
            self.widgets[2].string_var.get(), self.widgets[4].get(),
            temp_5 + ' мг/л' if temp_5 else '',
            self.widgets[6].string_var.get(),
        )


class Item14(ItemBase):
    def __init__(self, master, data):
        ItemBase.__init__(self, master, frames_number=5)
        self.data = data
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
        self.line_1 = 'отказ от сдачи пробы биологического объекта (мочи)'
        checkbutton = CheckbuttonSmart(frame, text=self.line_1)
        checkbutton.grid(row=0, sticky=W)
        self.widgets.append(checkbutton)
        self.line_2 = 'фальсификация пробы биологического объекта (мочи)'
        checkbutton = CheckbuttonSmart(frame, text=self.line_2)
        checkbutton.grid(row=1)
        self.widgets.append(checkbutton)

        Label(self.frames[2], text='метод исследования').pack(side=LEFT)
        self.widgets.append(
            OptionMenuSmart(self.frames[2], self.data.get_methods()))

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
        self.chemicals = self.data.get_chemicals()
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

    def dump(self):
        line = ''
        if self.widgets[2].int_var.get():
            line = self.line_1
        if self.widgets[3].int_var.get():
            line = self.line_2
        if line:
            return line, * 4 * ('',)
        temp_0 = self.widgets[0].get()
        temp_6 = self.widgets[6].get()
        return (
            temp_0 + ' (' + self.widgets[1].get() + ')' if temp_0 else '',
            self.data.settings['Лаборатория'] if temp_0 else '',
            self.widgets[4].string_var.get(),
            temp_6 + ('/' + self.widgets[5].get() if temp_6 else ''),
            self.get_result(),
        )

    def get_result(self):
        result = ''
        for i, chemical in enumerate(self.chemicals):
            temp = self.widgets[7 + i].get()
            if temp:
                result += chemical + ' ' + temp + ', '
        return result


class Item15(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master, frames_number=2)
        Label(self.frames[0], text='15. Другие данные').pack(side=LEFT)
        entry = EntryBase(self.frames[1], default='нет')
        entry.pack(fill=X)
        self.widgets.append(entry)


class Item16(ItemBase):
    def __init__(self, master):
        ItemBase.__init__(self, master)
        self.frame.grid(row=0, column=4)
        Label(self.frame, text='16. Окончание освидетельствования').pack()
        Label(self.frame, text='Дата').pack(side=LEFT)
        self.widgets.append(EntryDate(self.frame, '%d.%m.%Y'))
        Label(self.frame, text='Время').pack(side=LEFT)
        self.widgets.append(EntryTime(self.frame, '%H:%M'))


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

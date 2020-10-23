from tkinter import Frame, Label, LabelFrame, LEFT, X

from labelframe import get_frames
from widget.entry import EntryBase, EntryDisabled
from widget.label import LabelAddSmart, LabelReplace


class CommonFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(
            self, font='-size 10 -weight bold', text='Общие данные')
        self.paragraph_6()
        self.paragraph_7()
        self.paragraph_8()

    def init(self):
        pass

    def paragraph_6(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 2)

        Label(frames[0], text='6. Внешний вид освидетельствуемого').pack(
            side=LEFT)
        entry = EntryBase(frames[1], width=69)
        entry.pack(fill=X)
        entry.insert(
            0, 'внешний вид и кожные покровы без особенностей, ' +
            'видимых повреждений нет',
        )

    def paragraph_7(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 2)

        line = '7. Жалобы освидетельствуемого на своё состояние'
        Label(frames[0], text=line).pack(side=LEFT)
        entry = EntryBase(frames[1])
        entry.pack(fill=X)
        entry.insert(0, 'не предъявляет')

    def paragraph_8(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 8)
        line = '8. Изменения психической деятельности освидетельствуемого'
        Label(frames[0], text=line).pack(side=LEFT)

        Label(frames[1], text='состояние сознания').pack(side=LEFT)
        entry = EntryBase(frames[1])
        entry.pack(side=LEFT, expand=True, fill=X)
        for text in 'ясное', 'оглушение', 'сопор', 'кома':
            LabelReplace(frames[1], text, bind=entry, place=LEFT)

        default = 'без особенностей'
        entry = EntryDisabled(frames[4], default=default)
        entry.pack(fill=X)
        Label(frames[2], text='поведение').pack(side=LEFT)
        for text in (
                'эйфоричен', 'агрессивен', 'возбуждён',
                'раздражён', 'замкнут', 'напряжён'
        ):
            LabelAddSmart(frames[2], text, bind=(entry, default))
        for text in (
                'заторможен', 'сонлив', 'настроение '
                'неустойчиво', 'суетлив', 'болтлив',
        ):
            LabelAddSmart(frames[3], text, bind=(entry, default))

        line = 'ориентировка в месте, времени, ситуации'
        Label(frames[5], text=line).pack(side=LEFT)
        entry = EntryBase(frames[6])
        entry.pack(side=LEFT, expand=True, fill=X)
        for text in 'ориентирован', 'ориентация снижена', 'дезориентирован':
            LabelReplace(frames[6], text, bind=entry, place=LEFT)

        Label(frames[7], text='результат пробы Шульте').pack(side=LEFT)
        EntryBase(frames[7], width=2).pack(side=LEFT)
        Label(frames[7], text='сек.').pack(side=LEFT)

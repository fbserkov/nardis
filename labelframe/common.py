from tkinter import Entry, Frame, Label, LabelFrame, LEFT, X
from widget import get_frames, SmartLabel


class CommonFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text='Общие данные')
        self.paragraph_6()
        self.paragraph_7()
        self.paragraph_8()

    def paragraph_6(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 2)

        Label(frames[0], text='6. Внешний вид освидетельствуемого').pack(
            side=LEFT)
        entry = Entry(frames[1], width=69, font='-size 10', fg='#800000')
        entry.pack(fill=X)
        line = (
            'внешний вид и кожные покровы без особенностей, ' +
            'видимых повреждений нет'
        )
        entry.insert(0, line)

    def paragraph_7(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 2)

        line = '7. Жалобы освидетельствуемого на своё состояние'
        Label(frames[0], text=line).pack(side=LEFT)
        entry = Entry(frames[1], font='-size 10', fg='#800000')
        entry.pack(fill=X)
        entry.insert(0, 'не предъявляет')

    def paragraph_8(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 8)
        line = '8. Изменения психической деятельности освидетельствуемого'
        Label(frames[0], text=line).pack(side=LEFT)

        Label(frames[1], text='состояние сознания').pack(side=LEFT)
        entry = Entry(frames[1], font='-size 10', fg='#800000')
        entry.pack(side=LEFT, expand=True, fill=X)
        SmartLabel(
            frames[1], text='ясное', place=LEFT, bind=('replace', entry))
        SmartLabel(
            frames[1], text='оглушение', place=LEFT, bind=('replace', entry))
        SmartLabel(
            frames[1], text='сопор', place=LEFT, bind=('replace', entry))
        SmartLabel(frames[1], text='кома', place=LEFT, bind=('replace', entry))

        default = 'без особенностей'
        entry = Entry(frames[4], font='-size 10', fg='#800000')
        entry.pack(fill=X)
        entry.insert(0, default)
        entry.config(state='disabled', disabledforeground='#800000')
        Label(frames[2], text='поведение').pack(side=LEFT)
        for text in (
                'эйфоричен', 'агрессивен', 'возбуждён',
                'раздражён', 'замкнут', 'напряжён'
        ):
            SmartLabel(frames[2], text,  bind=('add_smart', entry, default))
        for text in (
                'заторможен', 'сонлив', 'настроение '
                'неустойчиво', 'суетлив', 'болтлив',
        ):
            SmartLabel(frames[3], text, bind=('add_smart', entry, default))

        line = 'ориентировка в месте, времени, ситуации'
        Label(frames[5], text=line).pack(side=LEFT)
        entry = Entry(frames[6], font='-size 10', fg='#800000')
        entry.pack(side=LEFT, expand=True, fill=X)
        SmartLabel(
            frames[6], text='ориентирован',
            place=LEFT, bind=('replace', entry),
        )
        SmartLabel(
            frames[6], text='ориентация снижена',
            place=LEFT, bind=('replace', entry),
        )
        SmartLabel(
            frames[6], text='дезориентирован',
            place=LEFT, bind=('replace', entry),
        )

        Label(frames[7], text='результат пробы Шульте').pack(side=LEFT)
        Entry(frames[7], width=2, font='-size 10', fg='#800000').pack(
            side=LEFT)
        Label(frames[7], text='сек.').pack(side=LEFT)

from tkinter import Entry, Frame, Label, LabelFrame, LEFT, X
from widget.widget import get_frames, SmartLabel


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
        entry_10 = Entry(frames[1], width=69, font='-size 10', fg='#800000')
        entry_10.pack(fill=X)
        line = (
            'внешний вид и кожные покровы без особенностей, ' +
            'видимых повреждений нет'
        )
        entry_10.insert(0, line)

    def paragraph_7(self):
        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        frames = get_frames(frame, 2)

        line = '7. Жалобы освидетельствуемого на своё состояние'
        Label(frames[0], text=line).pack(side=LEFT)
        entry_10 = Entry(frames[1], font='-size 10', fg='#800000')
        entry_10.pack(fill=X)
        entry_10.insert(0, 'не предъявляет')

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

        Label(frames[2], text='поведение').pack(side=LEFT)
        SmartLabel(frames[2], text='эйфоричен')
        SmartLabel(frames[2], text='агрессивен')
        SmartLabel(frames[2], text='возбуждён')
        SmartLabel(frames[2], text='раздражён')
        SmartLabel(frames[2], text='замкнут')
        SmartLabel(frames[2], text='напряжён')
        SmartLabel(frames[3], text='заторможен')
        SmartLabel(frames[3], text='сонлив')
        SmartLabel(frames[3], text='настроение неустойчиво')
        SmartLabel(frames[3], text='суетлив')
        SmartLabel(frames[3], text='болтлив')
        entry_40 = Entry(frames[4], font='-size 10', fg='#800000')
        entry_40.pack(fill=X)
        entry_40.insert(0, 'без особенностей')
        entry_40.config(state='disabled', disabledforeground='#800000')

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

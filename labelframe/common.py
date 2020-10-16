from tkinter import Entry, Frame, Label, LabelFrame, LEFT, X
from widget.widget import SmartLabel


class CommonFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text='Общие данные')

        # пункт 6
        frame_a = Frame(self, bd=4)
        frame_a.pack(fill=X)

        frame_a0 = Frame(frame_a)
        frame_a0.pack(fill=X)
        label_a00 = Label(frame_a0, text='6. Внешний вид освидетельствуемого')
        label_a00.pack(side=LEFT)

        frame_a1 = Frame(frame_a)
        frame_a1.pack(fill=X)
        entry_a10 = Entry(frame_a1, width=69, font='-size 10', fg='#800000')
        entry_a10.pack(fill=X)
        line = ('внешний вид и кожные покровы без особенностей' +
                ', видимых повреждений нет')
        entry_a10.insert(0, line)

        # пункт 7
        frame_b = Frame(self, bd=4)
        frame_b.pack(fill=X)

        frame_b0 = Frame(frame_b)
        frame_b0.pack(fill=X)
        line = '7. Жалобы освидетельствуемого на своё состояние'
        label_b00 = Label(frame_b0, text=line)
        label_b00.pack(side=LEFT)

        frame_b1 = Frame(frame_b)
        frame_b1.pack(fill=X)
        entry_b10 = Entry(frame_b1, font='-size 10', fg='#800000')
        entry_b10.pack(fill=X)
        entry_b10.insert(0, 'не предъявляет')

        # пункт 8
        frame_c = Frame(self, bd=4)
        frame_c.pack(fill=X)

        frame_c0 = Frame(frame_c)
        frame_c0.pack(fill=X)
        line = '8. Изменения психической деятельности освидетельствуемого'
        label_c00 = Label(frame_c0, text=line)
        label_c00.pack(side=LEFT)

        frame_c1 = Frame(frame_c)
        frame_c1.pack(fill=X)
        label_c10 = Label(frame_c1, text='состояние сознания')
        label_c10.pack(side=LEFT)
        entry_c10 = Entry(frame_c1, font='-size 10', fg='#800000')
        entry_c10.pack(side=LEFT, expand=True, fill=X)
        SmartLabel(frame_c1, text='ясное', place=LEFT)
        SmartLabel(frame_c1, text='оглушение', place=LEFT)
        SmartLabel(frame_c1, text='сопор', place=LEFT)
        SmartLabel(frame_c1, text='кома', place=LEFT)

        frame_c2 = Frame(frame_c)
        frame_c2.pack(fill=X)
        label_c20 = Label(frame_c2, text='поведение')
        label_c20.pack(side=LEFT)
        SmartLabel(frame_c2, text='эйфоричен')
        SmartLabel(frame_c2, text='агрессивен')
        SmartLabel(frame_c2, text='возбуждён')
        SmartLabel(frame_c2, text='раздражён')
        SmartLabel(frame_c2, text='замкнут')
        SmartLabel(frame_c2, text='напряжён')

        frame_c3 = Frame(frame_c)
        frame_c3.pack(fill=X)
        SmartLabel(frame_c3, text='заторможен')
        SmartLabel(frame_c3, text='сонлив')
        SmartLabel(frame_c3, text='настроение неустойчиво')
        SmartLabel(frame_c3, text='суетлив')
        SmartLabel(frame_c3, text='болтлив')

        frame_c4 = Frame(frame_c)
        frame_c4.pack(fill=X)
        entry_c40 = Entry(frame_c4, font='-size 10', fg='#800000')
        entry_c40.pack(fill=X)
        entry_c40.insert(0, 'без особенностей')
        entry_c40.config(state='disabled', disabledforeground='#800000')

        frame_c5 = Frame(frame_c)
        frame_c5.pack(fill=X)
        line = 'ориентировка в месте, времени, ситуации'
        label_c50 = Label(frame_c5, text=line)
        label_c50.pack(side=LEFT)

        frame_c6 = Frame(frame_c)
        frame_c6.pack(fill=X)
        entry_c60 = Entry(frame_c6, font='-size 10', fg='#800000')
        entry_c60.pack(side=LEFT, expand=True, fill=X)
        SmartLabel(frame_c6, text='ориентирован', place=LEFT)
        SmartLabel(frame_c6, text='ориентация снижена', place=LEFT)
        SmartLabel(frame_c6, text='дезориентирован', place=LEFT)

        frame_c7 = Frame(frame_c)
        frame_c7.pack(fill=X)
        label_c70 = Label(frame_c7, text='результат пробы Шульте')
        label_c70.pack(side=LEFT)
        entry_c70 = Entry(frame_c7, width=2, font='-size 10', fg='#800000')
        entry_c70.pack(side=LEFT)
        label_c71 = Label(frame_c7, text='сек.')
        label_c71.pack(side=LEFT)

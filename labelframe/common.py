from tkinter import Entry, Frame, Label, LabelFrame, LEFT, RIGHT, X
from widget.smartlabel import SmartLabel


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
        entry_a10 = Entry(frame_a1, font='-size 10', fg='#800000')
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
        smart_label_c10 = SmartLabel(frame_c1, text='ясное')
        smart_label_c10.pack(side=LEFT)
        smart_label_c11 = SmartLabel(frame_c1, text='оглушение')
        smart_label_c11.pack(side=LEFT)
        smart_label_c12 = SmartLabel(frame_c1, text='сопор')
        smart_label_c12.pack(side=LEFT)
        smart_label_c13 = SmartLabel(frame_c1, text='кома')
        smart_label_c13.pack(side=LEFT)

        frame_c2 = Frame(frame_c)
        frame_c2.pack(fill=X)
        label_c20 = Label(frame_c2, text='поведение')
        label_c20.pack(side=LEFT)
        smart_label_c20 = SmartLabel(frame_c2, text='эйфоричен')
        smart_label_c20.pack(side=RIGHT)
        smart_label_c21 = SmartLabel(frame_c2, text='агрессивен')
        smart_label_c21.pack(side=RIGHT)
        smart_label_c22 = SmartLabel(frame_c2, text='возбуждён')
        smart_label_c22.pack(side=RIGHT)
        smart_label_c23 = SmartLabel(frame_c2, text='раздражён')
        smart_label_c23.pack(side=RIGHT)
        smart_label_c24 = SmartLabel(frame_c2, text='замкнут')
        smart_label_c24.pack(side=RIGHT)
        smart_label_c25 = SmartLabel(frame_c2, text='напряжён')
        smart_label_c25.pack(side=RIGHT)

        frame_c3 = Frame(frame_c)
        frame_c3.pack(fill=X)
        smart_label_c30 = SmartLabel(frame_c3, text='заторможен')
        smart_label_c30.pack(side=RIGHT)
        smart_label_c31 = SmartLabel(frame_c3, text='сонлив')
        smart_label_c31.pack(side=RIGHT)
        smart_label_c32 = SmartLabel(frame_c3, text='настроение неустойчиво')
        smart_label_c32.pack(side=RIGHT)
        smart_label_c33 = SmartLabel(frame_c3, text='суетлив')
        smart_label_c33.pack(side=RIGHT)
        smart_label_c34 = SmartLabel(frame_c3, text='болтлив')
        smart_label_c34.pack(side=RIGHT)

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
        smart_label_c60 = SmartLabel(frame_c6, text='ориентирован')
        smart_label_c60.pack(side=LEFT)
        smart_label_c61 = SmartLabel(frame_c6, text='ориентация снижена')
        smart_label_c61.pack(side=LEFT)
        smart_label_c62 = SmartLabel(frame_c6, text='дезориентирован')
        smart_label_c62.pack(side=LEFT)

        frame_c7 = Frame(frame_c)
        frame_c7.pack(fill=X)
        label_c70 = Label(frame_c7, text='результат пробы Шульте')
        label_c70.pack(side=LEFT)
        entry_c70 = Entry(frame_c7, width=2, font='-size 10', fg='#800000')
        entry_c70.pack(side=LEFT)
        label_c71 = Label(frame_c7, text='сек.')
        label_c71.pack(side=LEFT)

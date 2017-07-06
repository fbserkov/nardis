from tkinter import Frame, Label, LabelFrame, LEFT, X
# from widget.smartlabel import SmartLabel


class ExaminationFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text='Данные освидетельствования')

        # пункт 13
        frame_a = Frame(self, bd=4)
        frame_a.pack(fill=X)

        frame_a0 = Frame(frame_a)
        frame_a0.pack(fill=X)
        line = '13. Наличие алкоголя в выдыхаемом воздухе освидетельствуемого'
        label_a00 = Label(frame_a0, text=line)
        label_a00.pack(side=LEFT)

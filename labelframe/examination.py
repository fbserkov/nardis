from tkinter import Frame, LabelFrame, X
# from widget.smartlabel import SmartLabel


class ExaminationFrame(LabelFrame):
    def __init__(self):
        LabelFrame.__init__(self, text='Данные освидетельствования')

        # пункт 13
        frame_a = Frame(self, bd=4)
        frame_a.pack(fill=X)

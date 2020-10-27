from labelframe import (
    CommonPart, ExaminationPart, PassportPart, SurveyPart)
from tkinter import Button, Frame, LEFT, X
from window.window import WindowBase


class WindowMain(WindowBase):
    def __init__(self, database):
        WindowBase.__init__(self)
        self.root.title('Наркологическая экспертиза')
        self.centering(width=604, height=643)
        frame = Frame()
        frame.pack(fill=X)

        Button(frame, text='Вход').pack(side=LEFT, expand=True, fill=X)
        button = Button(frame, text='Новый')
        button.pack(side=LEFT, expand=True, fill=X)
        button.bind('<Button-1>', lambda e: self.init())

        frame = Frame()
        frame.pack(fill=X)
        self.buttons = (
            Button(frame, text='I'), Button(frame, text='II'),
            Button(frame, text='III'), Button(frame, text='IV')
        )
        for button in self.buttons:
            button.pack(side=LEFT, expand=True, fill=X)
            button.bind('<Button-1>', lambda e: self.show_label_frame(
                self.buttons.index(e.widget)))

        self.label_frames = (
            PassportPart(database), CommonPart(),
            SurveyPart(), ExaminationPart(database),
        )
        self.show_label_frame(0)
        self.root.mainloop()

    def init(self):
        for label_frame in self.label_frames:
            label_frame.init()

    def show_label_frame(self, index):
        for i in range(len(self.label_frames)):
            if i == index:
                self.buttons[i].config(font='-size 10 -weight bold')
                self.label_frames[i].pack(fill=X)
            else:
                self.buttons[i].config(font='-size 10')
                self.label_frames[i].forget()

from labelframe.common import CommonFrame
from labelframe.examination import ExaminationFrame
from labelframe.passport import PassportFrame
from labelframe.survey import SurveyFrame
from tkinter import Button, Frame, LEFT, X
from window.window import Window


class Main(Window):
    def __init__(self, database):
        Window.__init__(self)
        self.root.title('Наркологическая экспертиза')
        self.centering(width=604, height=612)
        frame = Frame()
        frame.pack(fill=X)

        button = Button(frame, text='Новый')
        button.pack(side=LEFT, expand=True, fill=X)
        button.bind('<Button-1>', lambda e: self.init())

        self.buttons = (
            Button(frame, text='I'), Button(frame, text='II'),
            Button(frame, text='III'), Button(frame, text='IV')
        )
        for button in self.buttons:
            button.pack(side=LEFT, expand=True, fill=X)
            button.bind('<Button-1>', lambda e: self.show_label_frame(
                self.buttons.index(e.widget)))

        self.label_frames = (
            PassportFrame(database), CommonFrame(),
            SurveyFrame(), ExaminationFrame(database),
        )
        self.show_label_frame(0)
        self.root.mainloop()

    def init(self):
        print('init')
        pass

    def show_label_frame(self, index):
        for i in range(len(self.label_frames)):
            if i == index:
                self.buttons[i].config(font='-size 10 -weight bold')
                self.label_frames[i].pack(fill=X)
            else:
                self.buttons[i].config(font='-size 10')
                self.label_frames[i].forget()

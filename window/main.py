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
        self.create(database)
        self.centering(width=604, height=612)   # height < 768
        self.root.mainloop()

    @staticmethod
    def create(database):
        label_frames = [PassportFrame(database),
                        CommonFrame(),
                        SurveyFrame(),
                        ExaminationFrame(database)]
        for frame in label_frames:
            frame.config(font='-weight bold -size 10')

        label_frame_buttons_frame = Frame()
        label_frame_buttons_frame.pack(fill=X)

        label_frame_buttons = [Button(label_frame_buttons_frame, text='I'),
                               Button(label_frame_buttons_frame, text='II'),
                               Button(label_frame_buttons_frame, text='III'),
                               Button(label_frame_buttons_frame, text='IV')]

        def show_label_frame(n):
            for i in range(len(label_frames)):
                if i == n:
                    label_frame_buttons[i].config(font='-weight bold -size 10')
                    label_frames[i].pack(fill=X)
                else:
                    label_frame_buttons[i].config(font='-size 10')
                    label_frames[i].forget()

        for button in label_frame_buttons:
            button.config(font='-size 10')
            button.pack(side=LEFT, expand=True, fill=X)
            button.bind('<Button-1>', lambda e: show_label_frame(
                label_frame_buttons.index(e.widget)))

        show_label_frame(0)

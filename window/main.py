from tkinter import LabelFrame
from window.window import Window


class Main(Window):
    def __init__(self):
        Window.__init__(self)
        self.root.title('Наркологическая экспертиза')
        self.centering()    # было 551x672 (высота < 768)
        self.create()
        self.root.mainloop()

    @staticmethod
    def create():
        label_frames = [LabelFrame(text='Паспортная часть'),
                        LabelFrame(text='Общие данные'),
                        LabelFrame(text='Объективный осмотр'),
                        LabelFrame(text='Данные освидетельствования')]
        for item in label_frames:
            item.config(font='-weight bold -size 10')

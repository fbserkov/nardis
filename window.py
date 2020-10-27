import sys

from tkinter import Button, Entry, Frame, LEFT, OptionMenu, StringVar, Tk, X
from tkinter.messagebox import showinfo

from labelframe import PassportPart, CommonPart, SurveyPart, ExaminationPart


class WindowBase:
    def __init__(self):
        self.root = Tk()
        if not sys.platform == 'linux':
            self.root.iconbitmap('nardis.ico')

    def centering(self, width=0, height=0):
        if not (width and height):
            self.root.update()
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            print('{}x{}'.format(width, height))
        if sys.platform == 'linux':
            frame, title = 0, 37  # Ubuntu
        else:
            frame, title = 3, 26  # Windows XP
        left = (self.root.winfo_screenwidth() - (width + 2 * frame)) / 2
        top = (self.root.winfo_screenheight() - (height + 2 * frame + title)) / 2
        self.root.geometry('%ix%i+%i+%i' % (width, height, left, top))
        self.root.resizable(False, False)

    def show_popup(self, title, message, alone=False):
        if alone:
            self.root.withdraw()
        showinfo(title, message)


class WindowAuth(WindowBase):
    def __init__(self, database):
        WindowBase.__init__(self)
        self.root.title('Введите пароль')

        years = database.get_years()
        sv = StringVar(self.root)
        sv.set(years[-1])
        om = OptionMenu(self.root, sv, *years)
        om.config(font='-size 10', fg='#800000')
        om.pack(fill=X)

        def cb():
            if database.authentication(e.get(), int(sv.get())):
                self.root.destroy()
                self.root.quit()
        e = Entry(self.root, font='-size 14', show='●')
        e.bind('<Key-Return>', lambda _: cb())
        e.pack()
        e.focus()

        Button(self.root, font='-size 10', text='OK', command=cb).pack(fill=X)
        self.centering(width=200, height=88)
        self.root.mainloop()


class WindowMain(WindowBase):
    def __init__(self, data):
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
            PassportPart(data), CommonPart(),
            SurveyPart(), ExaminationPart(data),
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

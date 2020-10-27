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
        top = (
            self.root.winfo_screenheight() - (height + 2 * frame + title)) / 2
        self.root.geometry('%ix%i+%i+%i' % (width, height, left, top))
        self.root.resizable(False, False)

    def show_popup(self, title, message, alone=False):
        if alone:
            self.root.withdraw()
        showinfo(title, message)


class WindowAuth(WindowBase):  # TODO modal
    def __init__(self, data):
        WindowBase.__init__(self)
        self.root.title('Введите пароль')

        years = data.get_years()
        sv = StringVar(self.root)
        sv.set(years[-1])
        om = OptionMenu(self.root, sv, *years)
        om.config(font='-size 10', fg='#800000')
        om.pack(fill=X)

        def cb():
            if data.authentication(e.get(), int(sv.get())):
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
        self.data, self.index = data, 0

        frame = Frame()
        frame.pack(fill=X)
        self.auth_button = Button(frame, text='Вход')
        self.auth_button.pack(side=LEFT, expand=True, fill=X)
        self.auth_button.bind('<Button-1>', lambda e: self.login())

        button = Button(frame, text='Новый', state='disabled')
        button.pack(side=LEFT, expand=True, fill=X)
        # button.bind('<Button-1>', lambda e: self.init())
        # button.unbind('<Button-1>')

        self.frame = Frame()
        self.buttons = (
            Button(self.frame, text='I'), Button(self.frame, text='II'),
            Button(self.frame, text='III'), Button(self.frame, text='IV')
        )
        for button in self.buttons:
            button.pack(side=LEFT, expand=True, fill=X)
            button.bind('<Button-1>', lambda e: self.show_label_frame(
                self.buttons.index(e.widget) + 1))

        self.label_frames = (
            PassportPart(self.data), CommonPart(),
            SurveyPart(), ExaminationPart(self.data),
        )
        self.root.mainloop()

    def init(self):
        for label_frame in self.label_frames:
            label_frame.init()

    def login(self):
        WindowAuth(self.data)
        # TODO if self.data.current_user:

        self.frame.pack(fill=X)
        self.show_label_frame(0)
        self.auth_button['text'] = 'Выход'
        self.auth_button.bind('<Button-1>', lambda e: self.logout())

    def logout(self):
        self.frame.forget()
        self.show_label_frame(0)
        self.auth_button['text'] = 'Вход'
        self.auth_button.bind('<Button-1>', lambda e: self.login())

    def show_label_frame(self, index):
        if self.index == index:
            return
        self.label_frames[self.index - 1].forget()
        self.buttons[self.index - 1].config(font='-size 10')
        if index:
            self.label_frames[index - 1].pack(fill=X)
            self.buttons[index - 1].config(font='-size 10 -weight bold')
        self.index = index

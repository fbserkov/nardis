import sys
from tkinter import Button, Entry, Frame, LEFT, Toplevel, X

from labelframe import PassportPart, CommonPart, SurveyPart, ExaminationPart
from template import create_pdf


class WindowAuth(Toplevel):
    def __init__(self, root, data):
        Toplevel.__init__(self)
        self.title('Введите пароль')
        self.data, self.status = data, False

        self.entry = Entry(self, font='-size 14', show='●')
        self.entry.bind('<Key-Return>', lambda _: self.auth())
        self.entry.pack()
        self.entry.focus()
        self.button = Button(
            self, font='-size 10', text='OK', command=self.auth)
        self.button.pack(fill=X)

        self.transient(root)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def auth(self):
        if self.data.check_password(self.entry.get()):
            self.status = True
            self.destroy()
        else:
            self.button['text'] = 'Неверный пароль'


class WindowMain:
    def __init__(self, root, data):
        self.root, self.data = root, data
        root.title('Наркологическая экспертиза')
        root.geometry(f'610x650')
        root.resizable(width=False, height=False)
        if not sys.platform == 'linux':
            root.iconbitmap('nardis.ico')
        self.index, self.auth_status = 0, False

        frame = Frame()
        frame.pack(fill=X)
        self.auth_button = Button(frame, text='Вход', command=self.auth)
        self.auth_button.pack(side=LEFT, expand=True, fill=X)
        self.new_button = Button(
            frame, text='Новый', command=self.init, state='disabled')
        self.new_button.pack(side=LEFT, expand=True, fill=X)
        self.pdf_button = Button(
            frame, text='Сохранить', command=self.pdf, state='disabled')
        self.pdf_button.pack(side=LEFT, expand=True, fill=X)

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
        root.mainloop()

    def auth(self):
        if self.auth_status:
            self.auth_status = False
            self.auth_button['text'] = 'Вход'
            self.new_button['state'] = 'disabled'
            self.pdf_button['state'] = 'disabled'
            self.frame.forget()
            self.show_label_frame(0)

        else:
            if not WindowAuth(self.root, self.data).status:
                return
            self.auth_status = True
            self.auth_button['text'] = 'Выход'
            self.new_button['state'] = 'normal'
            self.pdf_button['state'] = 'normal'
            self.frame.pack(fill=X)
            self.show_label_frame(1)
            self.init()

    def init(self):
        for label_frame in self.label_frames:
            label_frame.init()
        self.label_frames[0].update()

    @staticmethod
    def pdf():
        create_pdf('test.pdf')

    def show_label_frame(self, index):
        if self.index == index:
            return
        self.label_frames[self.index - 1].forget()
        self.buttons[self.index - 1].config(font='-size 10')
        if index:
            self.label_frames[index - 1].pack(fill=X)
            self.buttons[index - 1].config(font='-size 10 -weight bold')
        self.index = index

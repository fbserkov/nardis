import sys
import os

from tkinter import Button, Entry, Frame, LEFT, Tk, Toplevel, X
from tkinter.messagebox import showinfo

from database import Database
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
    def __init__(self):
        self.root = Tk()
        self.customize()

        self.file_exists_error = False
        self.lock()
        if self.file_exists_error:
            return

        self.file_not_found_error = False
        self.data = self.load_data()
        if self.file_not_found_error:
            return

        self.auth_button, self.auth_status = None, False
        self.new_button, self.pdf_button = None, None
        self.create_menu()

        self.frame, self.buttons = None, None
        self.label_frames, self.index = None, 0
        self.create_parts()

        self.root.mainloop()

    def __del__(self):
        self.unlock()

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

    def create_menu(self):
        frame = Frame()
        frame.pack(fill=X)
        self.auth_button = Button(frame, text='Вход', command=self.auth)
        self.auth_button.pack(side=LEFT, expand=True, fill=X)
        self.new_button = Button(
            frame, text='Новый', command=self.init, state='disabled')
        self.new_button.pack(side=LEFT, expand=True, fill=X)
        self.pdf_button = Button(
            frame, text='Сохранить', command=self.save, state='disabled')
        self.pdf_button.pack(side=LEFT, expand=True, fill=X)

    def create_parts(self):
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

    def customize(self):
        self.root.title('Наркологическая экспертиза')
        self.root.geometry('610x650')
        self.root.resizable(width=False, height=False)
        if not sys.platform == 'linux':
            self.root.iconbitmap('nardis.ico')

    def init(self):
        for label_frame in self.label_frames:
            label_frame.init()
        self.label_frames[0].update()

    def save(self):
        report = self.data.get_report()
        for label_frame in self.label_frames:
            for item in label_frame.items:
                report[item] = label_frame.items[item].dump()
        self.data.save()
        create_pdf('test.pdf')

    def load_data(self):
        try:
            return Database('nardis.db')
        except FileNotFoundError:
            self.show_popup(
                title='Сообщение', message='База данных не найдена.')
            self.file_not_found_error = True

    def lock(self):
        try:
            open('file.lock', 'x').close()
        except FileExistsError:
            self.show_popup(
                title='Сообщение', message='Приложение уже запущено.')
            self.file_exists_error = True

    def show_label_frame(self, index):
        if self.index == index:
            return
        self.label_frames[self.index - 1].forget()
        self.buttons[self.index - 1].config(font='-size 10')
        if index:
            self.label_frames[index - 1].pack(fill=X)
            self.buttons[index - 1].config(font='-size 10 -weight bold')
        self.index = index

    def show_popup(self, title, message):
        self.root.withdraw()
        showinfo(title, message)

    def unlock(self):
        if self.file_exists_error:
            return
        os.remove('file.lock')


if __name__ == '__main__':
    WindowMain()

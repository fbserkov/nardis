import os
import sys
from time import mktime, strptime

from tkinter import Button, Entry, Frame, LEFT, Tk, Toplevel, X
from tkinter.messagebox import showinfo

from database import Database
from item import ItemBase, CheckException
from part import PassportPart, CommonPart, SurveyPart, ExaminationPart
from template import create_pdf


class FramePart(Frame):
    def __init__(self, data):
        Frame.__init__(self)
        frame = Frame(self)
        frame.pack(fill=X)

        self.buttons = (
            Button(frame, text='I'), Button(frame, text='II'),
            Button(frame, text='III'), Button(frame, text='IV'),
        )
        for i, obj in enumerate(self.buttons):
            obj.pack(side=LEFT, expand=True, fill=X)
            obj['command'] = lambda j=i: self.show_part(j + 1)

        ItemBase.db = data
        self.part_frames = (
            PassportPart(self), CommonPart(self),
            SurveyPart(self), ExaminationPart(self),
        )
        self.data, self.index = data, 0

    def check(self):
        for part_frame in self.part_frames:
            part_frame.check()
        self.check_chronology()

    def check_chronology(self):
        seconds = [
            mktime(strptime(time, '%H:%M')) if time else None for time in (
                self.part_frames[0].items[4].widgets[1].get(),
                self.part_frames[3].items[13].widgets[0].get(),
                self.part_frames[3].items[13].widgets[4].get(),
                self.part_frames[0].items[16].widgets[1].get(),
            )
        ]
        if seconds[0] and seconds[1]:
            if seconds[1] < seconds[0] < seconds[1] + 23*3600:
                raise CheckException(
                    'Несоответствие времени\nв пунктах 4 и 13.')
        if seconds[2] and seconds[3]:
            if seconds[3] < seconds[2] < seconds[3] + 23*3600:
                raise CheckException(
                    'Несоответствие времени\nв пунктах 16 и 13.')

    def dump(self):
        report = self.data.get_report()
        for part_frame in self.part_frames:
            for i in part_frame.items:
                report[i] = part_frame.items[i].dump()

    def init(self):
        for part_frame in self.part_frames:
            part_frame.init()
        self.part_frames[0].update()

    def insert(self):
        for part_frame in self.part_frames:
            for item in part_frame.items.values():
                item.insert()

    def save(self):
        try:
            self.check()
            self.dump()
            self.insert()
            self.data.save()
            create_pdf('test.pdf', self.data)
        except CheckException as exc:
            showinfo('Проверка', exc.text)

    def show_part(self, index):
        if self.index == index:
            return
        self.part_frames[self.index - 1].forget()
        self.buttons[self.index - 1].config(font='-size 10')
        if index:
            self.part_frames[index - 1].pack(fill=X)
            self.buttons[index - 1].config(font='-size 10 -weight bold')
        self.index = index


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

        self.frame_part = FramePart(self.data)
        self.auth_button, self.auth_status = None, False
        self.new_button, self.pdf_button = None, None
        self.create_menu()
        self.root.mainloop()

    def auth(self):
        if self.auth_status:
            self.auth_status = False
            self.auth_button['text'] = 'Вход'
            self.new_button['state'] = 'disabled'
            self.pdf_button['state'] = 'disabled'
            self.frame_part.forget()
        else:
            if not WindowAuth(self.root, self.data).status:
                return
            self.auth_status = True
            self.auth_button['text'] = 'Выход'
            self.new_button['state'] = 'normal'
            self.pdf_button['state'] = 'normal'
            self.frame_part.pack(fill=X)
            self.frame_part.show_part(1)
            self.frame_part.init()

    def create_menu(self):
        frame = Frame()
        frame.pack(fill=X)
        self.auth_button = Button(frame, text='Вход', command=self.auth)
        self.auth_button.pack(side=LEFT, expand=True, fill=X)
        self.new_button = Button(
            frame, text='Новый',
            command=self.frame_part.init, state='disabled',
        )
        self.new_button.pack(side=LEFT, expand=True, fill=X)
        self.pdf_button = Button(
            frame, text='Сохранить',
            command=self.frame_part.save, state='disabled',
        )
        self.pdf_button.pack(side=LEFT, expand=True, fill=X)

    def customize(self):
        self.root.title('Наркологическая экспертиза')
        self.root.geometry('610x650')
        self.root.resizable(width=False, height=False)
        if not sys.platform == 'linux':
            self.root.iconbitmap('nardis.ico')

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

    def show_popup(self, title, message):
        self.root.withdraw()
        showinfo(title, message)

    def unlock(self):
        if self.file_exists_error:
            return
        os.remove('file.lock')


if __name__ == '__main__':
    WindowMain().unlock()

import os
import sys

from tkinter import Button, Entry, Frame, LEFT, Listbox, Tk, Toplevel, X
from tkinter.messagebox import showinfo

from database import Database
from item import ItemBase, CheckException
from part import PassportPart, CommonPart, SurveyPart, ExaminationPart
from template import create_pdf


class App:
    def __init__(self):
        self.root = Tk()
        self.customize()

        self.file_exists_error = False
        self.lock()
        if self.file_exists_error:
            return

        self.file_not_found_error = False
        db = self.load_db()
        if self.file_not_found_error:
            return

        frame_part = FramePart(db)
        list_acts = ListActs()
        Menu(frame_part, list_acts)
        self.root.mainloop()

    def customize(self):
        self.root.title('Наркологическая экспертиза')
        self.root.geometry('610x650')
        self.root.resizable(width=False, height=False)
        if not sys.platform == 'linux':
            self.root.iconbitmap('nardis.ico')

    def load_db(self):
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


class FramePart(Frame):
    def __init__(self, db):
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

        ItemBase.db = db
        self.part_frames = (
            PassportPart(self), CommonPart(self),
            SurveyPart(self), ExaminationPart(self),
        )
        self.db, self.index = db, 0

    def check(self):
        for part_frame in self.part_frames:
            part_frame.check()

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
            self.insert()
            self.db.check()
            self.db.save()
            create_pdf('test.pdf', self.db)
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


class ListActs(Listbox):
    def __init__(self):
        Listbox.__init__(self, height=34)
        # self.status = False


class Menu(Frame):
    def __init__(self, frame_part, list_acts):
        Frame.__init__(self)
        self.pack(fill=X)
        self.frame_part, self.list_acts = frame_part, list_acts
        self.auth_status, self.list_status = False, False

        self.auth_button = Button(self, text='Вход', command=self.auth)
        self.auth_button.pack(side=LEFT, expand=True, fill=X)
        self.new_button = Button(
            self, text='Новый', command=frame_part.init, state='disabled')
        self.new_button.pack(side=LEFT, expand=True, fill=X)
        self.pdf_button = Button(
            self, text='Сохранить', command=frame_part.save, state='disabled')
        self.pdf_button.pack(side=LEFT, expand=True, fill=X)
        self.list_button = Button(
            self, text='Список', command=self.show_list, state='disabled')
        self.list_button.pack(side=LEFT, expand=True, fill=X)

    def auth(self):
        if self.auth_status:
            self.auth_status = False
            self.auth_button['text'] = 'Вход'
            self.new_button['state'] = 'disabled'
            self.pdf_button['state'] = 'disabled'
            self.list_button['state'] = 'disabled'
            self.frame_part.forget()
            self.list_acts.forget()
            self.list_status = False
        else:
            if not WindowAuth(self.frame_part.db).status:
                return
            self.auth_status = True
            self.auth_button['text'] = 'Выход'
            self.new_button['state'] = 'normal'
            self.pdf_button['state'] = 'normal'
            self.list_button['state'] = 'normal'
            self.frame_part.pack(fill=X)
            self.frame_part.show_part(1)
            self.frame_part.init()

    def show_list(self):
        if self.list_status:
            self.list_status = False
            self.new_button['state'] = 'normal'
            self.pdf_button['state'] = 'normal'
            self.list_acts.forget()
            self.frame_part.pack(fill=X)
        else:
            self.list_status = True
            self.new_button['state'] = 'disabled'
            self.pdf_button['state'] = 'disabled'
            self.frame_part.forget()
            self.list_acts.pack(fill=X)


class WindowAuth(Toplevel):
    def __init__(self, db):
        Toplevel.__init__(self)
        self.title('Введите пароль')
        self.db, self.status = db, False

        self.entry = Entry(self, font='-size 14', show='●')
        self.entry.bind('<Key-Return>', lambda _: self.auth())
        self.entry.pack()
        self.entry.focus()
        self.button = Button(
            self, font='-size 10', text='OK', command=self.auth)
        self.button.pack(fill=X)

        self.transient(self.master)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def auth(self):
        if self.db.check_password(self.entry.get()):
            self.status = True
            self.destroy()
        else:
            self.button['text'] = 'Неверный пароль'


if __name__ == '__main__':
    App().unlock()

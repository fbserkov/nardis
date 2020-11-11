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
        self.list_status = False

        self.file_exists_error = False
        self.lock()
        if self.file_exists_error:
            return

        self.file_not_found_error = False
        db = self.load_db()
        if self.file_not_found_error:
            return

        self.parts = FrameParts(db)
        self.acts = ListboxActs()
        self.menu = FrameMenu(self)
        self.root.mainloop()

    def cb_auth(self):
        if self.parts.is_visible:
            self.parts.hide()
            self.menu.auth_button['text'] = 'Вход'
            self.menu.new_button['state'] = 'disabled'
            self.menu.pdf_button['state'] = 'disabled'
            self.menu.list_button['state'] = 'disabled'
            self.acts.forget()
            self.menu.list_status = False
        else:
            if not TopLevelAuth(self.parts.db).status:
                return
            self.parts.show()
            self.menu.auth_button['text'] = 'Выход'
            self.menu.new_button['state'] = 'normal'
            self.menu.pdf_button['state'] = 'normal'
            self.menu.list_button['state'] = 'normal'

    def cb_list(self):
        if self.list_status:
            self.list_status = False
            self.menu.new_button['state'] = 'normal'
            self.menu.pdf_button['state'] = 'normal'
            self.acts.forget()
            self.parts.pack(fill=X)
        else:
            self.list_status = True
            self.menu.new_button['state'] = 'disabled'
            self.menu.pdf_button['state'] = 'disabled'
            self.parts.forget()
            self.acts.pack(fill=X)

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


class FrameMenu(Frame):
    def __init__(self, app):
        Frame.__init__(self)
        self.pack(fill=X)
        self.app = app

        self.auth_button = Button(self, text='Вход', command=app.cb_auth)
        self.auth_button.pack(side=LEFT, expand=True, fill=X)

        self.new_button = Button(
            self, text='Новый', command=app.parts.init, state='disabled')
        self.new_button.pack(side=LEFT, expand=True, fill=X)

        self.pdf_button = Button(
            self, text='Сохранить', command=app.parts.save, state='disabled')
        self.pdf_button.pack(side=LEFT, expand=True, fill=X)

        self.list_button = Button(
            self, text='Список', command=self.app.cb_list, state='disabled')
        self.list_button.pack(side=LEFT, expand=True, fill=X)


class FrameParts(Frame):
    def __init__(self, db):
        Frame.__init__(self)
        frame = Frame(self)
        frame.pack(fill=X)
        self.is_visible = False

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

    def hide(self):
        self.forget()
        self.is_visible = False

    def save(self):
        try:
            self.check()
            self.insert()
            self.db.check()
            self.db.save()
            create_pdf('test.pdf', self.db)
        except CheckException as exc:
            showinfo('Проверка', exc.text)

    def show(self):
        self.pack(fill=X)
        self.show_part(1)
        self.init()
        self.is_visible = True

    def show_part(self, index):
        if self.index == index:
            return
        self.part_frames[self.index - 1].forget()
        self.buttons[self.index - 1].config(font='-size 10')
        if index:
            self.part_frames[index - 1].pack(fill=X)
            self.buttons[index - 1].config(font='-size 10 -weight bold')
        self.index = index


class ListboxActs(Listbox):
    def __init__(self):
        Listbox.__init__(self, height=34)
        # self.status = False


class TopLevelAuth(Toplevel):
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

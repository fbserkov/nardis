import os
import sys

from tkinter import (
    Button, Entry, Frame, LEFT, Listbox, StringVar, Tk, Toplevel, X)
from tkinter.messagebox import showinfo

from database import Database
from item import ItemBase, CheckException
from part import PassportPart, CommonPart, SurveyPart, ExaminationPart
from template import create_pdf


class App:
    def __init__(self):
        self.root = Tk()
        self._customize()
        self.db, self.auth_status = None, False

        self.file_exists_error = False
        self._lock()
        if self.file_exists_error:
            return

        self.file_not_found_error = False
        self._load()
        if self.file_not_found_error:
            return

        self.menu = FrameMenu(self)
        self.parts = FrameParts()
        self.acts = ListboxActs(self)
        self.root.mainloop()

    def _customize(self):
        self.root.title('Наркологическая экспертиза')
        self.root.geometry('610x650')
        self.root.resizable(width=False, height=False)
        if not sys.platform == 'linux':
            self.root.iconbitmap('nardis.ico')

    def _load(self):
        try:
            self.db = Database('nardis.db')
            ItemBase.db = self.db
        except FileNotFoundError:
            self._show_popup(
                title='Сообщение', message='База данных не найдена.')
            self.file_not_found_error = True

    def _lock(self):
        try:
            open('file.lock', 'x').close()
        except FileExistsError:
            self._show_popup(
                title='Сообщение', message='Приложение уже запущено.')
            self.file_exists_error = True

    def _show_popup(self, title, message):
        self.root.withdraw()
        showinfo(title, message)

    def init(self, index=None):
        if index is not None:
            print(index)
        self.db.init()
        self.parts.init()

    def save(self):
        try:
            self.parts.check()
            self.parts.insert()
            self.db.check()
            self.db.save()
            create_pdf('test.pdf', self.db)
        except CheckException as exc:
            showinfo('Проверка', exc.text)

    def switch_auth(self):
        if self.auth_status:
            self.parts.hide()
            self.acts.hide()
            self.auth_status = False
        else:
            if not TopLevelAuth(self.db).status:
                return False
            self.init()
            self.parts.show()
            self.auth_status = True
        return self.auth_status

    def switch_list(self):
        if self.acts.is_visible:
            self.acts.hide()
            self.parts.show()
        else:
            self.parts.hide()
            self.acts.show()
        return self.acts.is_visible

    def unlock(self):
        if self.file_exists_error:
            return
        os.remove('file.lock')


class FrameMenu(Frame):
    def __init__(self, app):
        Frame.__init__(self)
        self.pack(fill=X)
        self.app = app

        self.auth_button = Button(self, text='Вход', command=self.switch_auth)
        self.auth_button.pack(side=LEFT, expand=True, fill=X)

        self.new_button = Button(
            self, text='Новый', command=app.init, state='disabled')
        self.new_button.pack(side=LEFT, expand=True, fill=X)

        self.pdf_button = Button(
            self, text='Сохранить', command=app.save, state='disabled')
        self.pdf_button.pack(side=LEFT, expand=True, fill=X)

        self.list_button = Button(
            self, text='Список', command=self.switch_list, state='disabled')
        self.list_button.pack(side=LEFT, expand=True, fill=X)

    def switch_auth(self):
        if self.app.switch_auth():
            self.auth_button['text'] = 'Выход'
            self.new_button['state'] = 'normal'
            self.pdf_button['state'] = 'normal'
            self.list_button['state'] = 'normal'
            self.list_button['text'] = 'Список'
        else:
            self.auth_button['text'] = 'Вход'
            self.new_button['state'] = 'disabled'
            self.pdf_button['state'] = 'disabled'
            self.list_button['state'] = 'disabled'
            self.list_button['text'] = 'Список'

    def switch_list(self):
        if self.app.switch_list():
            self.new_button['state'] = 'disabled'
            self.pdf_button['state'] = 'disabled'
            self.list_button['text'] = 'Форма'
        else:
            self.new_button['state'] = 'normal'
            self.pdf_button['state'] = 'normal'
            self.list_button['text'] = 'Список'


class FrameParts(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.index, self.is_visible = 0, False

        frame = Frame(self)
        self.buttons = (
            Button(frame, text='I'), Button(frame, text='II'),
            Button(frame, text='III'), Button(frame, text='IV'),
        )
        for i, obj in enumerate(self.buttons):
            obj['command'] = lambda j=i: self.show_part(j + 1)
            obj.pack(side=LEFT, expand=True, fill=X)
        frame.pack(fill=X)

        self.part_frames = (
            PassportPart(self), CommonPart(self),
            SurveyPart(self), ExaminationPart(self),
        )

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

    def show(self):
        self.show_part(1)
        self.pack(fill=X)
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
    def __init__(self, app):
        self.app, self.is_visible = app, False
        self.frame, self.choices = Frame(padx=2, pady=1), StringVar()
        Listbox.__init__(
            self, master=self.frame, listvariable=self.choices, height=34)
        self.bind('<Double-1>', lambda e: app.init(e.widget.curselection()[0]))
        self.pack(fill=X)

    def _update(self):
        self.choices.set(self.app.db.get_acts_titles())

    def hide(self):
        self.frame.forget()
        self.is_visible = False

    def show(self):
        self._update()
        self.frame.pack(fill=X)
        self.is_visible = True


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

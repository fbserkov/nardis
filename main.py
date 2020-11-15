import os
import sys

from tkinter import (
    Button, E, Entry, Frame, Listbox, RIGHT,
    Scrollbar, StringVar, Tk, Toplevel, W, X, Y,
)
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
        self.acts = FrameList(self)
        self.root.mainloop()

    def _customize(self):
        self.root.title('Наркологическая экспертиза')
        self.root.geometry('610x630')
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
        self.db.init(index)
        self.parts.init()
        if index is not None:
            self.parts.select()

    def save(self):
        try:
            self.parts.check()
            self.parts.insert()
            self.db.check()
            self.db.save()
            create_pdf(self.db)
        except CheckException as exc:
            showinfo('Проверка', exc.text)

    def switch_auth(self):
        if self.auth_status:
            self.parts.hide()
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
        self._app = app

        self._buttons = (
            Button(self, text='Вход', command=self.switch_auth),
            Button(self, text='Новый', command=app.init),
            Button(self, text='Настройки'),
            Button(self, text='Сохранить', command=app.save),
            Button(self, text='Список', command=self.switch_list),
        )
        min_width = max(button.winfo_reqwidth() for button in self._buttons)
        for i in range(5):
            self.columnconfigure(i, weight=1, minsize=min_width)
            self._buttons[i].grid(row=0, column=i, sticky=E + W)
            self._buttons[i]['state'] = 'disabled'
        self._buttons[0]['state'] = 'normal'

    def switch_auth(self):
        if self._app.switch_auth():
            self._buttons[0]['text'] = 'Выход'
            self._buttons[1]['state'] = 'normal'
            if not self._app.db.get_current_doctor():
                self._buttons[2]['state'] = 'normal'
            self._buttons[3]['state'] = 'normal'
            self._buttons[4]['state'] = 'normal'
            self._buttons[4]['text'] = 'Список'
        else:
            self._buttons[0]['text'] = 'Вход'
            self._buttons[1]['state'] = 'disabled'
            self._buttons[2]['state'] = 'disabled'
            self._buttons[3]['state'] = 'disabled'
            self._buttons[4]['state'] = 'disabled'
            self._buttons[4]['text'] = 'Список'

    def switch_list(self):
        if self._app.switch_list():
            self._buttons[0]['state'] = 'disabled'
            self._buttons[1]['state'] = 'disabled'
            self._buttons[3]['state'] = 'disabled'
            self._buttons[4]['text'] = 'Форма'
        else:
            self._buttons[0]['state'] = 'normal'
            self._buttons[1]['state'] = 'normal'
            self._buttons[3]['state'] = 'normal'
            self._buttons[4]['text'] = 'Список'


class FrameParts(Frame):
    def __init__(self):
        Frame.__init__(self)
        self._index, self.is_visible = 0, False  # TODO is_visible isn't use

        frame = Frame(self)
        self._buttons = (
            Button(frame, text='I'), Button(frame, text='II'),
            Button(frame, text='III'), Button(frame, text='IV'),
        )
        min_width = max(button.winfo_reqwidth() for button in self._buttons)
        for i, button in enumerate(self._buttons):
            frame.columnconfigure(i, weight=1, minsize=min_width)
            button.grid(row=0, column=i, sticky=E + W)
            button['command'] = lambda j=i: self._switch_part(j + 1)
        frame.pack(fill=X)

        self.part_frames = (
            PassportPart(self), CommonPart(self),
            SurveyPart(self), ExaminationPart(self),
        )

    def _switch_part(self, index):
        if self._index == index:
            return
        self.part_frames[self._index - 1].forget()
        self._buttons[self._index - 1].config(font='-size 10')
        if index:
            self.part_frames[index - 1].pack(fill=X)
            self._buttons[index - 1].config(font='-size 10 -weight bold')
        self._index = index

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

    def select(self):
        for part_frame in self.part_frames:
            for item in part_frame.items.values():
                item.select()

    def show(self):
        self._switch_part(1)
        self.pack(fill=X)
        self.is_visible = True


class FrameList(Frame):
    def __init__(self, app):
        Frame.__init__(self, bd=4)
        self.app, self.choices, self.is_visible = app, StringVar(), False

        listbox = Listbox(master=self, listvariable=self.choices, height=32)
        scrollbar = Scrollbar(self, command=listbox.yview)
        listbox['yscrollcommand'] = scrollbar.set

        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.pack(fill=X)
        listbox.bind(
            '<Double-1>', lambda e: app.init(e.widget.curselection()[0]))
        listbox.bind('<Double-1>', lambda _: app.menu.switch_list(), add='+')

    def _update(self):
        self.choices.set(self.app.db.get_acts_titles())

    def hide(self):
        self.forget()
        self.is_visible = False

    def show(self):
        self._update()
        self.pack(fill=X)
        self.is_visible = True


class TopLevelAuth(Toplevel):
    def __init__(self, db):
        Toplevel.__init__(self)
        self.title('Введите пароль')
        self.db, self.status = db, False

        self.entry = Entry(self, font='-size 14', show='●')
        self.entry.bind('<Key-Return>', lambda _: self._auth())
        self.entry.bind('<KeyPress>', lambda _: self._ok())
        self.entry.pack()
        self.entry.focus()
        self.button = Button(
            self, font='-size 10', text='OK', command=self._auth)
        self.button.pack(fill=X)

        self.transient(self.master)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def _auth(self):
        if self.db.check_password(self.entry.get()):
            self.status = True
            self.destroy()
        else:
            self.button['text'] = 'Неверный пароль'

    def _ok(self):
        self.button['text'] = 'OK'


if __name__ == '__main__':
    App().unlock()

import os
import sys

from tkinter import Button, E, Entry, Frame, Tk, Toplevel, W, X
from tkinter.messagebox import showinfo

from database import Database
from item import CheckException, ItemBase
from subframe import ActsList, FormParts
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
        self.parts = FormParts()
        self.acts = ActsList(self)
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

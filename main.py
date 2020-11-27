import locale
import os
import sys

from tkinter import Button, E, Entry, Frame, Tk, Toplevel, W, X
from tkinter.messagebox import showinfo

from database import Database
from item import CheckException, ItemBase
from subframe import ActsList, FormParts, Settings
from template import PDF

locale.setlocale(locale.LC_ALL, '')


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
        self.settings = Settings(self.db)
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
            self.db = Database()
            self._show_popup(
                title='Сообщение',
                message='Создана пустая база\nданных (пароль: 000)',
            )
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
            self.db.save_act()
            PDF(self.db).create()
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

    def switch_settings(self):
        if self.settings.is_visible:
            try:
                self.settings.check()
                self.settings.save()
                self.settings.hide()
                self.parts.update_menu()
                self.parts.show()
            except CheckException as exc:
                showinfo('Проверка', exc.text)
        else:
            self.parts.hide()
            self.settings.init()
            self.settings.show()
        return self.settings.is_visible

    def unlock(self):
        if self.file_exists_error:
            return
        os.remove('file.lock')


class FrameMenu(Frame):
    def __init__(self, app):
        Frame.__init__(self)
        self.pack(fill=X)
        self._app = app

        keys = {0: 'auth', 1: 'new', 2: 'settings', 3: 'save', 4: 'list'}
        self._buttons = {
            keys[0]: Button(self, text='Вход', command=self.switch_auth),
            keys[1]: Button(self, text='Новый', command=app.init),
            keys[2]: Button(
                self, text='Настройки', command=self.switch_settings),
            keys[3]: Button(self, text='Сохранить', command=app.save),
            keys[4]: Button(self, text='Список', command=self.switch_list),
        }
        min_width = max(btn.winfo_reqwidth() for btn in self._buttons.values())
        for i, key in keys.items():
            self.columnconfigure(i, weight=1, minsize=min_width)
            self._buttons[key].grid(row=0, column=i, sticky=E + W)
            self._buttons[key]['state'] = 'disabled'
        self._buttons['auth']['state'] = 'normal'

    def switch_auth(self):
        if self._app.switch_auth():
            self._buttons['auth']['text'] = 'Выход'
            self._buttons['new']['state'] = 'normal'
            if self._app.db.is_opened_by_admin:
                self._buttons['settings']['state'] = 'normal'
            self._buttons['save']['state'] = 'normal'
            self._buttons['list']['state'] = 'normal'
            self._buttons['list']['text'] = 'Список'
        else:
            self._buttons['auth']['text'] = 'Вход'
            self._buttons['new']['state'] = 'disabled'
            self._buttons['settings']['state'] = 'disabled'
            self._buttons['save']['state'] = 'disabled'
            self._buttons['list']['state'] = 'disabled'
            self._buttons['list']['text'] = 'Список'

    def switch_list(self):
        if self._app.switch_list():
            self._buttons['auth']['state'] = 'disabled'
            self._buttons['new']['state'] = 'disabled'
            self._buttons['settings']['state'] = 'disabled'
            self._buttons['save']['state'] = 'disabled'
            self._buttons['list']['text'] = 'Форма'
        else:
            self._buttons['auth']['state'] = 'normal'
            self._buttons['new']['state'] = 'normal'
            if self._app.db.is_opened_by_admin:
                self._buttons['settings']['state'] = 'normal'
            self._buttons['save']['state'] = 'normal'
            self._buttons['list']['text'] = 'Список'

    def switch_settings(self):
        if self._app.switch_settings():
            self._buttons['auth']['state'] = 'disabled'
            self._buttons['new']['state'] = 'disabled'
            self._buttons['settings']['text'] = 'Сохранить'
            self._buttons['save']['state'] = 'disabled'
            self._buttons['list']['state'] = 'disabled'
        else:
            self._buttons['auth']['state'] = 'normal'
            self._buttons['new']['state'] = 'normal'
            self._buttons['settings']['text'] = 'Настройки'
            self._buttons['save']['state'] = 'normal'
            self._buttons['list']['state'] = 'normal'


class TopLevelAuth(Toplevel):
    def __init__(self, db):
        Toplevel.__init__(self)
        self.title('Введите пароль')
        self.db, self.status = db, False

        self.entry = Entry(self, font='-size 14', fg='#800000', show='●')
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

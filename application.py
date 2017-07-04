from database import Database
import os
from tkinter.messagebox import showinfo
from window.entrance import Entrance
from window.main import Main


class Application:
    def __init__(self):
        self.lock_file = None
        self.lock()

        self.database = Database()
        Entrance(self.database)
        if self.database.current_user:
            Main()

        self.unlock()

    def lock(self):
        try:
            self.lock_file = open('file.lock', 'r')
        except FileNotFoundError:
            self.lock_file = open('file.lock', 'w')
            self.lock_file.close()
        else:
            showinfo('Сообщение', 'Приложение уже запущено.')
            raise SystemExit

    @staticmethod
    def unlock():
        os.remove('file.lock')


application = Application()

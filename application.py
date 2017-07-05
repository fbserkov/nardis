from database import Database
import os
from window.entrance import Entrance
from window.main import Main
from window.window import Window


LOCK = False
PASSWORD = True


class Application:
    def __init__(self):
        self.lock_file = None
        if LOCK:
            self.lock()

        self.database = Database()
        if self.database.read():
            if PASSWORD:
                Entrance(self.database)
            else:
                self.database.current_user = True
        if self.database.current_user:
            Main(self.database)

        if LOCK:
            self.unlock()

    def lock(self):
        try:
            self.lock_file = open('file.lock', 'r')
        except FileNotFoundError:
            self.lock_file = open('file.lock', 'w')
            self.lock_file.close()
        else:
            Window().show_popup('Сообщение', 'Приложение уже запущено.', True)
            raise SystemExit

    @staticmethod
    def unlock():
        os.remove('file.lock')


application = Application()

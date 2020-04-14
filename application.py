from database import Database
import os
from window.entrance import Entrance
from window.main import Main
from window.window import Window


def lock(on):
    if not on:
        os.remove('file.lock')
        return
    try:
        open('file.lock', 'x').close()
    except FileExistsError:
        Window().show_popup(
            title='Сообщение', message='Приложение уже запущено.', alone=True)
        raise SystemExit


class Application:
    def __init__(self):
        lock(True)
        self.database = Database()
        if self.database.read():
            Entrance(self.database)
        if self.database.current_user:
            Main(self.database)
        lock(False)


application = Application()

from database import Database
import os
from window.entrance import Entrance
from window.main import Main
from window.window import WindowBase

try:
    open('file.lock', 'x').close()
    database = Database('nardis.db')
    Entrance(database)
    if database.current_user:
        Main(database)
    os.remove('file.lock')
except FileExistsError:
    WindowBase().show_popup(
        title='Сообщение', message='Приложение уже запущено.', alone=True)
except FileNotFoundError:
    WindowBase().show_popup(
        title='Сообщение', message='База данных не найдена.', alone=True)
    os.remove('file.lock')
except KeyboardInterrupt:
    os.remove('file.lock')

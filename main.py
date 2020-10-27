from database import Database
import os
from window.window import WindowAuth, WindowBase, WindowMain

try:
    open('file.lock', 'x').close()
    database = Database('nardis.db')
    WindowAuth(database)
    if database.current_user:
        WindowMain(database)
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

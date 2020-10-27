import os

from database import Database
from window import WindowBase, WindowMain


class App:
    def __init__(self):
        self.file_exists_error = False
        self.check_lock()
        if self.file_exists_error:
            return
        self.file_not_found_error = False
        self.data = self.load_data()
        if self.file_not_found_error:
            return
        WindowMain(self.data)

    def check_lock(self):
        try:
            open('file.lock', 'x').close()
        except FileExistsError:
            WindowBase().show_popup(
                title='Сообщение',
                message='Приложение уже запущено.',
                alone=True,
            )
            self.file_exists_error = True

    def load_data(self):
        try:
            return Database('nardis.db')
        except FileNotFoundError:
            WindowBase().show_popup(
                title='Сообщение',
                message='База данных не найдена.',
                alone=True,
            )
            self.file_not_found_error = True

    def __del__(self):
        if self.file_exists_error:
            return
        os.remove('file.lock')


if __name__ == '__main__':
    App()

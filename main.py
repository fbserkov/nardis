import os

from tkinter import Tk
from tkinter.messagebox import showinfo

from database import Database
from window import WindowMain


class App:
    def __init__(self):
        self.root = Tk()

        self.file_exists_error = False
        self.check_lock()
        if self.file_exists_error:
            return

        self.file_not_found_error = False
        self.data = self.load_data()
        if self.file_not_found_error:
            return

        WindowMain(self.root, self.data)

    def __del__(self):
        if self.file_exists_error:
            return
        os.remove('file.lock')

    def check_lock(self):
        try:
            open('file.lock', 'x').close()
        except FileExistsError:
            self.show_popup(
                title='Сообщение', message='Приложение уже запущено.')
            self.file_exists_error = True

    def load_data(self):
        try:
            return Database('nardis.db')
        except FileNotFoundError:
            self.show_popup(
                title='Сообщение', message='База данных не найдена.')
            self.file_not_found_error = True

    def show_popup(self, title, message):
        self.root.withdraw()
        showinfo(title, message)


if __name__ == '__main__':
    App()

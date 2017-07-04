from database import Database
from entrance import Entrance


class Application:
    def __init__(self):
        self.database = Database()
        Entrance(self.database)
        if self.database.current_user:
            pass    # создаём главное окно
        print('End.')


application = Application()

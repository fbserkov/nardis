import pickle
import time
from window.window import Window


database_name = 'nardis.db'


class Database:
    def __init__(self):
        self.current_user = None
        self.current_year = None
        self.current_index = -1
        self.settings = None
        self.folders = None

    def read(self):
        try:
            with open(database_name, 'rb') as f:
                database = pickle.load(f)
        except FileNotFoundError:
            Window().show_popup('Сообщение', 'База данных не найдена.', True)
            return False
        self.settings = database[0]
        self.folders = database[1]
        return True

    # использовать только при наличии изменений
    def write(self):
        database = [self.settings, self.folders]
        with open(database_name, 'wb') as f:
            pickle.dump(database, f)

    def get_years(self):
        years = sorted(self.folders.keys())
        current_year = int(time.strftime('%Y'))
        if current_year not in years:
            years.append(current_year)
        return years

    def authentication(self, password, current_year):
        if password in self.settings['Врачи'].keys():
            self.current_user = self.settings['Врачи'][password].partition(',')[0]
            self.current_year = current_year
            return True
        return False

    def get_doctors(self):
        doctors = None
        if self.current_user == 'admin':
            doctors = list(self.settings['Врачи'].values())
            doctors.remove('admin')
        else:
            for line in self.settings['Врачи'].values():
                if line.find(self.current_user) != -1:
                    doctors = [line]
                    break
        return doctors

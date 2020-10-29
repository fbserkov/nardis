import pickle
import time


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.current_user = None
        self.changed = False
        with open(self.filename, 'rb') as f:
            database = pickle.load(f)
        self.settings, self.folders = database
        self.current_year = -1
        self.current_index = -1

    def __del__(self):
        if not self.changed:
            return
        with open(self.filename, 'wb') as file:
            pickle.dump((self.settings, self.folders), file)

    def check_password(self, password):
        if password in self.settings['Врачи'].keys():
            self.current_user = (
                self.settings['Врачи'][password])
            return True
        return False

    def get_chemicals(self):
        return self.settings['Вещества']

    def get_doctors(self):
        doctors = list(self.settings['Врачи'].values())
        doctors.remove('admin')
        return doctors

    def get_index(self):
        return self.settings['Номер следующего акта']

    def get_methods(self):
        return self.settings['Методы']

    def get_technical_means(self):
        return self.settings['Технические средства']

    def get_years(self):
        years = sorted(self.folders.keys())
        current_year = int(time.strftime('%Y'))
        if current_year not in years:
            years.append(current_year)
        return years

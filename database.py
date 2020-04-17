import pickle
import time

database_name = 'nardis.db'


class Database:
    def __init__(self):
        self.changed = False
        with open(database_name, 'rb') as f:
            database = pickle.load(f)
        self.settings, self.folders = database
        self.current_index = -1
        self.current_user = None

    def __del__(self):
        if not self.changed:
            return
        with open(database_name, 'wb') as file:
            pickle.dump((self.settings, self.folders), file)

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

    def get_technical_means(self):
        return self.settings['Технические средства']

    def get_methods(self):
        return self.settings['Методы']

    def get_chemicals(self):
        return self.settings['Вещества']

import pickle
from popup import dat_name, popup_name
import time


class Database:
    def __init__(self):
        self.current_user = None
        self.current_year = None
        try:
            with open(dat_name, 'rb') as f:
                database = pickle.load(f)
            self.settings = database[0]
            self.folders = database[1]
        except FileNotFoundError:
            popup_name(dat_name)

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

    # использовать только при наличии изменений
    def save(self):
        with open(dat_name, 'wb') as f:
            database = [self.settings, self.folders]
            pickle.dump(database, f)

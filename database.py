import pickle


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.current_user = None
        with open(self.filename, 'rb') as f:
            self.settings, self.reports = pickle.load(f)

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

    def get_report(self):  # TODO test mode now
        # index = self.settings['Номер следующего акта']
        # self.settings['Номер следующего акта'] = index + 1
        if not self.reports:
            self.reports.append({})
        return self.reports[-1]

    def get_technical_means(self):
        return self.settings['Технические средства']

    def save(self):
        with open(self.filename, 'wb') as file:
            pickle.dump((self.settings, self.reports), file)

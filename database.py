import pickle


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.current_user = None
        with open(self.filename, 'rb') as f:
            self._settings, self.reports = pickle.load(f)

    def check_password(self, password):
        if password in self._settings['Врачи'].keys():
            self.current_user = (
                self._settings['Врачи'][password])
            return True
        return False

    def get_chemicals(self):
        return self._settings['Вещества']

    def get_doctors(self):
        doctors = list(self._settings['Врачи'].values())
        doctors.remove('admin')
        return doctors

    def get_index(self):
        return self._settings['Номер следующего акта']

    def get_laboratory_name(self):
        return self._settings['Лаборатория']

    def get_methods(self):
        return self._settings['Методы']

    def get_organization(self):
        return self._settings['Организация']

    def get_report(self):
        return self.reports[-1]

    def get_technical_means(self):
        return self._settings['Технические средства']

    def get_unit_name(self):
        return self._settings['Подразделение']

    def save(self):
        with open(self.filename, 'rb') as file_1:
            temp = file_1.read()
        with open(self.filename, 'wb') as file_2:
            try:
                pickle.dump((self._settings, self.reports), file_2)
            except Exception as exception:
                with open(self.filename, 'wb') as file_1:
                    file_1.write(temp)
                    raise exception

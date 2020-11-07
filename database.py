import pickle

from item import CheckException


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.current_user = None
        with open(self.filename, 'rb') as f:
            self._settings, self.reports = pickle.load(f)

    def check(self):
        datetime_4 = self.select(4, 'datetime')
        datetime_13_1 = self.select(13, 'datetime_1')
        datetime_13_2 = self.select(13, 'datetime_2')
        datetime_16 = self.select(16, 'datetime')

        if datetime_13_1 and datetime_13_1 < datetime_4:
            raise CheckException('Несоответствие времени\nв пунктах 13.1 и 4.')
        if datetime_13_1 and datetime_13_2:
            if not 15 <= (datetime_13_2 - datetime_13_1).seconds / 60 <= 20:
                raise CheckException(
                    'Интервал в пункте 13\nне равен 15-20 минутам.')
        if datetime_13_1 and datetime_13_1 > datetime_16:
            raise CheckException(
                'Несоответствие времени\nв пунктах 13.1 и 16.')
        if datetime_13_2 and datetime_13_2 > datetime_16:
            raise CheckException(
                'Несоответствие времени\nв пунктах 13.2 и 16.')
        if datetime_16 < datetime_4:
            raise CheckException('Несоответствие\nв пунктах 4 и 16.')

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

    def get_act_number(self):
        return self._settings['Номер следующего акта']

    def get_devices(self):
        return self._settings['Технические средства']

    def get_laboratory_name(self):
        return self._settings['Лаборатория']

    def get_methods(self):
        return self._settings['Методы']

    def get_organization(self):
        return self._settings['Организация']

    def get_report(self):
        return self.reports[-1]

    def get_subdivision(self):
        return self._settings['Подразделение']

    def insert(self, i, key, value):
        report = self.get_report()
        report[i, key] = value

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

    def select(self, i, key):
        report = self.get_report()
        return report[i, key]

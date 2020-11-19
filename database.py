import pickle

from default import default_settings
from item import CheckException


class Database:
    def __init__(self, filename=None):
        self._filename, self.is_opened_by_admin = filename, False
        self._current_act, self.current_doctor = None, None
        if filename:
            with open(self._filename, 'rb') as f:
                self._settings, self._acts = pickle.load(f)
        else:
            self._settings, self._acts = default_settings, []
            with open('nardis.db', 'wb') as file:
                pickle.dump((self._settings, self._acts), file)

    @staticmethod
    def _act2title(act):
        return (
            f'{act[0, "number"]}/{act[0, "year"]} '
            f'{act[1, "full_name"]} ({act[17, "opinion"]})'
        )

    def _doctor_filter(self, act):
        if self.is_opened_by_admin:
            return True
        return act[5, 'doctor'] == self.current_doctor.split(', ')[0]

    def _dump(self):
        with open(self._filename, 'rb') as file_1:
            temp = file_1.read()
        with open(self._filename, 'wb') as file_2:
            try:
                pickle.dump((self._settings, self._acts), file_2)
            except Exception as exc:
                with open(self._filename, 'wb') as file_1:
                    file_1.write(temp)
                    raise exc

    def _find(self, act_):
        number_, year_ = act_[0, 'number'], act_[0, 'year']
        for index, act in enumerate(self._acts):
            number, year = act[0, 'number'], act[0, 'year']
            if number == number_ and year == year_:
                return index

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
        self.current_doctor = self.select('doctors').get(password)
        self.is_opened_by_admin = self.select('password') == password
        if self.is_opened_by_admin:
            return True
        return True if self.current_doctor else False

    def get_acts_titles(self):
        return {
            self._act2title(act): i for i, act in enumerate(self._acts)
            if self._doctor_filter(act)
        }

    def get_doctors(self):
        return list(self.select('doctors').values())

    def init(self, index=None):
        if index is None:
            self._current_act = {}
        else:
            self._current_act = self._acts[index]

    def insert(self, *args):
        if len(args) == 3:
            i, key, value = args
            self._current_act[i, key] = value
        else:
            key, value = args[:2]
            self._settings[key] = value

    def save_act(self):
        index = self._find(self._current_act)
        if index is None:
            self._acts.append(self._current_act)
            self.insert('next_number', self.select(0, 'number') + 1)
        self._dump()

    def save_settings(self):
        self._dump()

    def select(self, *args):
        if len(args) == 2:
            i, key = args
            return self._current_act[i, key]
        else:
            key = args[0]
            return self._settings[key]

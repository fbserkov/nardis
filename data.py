from time import strftime


minus = '«-»'
plus = '«+»'


def get_simple_labels_data(chemicals):
    return (
        (14, 3, 'метод исследования'),
        (14, 3, 'Результаты химико-токсикологических исследований'),
        (14, 3, 'номер справки'),
        (14, 3, strftime('/%y')),
        (14, 3, chemicals[0]),
        (14, 3, chemicals[1]),
        (14, 3, chemicals[2]),
        (14, 3, chemicals[3]),
        (14, 3, chemicals[4]),
        (14, 3, chemicals[5]),
        (14, 3, chemicals[6]),
        (14, 3, chemicals[7]),
        (14, 3, chemicals[8]),
        (14, 3, chemicals[9]),
        (14, 3, chemicals[10]),
        (15, 3, '15. Другие данные'),
        (17, 3, '17. Заключение'),
        (17, 3, 'Дата'))


def get_entries_data():
    return (
        (14, 3,  5, True,  ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (14, 3,  3, False, ''),
        (15, 3, 73, True,  'нет'),
        (17, 3, 44, False, ''),
        (17, 3, 10, True,  ''))


def get_smart_labels_data():
    return (
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (14, 3, minus),
        (14, 3, plus),
        (17, 3, 'от медицинского освидетельствования отказался'),
        (17, 3, 'установлено состояние опьянения'),
        (17, 3, 'состояние опьянения не установлено'))

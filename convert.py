from datetime import date, datetime, time


def date2str(obj):
    """
    >>> date2str(None)
    ''
    >>> date2str(date(2020, 12, 4))
    '04.12.2020'
    """
    if obj is None:
        return ''
    return obj.strftime('%d.%m.%Y')


def datetime2str(obj):
    """
    >>> datetime2str(None)
    ''
    >>> datetime2str(datetime(2020, 12, 4, 18, 44))
    '04.12.2020 18:44'
    """
    if obj is None:
        return ''
    return obj.strftime('%d.%m.%Y %H:%M')


def datetime2str_time(obj):
    """
    >>> datetime2str_time(None)
    ''
    >>> datetime2str_time(datetime(2020, 12, 4, 18, 44))
    '18:44'
    """
    if obj is None:
        return ''
    return obj.strftime('%H:%M')


def str2date(line):
    """
    >>> str2date('')
    >>> str2date('04.12.2020')
    datetime.date(2020, 12, 4)
    """
    if line == '':
        return None
    return datetime.strptime(line, '%d.%m.%Y').date()


def str2datetime(line):
    """
    >>> str2datetime(' ')
    >>> str2datetime('04.12.2020 18:44')
    datetime.datetime(2020, 12, 4, 18, 44)
    """
    line_1, line_2 = line.split(' ')
    obj_1, obj_2 = str2date(line_1), str2time(line_2)
    if not (obj_1 and obj_2):
        return None
    return datetime.combine(obj_1, obj_2)


def str2time(line):
    """
    >>> str2time('')
    >>> str2time('18:44')
    datetime.time(18, 44)
    """
    if line == '':
        return None
    return datetime.strptime(line, '%H:%M').time()


def time2str(obj):
    """
    >>> time2str(None)
    ''
    >>> time2str(time(18, 44))
    '18:44'
    """
    if obj is None:
        return ''
    return obj.strftime('%H:%M')


if __name__ == "__main__":
    import doctest
    doctest.testmod()

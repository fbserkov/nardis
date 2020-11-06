from datetime import datetime


def date2str(obj):
    if obj is None:
        return ''
    return obj.strftime('%d.%m.%Y')


def datetime2str(obj):
    if obj is None:
        return ''
    return obj.strftime('%d.%m.%Y %H:%M')


def datetime2str_time(obj):
    if obj is None:
        return ''
    return obj.strftime('%H:%M')


def str2date(line):
    if line == '':
        return None
    return datetime.strptime(line, '%d.%m.%Y').date()


def str2datetime(line):
    line_1, line_2 = line.split(' ')
    obj_1, obj_2 = str2date(line_1), str2time(line_2)
    if not (obj_1 and obj_2):
        return None
    return datetime.combine(obj_1, obj_2)


def str2time(line):
    if line == '':
        return None
    return datetime.strptime(line, '%H:%M').time()


def time2str(obj):
    if obj is None:
        return ''
    return obj.strftime('%H:%M')

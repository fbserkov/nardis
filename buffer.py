# Чтение данных инициализации                                        ReadInit
    # Подготовка строк
    # Однострочные данные
    # Многострочные данные
    # Списки данных
    # Словари данных
# Запись данных инициализации                                        WriteInit

from os import remove
from tkinter import Entry, Frame, Label, Listbox, Scrollbar
from form import dX, dY
from popup import exe_name, PopupName   # ini_name - уже не используется

# Чтение данных инициализации
def ReadInit(lines):
    init = {}
    # Подготовка строк
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    while True:
        try:
            lines.remove('')
        except:
            break
    # Однострочные данные
    def getLine(line):
        for i in range(len(lines)):
            if lines[i] == line:
                return lines[i + 1]
        PopupName(ini_name, line)
    init['Подразделение'] = getLine('[Подразделение]')
    init['Лаборатория']   = getLine('[Лаборатория]')
    # Многострочные данные
    def lastLine(n):
        return n + 1 == len(lines) or lines[n + 1][0] == '['
    line = '[Организация]'
    temp = ''
    for i in range(len(lines)):
        if lines[i] == line:
            while not lastLine(i):
                temp += lines[i + 1]
                i += 1
                if not lastLine(i):
                    temp += '\n'
    if not temp:
        PopupName(ini_name, line)
    init['Организация'] = temp
    # Списки данных
    def getList(line):
        temp = []
        for i in range(len(lines)):
            if lines[i] == line:
                while not lastLine(i):
                    temp.append(lines[i + 1])
                    i += 1
        if not temp:
            PopupName(ini_name, line)
        return temp
    init['Вещества']             = getList('[Вещества]')
    while len(init['Вещества']) < 11:
        init['Вещества'].append('(пусто)')
    init['Технические средства'] = getList('[Технические средства]')
    init['Методы']               = getList('[Методы]')
    # Словари данных
    def getDict(line):
        temp = {}
        for i in range(len(lines)):
            if lines[i] == line:
                while not lastLine(i):
                    temp1, trash, temp2 = lines[i + 1].partition(':')
                    temp[temp1.strip()] = temp2.strip()
                    i += 1
        if not temp:
            PopupName(ini_name, line)
        return temp
    init['Врачи'] = getDict('[Врачи]')
    return init

# Запись данных инициализации
def WriteInit(init):
    lines = ''
    # Организация
    lines += '[Организация]\n'
    lines += init['Организация'] + '\n'
    lines += '\n'
    # Подразделение
    lines += '[Подразделение]\n'
    lines += init['Подразделение'] + '\n'
    lines += '\n'
    # Врачи
    lines += '[Врачи]\n'
    temp = sorted(init['Врачи'].items(), key = lambda x: x[1])
    for item in temp:
        lines += item[0] + ': ' + item[1] + '\n'
    lines += '\n'
    # Технические средства
    lines += '[Технические средства]\n'
    for item in init['Технические средства']:
        lines += item + '\n'
    lines += '\n'
    # Лаборатория
    lines += '[Лаборатория]\n'
    lines += init['Лаборатория'] + '\n'
    lines += '\n'
    # Методы
    lines += '[Методы]\n'
    for item in init['Методы']:
        lines += item + '\n'
    lines += '\n'
    # Вещества
    lines += '[Вещества]'
    for item in init['Вещества']:
        lines += '\n' + item
    return lines

##########

# Список
def getLB(LF):
    # Создание
    LB_label = Label(LF, font='-size 10', text='№' + 9*' ' +
                     'Дата' + 13*' ' + 'ФИО' + 25*' ' + 'Найти')
    LB_entry = Entry(LF, width=15, font='-size 10', fg='#800000')
    LB_frame = Frame(LF)
    SB = Scrollbar(LB_frame)
    SB.pack(side='right', fill='y')
    LB = Listbox(LB_frame, font='-size 10', width=71, height=35, fg='#800000')
    LB.pack()
    SB['command'] = LB.yview
    LB['yscrollcommand'] = SB.set
    LB_label.place(x= 2*dX, y=0*dY + 3)
    LB_entry.place(x=40*dX, y=0*dY + 4)
    LB_frame.place(x= 1*dX, y=1*dY)
    return LB, LB_entry

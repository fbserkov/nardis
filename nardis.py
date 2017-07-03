from form import (check, dX, dY, entries, init_simple_labels, init_entries,
                  init_smart_labels, init_option_menus, init_checkbuttons,
                  place, write_indexes, get_data_lines, set_data_lines,
                  get_print_data)
from os import remove
from pickle import dump, load
from popup import dat_name, exe_name, pdf_name, PopupName
from subprocess import Popen
from sys import platform
from template import createPDF
from time import strftime
from tkinter import (Button, END, Entry, Frame, Label, LabelFrame, Listbox,
                     OptionMenu, Scrollbar, StringVar, Text, Tk, Toplevel)
from tkinter.messagebox import askyesno


# Константы
X =    551  # ширина окна (не более 1366)
Y =    672  # высота окна (не более  768)
frame =  3  # толщина рамки окна    (Windows XP)
title = 26  # высота заголовка окна (Windows XP)

# Переменные
current = {'user': '', 'year': -1, 'index': -1}

# Настройка главного окна
root = Tk()
temp_x = (root.winfo_screenwidth()  - (X + 2*frame))/2
temp_y = (root.winfo_screenheight() - (Y + 2*frame + title))/3
root.geometry('%dx%d+%d+%d' % (X, Y, temp_x, temp_y))
if not platform == 'linux':
    root.iconbitmap('nardis.ico')
root.title('Наркологическая экспертиза')
root.resizable(False, False)

# Вспомогательная функция
def dqRoot():
    lock.close()
    try:
        remove('#LOCK')
        remove(pdf_name)
    except:
        pass
    root.destroy()
    root.quit()

# Запрет второго экземпляра
global lock
lock = open('#LOCK', 'w')
try:
    lock.close()
    remove('#LOCK')
    lock = open('#LOCK', 'w')
except PermissionError:
    PopupName(exe_name)
    dqRoot()
    raise SystemExit

# Чтение базы данных
try:
    with open('nardis.dat', 'rb') as f:
        DB = load(f)
except:
    PopupName(dat_name)
    dqRoot()
    raise SystemExit
init = DB[0]
base = DB[1]

# Запрос пароля
 # Окно
tl_psw = Toplevel()
X = 154
Y = 84
temp_x = (root.winfo_screenwidth()  - (X + 2*frame))/2
temp_y = (root.winfo_screenheight() - (Y + 2*frame + title))/3
tl_psw.geometry('%dx%d+%d+%d' % (X, Y, temp_x, temp_y))
if not platform == 'linux':
    tl_psw.iconbitmap('nardis.ico')
tl_psw.title('Введите пароль')
tl_psw.resizable(False, False)
 # Элементы
sv = StringVar(tl_psw)
y = int(strftime('%Y'))
sv.set(y)
l = list(base.keys())
if y + 1 not in base.keys():
    l.append(y + 1)
om = OptionMenu(tl_psw, sv, *l)
om.config(width=16, font='-size 10', fg='#800000')
e = Entry(tl_psw, width=14, font='-size 14', show='●')
b = Button(tl_psw, width=18, text='OK', font='-size 10')
om.place(x=0*dX - 1, y=0*dY - 2)
e.place (x=0*dX    , y=1*dY + 1)
b.place (x=0*dX    , y=2*dY)
def cbf():
    if e.get() in init['Врачи'].keys():
        current['user'] = init['Врачи'][e.get()].partition(',')[0]
        current['year'] = int(sv.get())
        tl_psw.destroy()
        tl_psw.quit()
e.bind('<Key-Return>', lambda _: cbf())
b.config(command=cbf)
e.focus()
 # Модальность
tl_psw.transient(root)
tl_psw.grab_set()
root.wait_window(tl_psw)
 # Закрытие без пароля
if not current['user']:
    dqRoot()
    raise SystemExit

# Создание подразделов формы и списка актов
LFs = []
LFs.append(LabelFrame(height=17*dY - 7, text='Паспортная часть'))
LFs.append(LabelFrame(height=13*dY - 7, text='Общие данные'))
LFs.append(LabelFrame(height=21*dY - 7, text='Объективный осмотр'))
LFs.append(LabelFrame(height=23*dY - 7, text='Данные освидетельствования'))
for item in LFs:
    item.config(width=67*dX, font='-weight bold -size 10')

# Создание списка актов
F = Frame(height=23*dY - 7, width=67*dX)


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


# Создание и размещение элементов формы и списка актов
init_simple_labels(LFs, init)
init_entries(LFs)
init_smart_labels(LFs)
init_option_menus(LFs, init, current['user'])
init_checkbuttons(LFs)
LB, LB_entry = getLB(F)
place()
if False:
    write_indexes()
 # Указание следующего номера акта
if current['year'] not in base.keys():
    base[current['year']] = []
if base[current['year']]:
    temp = int(base[current['year']][len(base[current['year']]) - 1][0])
else:
    temp = 0
entries[0][0].config(state='normal')
entries[0][0].insert(0, str(temp + 1))
entries[0][0].config(state='disabled')
save = get_data_lines()


 # Функция поиска (заполнение списка актов)
def Find(temp=''):
    LB.delete(0, END)
    BI.clear()
    for lines in base[current['year']]:
        line = ' %s    %s    %s' % (lines[0].zfill(4), lines[8], lines[2])
        if ((current['user'] == 'admin' or lines[10].find(current['user']) != -1) and
            line.lower().find(temp.lower()) != -1):
            BI.insert(0, base[current['year']].index(lines))
            LB.insert(0, line)
def cbFind(event):
    Find(LB_entry.get())
BI = []
LB_entry.bind('<KeyRelease>', cbFind)

# Главные функции
 # Сохранение данных в базу
def Save():
    lines = get_data_lines()
    # Запись акта
    if current['index'] == -1:
        current['index'] = len(base[current['year']])
        base[current['year']].append(lines)
    else:
        base[current['year']][current['index']] = lines
    global save
    save = get_data_lines()
 # Загрузка данных из базы
def Open():
    try:
        current['index'] = BI[LB.curselection()[0]]
    except:
        Show(4)
        return
    lines = base[current['year']][current['index']]
    set_data_lines(lines)
    global save
    save = get_data_lines()
    Show(0)
 # Создание и открытие PDF-файла
def Print():
    try:
        f = open(pdf_name, 'w')
        f.close()
        data = get_print_data(init)
        createPDF(data, pdf_name)
        if not platform == 'linux':
            Popen(pdf_name, shell=True)
        else:
            Popen('evince %s' % pdf_name, shell=True)
    except PermissionError:
        PopupName(pdf_name)

# Создание и настройка кнопок
 # Переключение подразделов формы
def Show(n):
    F.place_forget()
    for i in range(len(LFs)):
        if i == n:
            LF_Bs[i].config(font='-weight bold -size 10')
            LFs[i].place(x=1*dX, y=1*dY)
        else:
            LF_Bs[i].config(font='-size 10')
            LFs[i].place_forget()
    if n == 4:
        for i in range(len(LFs)):
            LFs[i].place_forget()
        F.place(x=1*dX, y=1*dY)
        LB_entry.delete(0, END)
        Find()
def cbShow(event):
    Show(LF_Bs.index(event.widget))
def cbShowF(event):
    Show(4)
LF_Bs = []
LF_Bs.append(Button(text='I'))
LF_Bs.append(Button(text='II'))
LF_Bs.append(Button(text='III'))
LF_Bs.append(Button(text='IV'))
for i in range(len(LF_Bs)):
    LF_Bs[i].config(width=7, font='-size 10')
    LF_Bs[i].place(x=(17 + i*9)*dX, y=0*dY)
    LF_Bs[i].bind('<Button-1>', cbShow)
 # "Переключение" списка актов
F_B = Button(text='Список', width=7, font='-size 10')
F_B.place(x=56*dX, y=0*dY)
F_B.bind('<Button-1>', cbShowF)
 # Вызов главных функций
def cbOpen():
    if get_data_lines() != save:
        if askyesno('Вопрос', 'Сохранить акт?'):
            if check():
                Save()
            else:
                return
    Open()
def cbPrint():
    if check():
        Save()
        Print()
def cbNew():
    if cbExit():
        if not platform == 'linux':
            Popen('nardis', shell=True)     # вызов .exe-файла
        else:
            Popen('python3 nardis.py', shell=True)
def cbExit():
    if get_data_lines() != save:
        if askyesno('Вопрос', 'Сохранить акт?'):
            if check():
                Save()
            else:
                return False
    dqRoot()
    with open('nardis.dat', 'wb') as f:
        DB = [init, base]
        dump(DB, f)
    return True
MF_Bs = []
MF_Bs.append(Button(F,      text='Открыть', command=cbOpen))
MF_Bs.append(Button(LFs[3], text='Печать',  command=cbPrint))
MF_Bs.append(Button(        text='Рестарт', command=cbNew))
for item in MF_Bs:
    item.config(width=7, font='-size 10')
MF_Bs[0].place(x=55*dX, y= 0*dY)
MF_Bs[1].place(x=57*dX, y=21*dY - 3)
MF_Bs[2].place(x=5*dX, y= 0*dY)
MF_Bs[1].config(font='-weight bold -size 10')


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
        PopupName(exe_name, line)
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
        PopupName(exe_name, line)
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
            PopupName(exe_name, line)
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
            PopupName(exe_name, line)
        return temp
    init['Врачи'] = getDict('[Врачи]')
    return init


# Настройки администратора (и удаление)
tl = None
def cbtl():
    global tl, init
    init = ReadInit(t.get(1.0, END).split('\n'))
    tl.destroy()
    tl.quit()
    cbNew()
    tl = None


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


def cbSets():
    global tl
    if tl: return
    tl = Toplevel()
    X = 551
    Y = 672
    temp_x = (root.winfo_screenwidth()  - (X + 2*frame))/2
    temp_y = (root.winfo_screenheight() - (Y + 2*frame + title))/3
    tl.geometry('%dx%d+%d+%d' % (X, Y, temp_x, temp_y))
    if not platform == 'linux':
        tl.iconbitmap('nardis.ico')
    tl.title('Данные инициализации')
    tl.resizable(False, False)
    # Элементы
    sb = Scrollbar(tl)
    sb.pack(side='right', fill='y')
    global t
    t = Text(tl, font='-size 10', height=42)
    t.pack(fill='both')
    sb['command'] = t.yview
    t['yscrollcommand'] = sb.set
    # Отображение данных инициализации
    lines = WriteInit(init)
    for line in lines:
        t.insert(END, line)
    tl.protocol('WM_DELETE_WINDOW', cbtl)
     # Модальность
    tl.transient(root)
    tl.grab_set()
    root.wait_window(tl)
def cbDel():
    try:
        current['index'] = BI[LB.curselection()[0]]
    except:
        Show(4)
        return
    base[current['year']].remove(base[current['year']][current['index']])
    Show(4)
if current['user'] == 'admin':
    bSet = Button(width=12, font='-weight bold -size 10',
                  text='Настройка', command=cbSets)
    bSet.place(x=28*dX, y=23*dY)
    bDel = Button(F, width=7, font='-size 10',
                  text='Удалить', command=cbDel)
    bDel.place(x=25*dX, y=0*dY)
    entries[0][0].config(state='normal')

# Запуск окна
Show(0)
root.protocol('WM_DELETE_WINDOW', cbExit)
root.mainloop()

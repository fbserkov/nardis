# Константы и списки
# Создание элементов формы
#     Обыкновенные надписи                                      getSimpleLs
#         Текст надписей
#         Размер текста
#     Текстовые поля                                            getEs
#         Ширина полей
#         Размер и цвет текста
#         Значения по умолчанию
#         Отключение полей
#         Обработчики событий
#     Интерактивные надписи                                     getSmartLs
#         Текст надписей
#         Размер, подчёркивание и цвет текста
#         Реакция на указатель мыши
#         Добавление варианта
#         Замена варианта
#         "Умное" добавление варианта
#         "Умная" замена варианта
#     Выпадающие списки                                         getOMs
#     Флажки                                                    getCBs
# Размещение элементов формы                                    Place
#     I. Паспортная часть
#     II. Общие данные
#     III. Объективный осмотр
#     IV. Данные освидетельствования
# Вывод индексации списков                                      WriteIndexes
# Работа с элементаци формы
#     Проверка данных формы                                     Check
#         I. Паспортная часть
#         IV. Данные освидетельствования
#         Последовательность событий
#     Чтение данных из формы                                    getDataLines
#     Запись данных в форму                                     setDataLines
#     Подготовка данных к печати                                getPrintData


from popup import PopupTag
from data import get_entries_width, get_simple_labels_text
from time import strftime, strptime
from tkinter import (Checkbutton, END, Entry, IntVar,
                     Label, OptionMenu, StringVar)


# Константы и списки
dX = 8  # шаг сетки по X
dY = 28  # шаг сетки по Y
N = 18  # Количество пунктов в форме акта
minus = '«-»'
plus = '«+»'
simple_Ls = []
E_defaults = []
Es = []
smart_Ls = []
OM_notes = []
SVs = []
OMs = []
CB_texts = []
IVs = []
CBs = []

# Создание элементов формы
## Обыкновенные надписи
def getSimpleLs(LFs, init):
    for i in range(N):
        simple_Ls.append([])
    # Текст надписей
    for item in get_simple_labels_text(init['Вещества']):
        simple_Ls[item[0]].append(Label(LFs[item[1]], text=item[2]))
    # Размер текста
    for i_item in simple_Ls:
        for j_item in i_item:
            j_item.config(font='-size 10')
## Текстовые поля
def getEs(LFs):
    for i in range(N):
        Es.append([])
    # Ширина полей
    for item in get_entries_width():
        Es[item[0]].append(Entry(LFs[item[1]], width=item[2]))
    # Размер и цвет текста
    for item in Es:
        for jtem in item:
            jtem.config(font='-size 10', fg='#800000')
    # Значения по умолчанию
    for i in range(N):
        E_defaults.append([])
        for j in range(len(Es[i])):
            E_defaults[i].append('')
    line = \
       'внешний вид и кожные покровы без особенностей, видимых повреждений нет'
    E_defaults[ 4][0] = strftime('%d.%m.%Y')
    E_defaults[ 4][1] = strftime('%H:%M')
    E_defaults[ 6][0] = line
    E_defaults[ 7][0] = 'не предъявляет'
    E_defaults[ 8][1] = 'без особенностей'
    E_defaults[ 9][0] = 'в норме'
    E_defaults[ 9][1] = 'живая'
    E_defaults[ 9][2] = 'обычные'
    E_defaults[ 9][3] = 'нет'
    E_defaults[10][0] = 'речевая способность сохранена'
    E_defaults[10][1] = 'уверенная'
    E_defaults[10][2] = 'не проводилось'
    E_defaults[10][3] = 'не проводилось'
    E_defaults[11][0] = 'нет'
    E_defaults[13][0] = strftime('%H:%M')
    E_defaults[14][1] = 'моча'
    E_defaults[15][0] = 'нет'
    E_defaults[16][0] = strftime('%d.%m.%Y')
    E_defaults[16][1] = strftime('%H:%M')
    for i in range(N):
        for j in range(len(Es[i])):
            if E_defaults[i][j]:
                Es[i][j].insert(0, E_defaults[i][j])
    # Отключение полей
    Es[ 0][ 0].config(state='disabled', disabledforeground='#800000')
    Es[ 8][ 1].config(state='disabled', disabledforeground='#800000')
    Es[ 9][ 0].config(state='disabled', disabledforeground='#800000')
    Es[ 9][ 1].config(state='disabled', disabledforeground='#800000')
    Es[ 9][ 2].config(state='disabled', disabledforeground='#800000')
    Es[ 9][ 3].config(state='disabled', disabledforeground='#800000')
    Es[10][ 0].config(state='disabled', disabledforeground='#800000')
    Es[10][ 1].config(state='disabled', disabledforeground='#800000')
    Es[10][ 2].config(state='disabled', disabledforeground='#800000')
    Es[10][ 3].config(state='disabled', disabledforeground='#800000')
    Es[14][ 1].config(state='disabled', disabledforeground='#800000')
    Es[14][ 3].config(state='disabled', disabledforeground='#800000')
    Es[14][ 4].config(state='disabled', disabledforeground='#800000')
    Es[14][ 5].config(state='disabled', disabledforeground='#800000')
    Es[14][ 6].config(state='disabled', disabledforeground='#800000')
    Es[14][ 7].config(state='disabled', disabledforeground='#800000')
    Es[14][ 8].config(state='disabled', disabledforeground='#800000')
    Es[14][ 9].config(state='disabled', disabledforeground='#800000')
    Es[14][10].config(state='disabled', disabledforeground='#800000')
    Es[14][11].config(state='disabled', disabledforeground='#800000')
    Es[14][12].config(state='disabled', disabledforeground='#800000')
    Es[14][13].config(state='disabled', disabledforeground='#800000')
    Es[17][ 0].config(state='disabled', disabledforeground='#800000')
    # Обработчики событий
    #def cbKeyReleaseNum(event):
    #    n = len(event.widget.get())
    #    if n > 4: event.widget.delete(4, END)
    def cbKeyReleaseDate(event):
        n = len(event.widget.get())
        if n == 2 or n == 5: event.widget.insert(END, '.')
        if n > 10:           event.widget.delete(10, END)
    def cbKeyReleaseTime(event):
        n = len(event.widget.get())
        if n == 2: event.widget.insert(END, ':')
        if n > 5:  event.widget.delete(5, END)
    def cbKeyReleaseResult(event):
        n = len(event.widget.get())
        if n == 1: event.widget.insert(END, '.')
        if n > 4:  event.widget.delete(4, END)
    #Es[ 0][0].bind('<KeyRelease>', cbKeyReleaseNum)
    Es[ 1][1].bind('<KeyRelease>', cbKeyReleaseDate)
    Es[ 4][0].bind('<KeyRelease>', cbKeyReleaseDate)
    Es[ 4][1].bind('<KeyRelease>', cbKeyReleaseTime)
    Es[13][0].bind('<KeyRelease>', cbKeyReleaseTime)
    Es[13][1].bind('<KeyRelease>', cbKeyReleaseResult)
    Es[13][2].bind('<KeyRelease>', cbKeyReleaseTime)
    Es[13][3].bind('<KeyRelease>', cbKeyReleaseResult)
    Es[14][0].bind('<KeyRelease>', cbKeyReleaseTime)
    Es[16][0].bind('<KeyRelease>', cbKeyReleaseDate)
    Es[16][1].bind('<KeyRelease>', cbKeyReleaseTime)
    Es[17][1].bind('<KeyRelease>', cbKeyReleaseDate)
## Интерактивные надписи
def getSmartLs(LFs):
    for i in range(N):
        smart_Ls.append([])
    # Текст надписей
    lines = (
'протокол о направлении на медицинское освидетельствование',
'письменное направление работодателя',
'от медицинского освидетельствования отказался',
'состояние опьянения не установлено')
    smart_Ls[ 1].append(Label(LFs[0], text='Хабаровский край'))
    smart_Ls[ 1].append(Label(LFs[0], text='Комсомольский район'))
    smart_Ls[ 1].append(Label(LFs[0], text='г. Комсомольск-на-Амуре'))
    smart_Ls[ 1].append(Label(LFs[0], text='протокола'))
    smart_Ls[ 1].append(Label(LFs[0], text='водительского удостоверения'))
    smart_Ls[ 1].append(Label(LFs[0], text='паспорта'))
    smart_Ls[ 2].append(Label(LFs[0], text=lines[0]))
    smart_Ls[ 2].append(Label(LFs[0], text=lines[1]))
    smart_Ls[ 2].append(Label(LFs[0], text='личное заявление'))
    smart_Ls[ 8].append(Label(LFs[1], text='ясное'))
    smart_Ls[ 8].append(Label(LFs[1], text='оглушение'))
    smart_Ls[ 8].append(Label(LFs[1], text='сопор'))
    smart_Ls[ 8].append(Label(LFs[1], text='кома'))
    smart_Ls[ 8].append(Label(LFs[1], text='напряжён'))
    smart_Ls[ 8].append(Label(LFs[1], text='замкнут'))
    smart_Ls[ 8].append(Label(LFs[1], text='раздражён'))
    smart_Ls[ 8].append(Label(LFs[1], text='возбуждён'))
    smart_Ls[ 8].append(Label(LFs[1], text='агрессивен'))
    smart_Ls[ 8].append(Label(LFs[1], text='эйфоричен'))
    smart_Ls[ 8].append(Label(LFs[1], text='болтлив'))
    smart_Ls[ 8].append(Label(LFs[1], text='суетлив'))
    smart_Ls[ 8].append(Label(LFs[1], text='настроение неустойчиво'))
    smart_Ls[ 8].append(Label(LFs[1], text='сонлив'))
    smart_Ls[ 8].append(Label(LFs[1], text='заторможен'))
    smart_Ls[ 8].append(Label(LFs[1], text='ориентирован'))
    smart_Ls[ 8].append(Label(LFs[1], text='ориентация снижена'))
    smart_Ls[ 8].append(Label(LFs[1], text='дезориентирован'))
    smart_Ls[ 9].append(Label(LFs[2], text='сужены'))
    smart_Ls[ 9].append(Label(LFs[2], text='расширены'))
    smart_Ls[ 9].append(Label(LFs[2], text='вялая'))
    smart_Ls[ 9].append(Label(LFs[2], text='инъекция сосудов конъюнктивы'))
    smart_Ls[ 9].append(Label(LFs[2], text='есть'))
    smart_Ls[10].append(Label(LFs[2], text='нарушение артикуляции'))
    smart_Ls[10].append(Label(LFs[2], text='смазанность речи'))
    smart_Ls[10].append(Label(LFs[2], text='речь бессвязная'))
    smart_Ls[10].append(Label(LFs[2], text='шатающаяся'))
    smart_Ls[10].append(Label(LFs[2], text='пошатывание при поворотах'))
    smart_Ls[10].append(Label(LFs[2], text='устойчив'))
    smart_Ls[10].append(Label(LFs[2], text='неустойчив'))
    smart_Ls[10].append(Label(LFs[2], text='падает'))
    smart_Ls[10].append(Label(LFs[2], text='выполняет точно'))
    smart_Ls[10].append(Label(LFs[2], text='промахивание'))
    smart_Ls[10].append(Label(LFs[2], text='не выполняет'))
    smart_Ls[12].append(Label(LFs[2], text='отрицает'))
    smart_Ls[12].append(Label(LFs[2], text='употреблял спиртное'))
    smart_Ls[14].append(Label(LFs[3], text='кровь'))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[14].append(Label(LFs[3], text=minus))
    smart_Ls[14].append(Label(LFs[3], text=plus))
    smart_Ls[17].append(Label(LFs[3], text=lines[2]))
    smart_Ls[17].append(Label(LFs[3], text='установлено состояние опьянения'))
    smart_Ls[17].append(Label(LFs[3], text=lines[3]))
    # Размер, подчёркивание и цвет текста
    for i in range(N):
        for item in smart_Ls[i]:
            item.config(font='-size 10 -underline true', fg='#000080')
    # Реакция на указатель мыши
    def cbEnter(event):
        event.widget['font'] = '-size 10 -underline false'
    def cbLeave(event):
        event.widget['font'] = '-size 10 -underline true'
    for i in range(N):
        for item in smart_Ls[i]:
            item.bind('<Enter>', cbEnter)
            item.bind('<Leave>', cbLeave)
    # Добавление варианта
    def cbAdd(event):
        if Es[1][2].get().find(event.widget['text']) == -1:
            Es[1][2].insert(END, event.widget['text'] + ', ')
    smart_Ls[1][0].bind('<Button-1>', cbAdd)
    smart_Ls[1][1].bind('<Button-1>', cbAdd)
    smart_Ls[1][2].bind('<Button-1>', cbAdd)
    # Замена варианта
    def replace(entry, label):
        entry.delete(0, END)
        entry.insert(0, label['text'])
    def cbReplace(event):
        if event.widget == smart_Ls[1][ 3]: entry = Es[ 1][3]
        if event.widget == smart_Ls[1][ 4]: entry = Es[ 1][3]
        if event.widget == smart_Ls[1][ 5]: entry = Es[ 1][3]
        if event.widget == smart_Ls[2][ 0]: entry = Es[ 2][0]
        if event.widget == smart_Ls[2][ 1]: entry = Es[ 2][0]
        if event.widget == smart_Ls[2][ 2]: entry = Es[ 2][0]
        if event.widget == smart_Ls[8][ 0]: entry = Es[ 8][0]
        if event.widget == smart_Ls[8][ 1]: entry = Es[ 8][0]
        if event.widget == smart_Ls[8][ 2]: entry = Es[ 8][0]
        if event.widget == smart_Ls[8][ 3]: entry = Es[ 8][0]
        if event.widget == smart_Ls[8][15]: entry = Es[ 8][2]
        if event.widget == smart_Ls[8][16]: entry = Es[ 8][2]
        if event.widget == smart_Ls[8][17]: entry = Es[ 8][2]
        if event.widget == smart_Ls[12][0]: entry = Es[12][0]
        if event.widget == smart_Ls[12][1]: entry = Es[12][0]
        replace(entry, event.widget)
    def cbReplacePlus(event):
        Es[17][0].config(state='normal')
        replace(Es[17][0], event.widget)
        Es[17][0].config(state='disabled')
        if not Es[17][1].get():
            Es[17][1].insert(0, strftime('%d.%m.%Y'))
    smart_Ls[ 1][ 3].bind('<Button-1>', cbReplace)
    smart_Ls[ 1][ 4].bind('<Button-1>', cbReplace)
    smart_Ls[ 1][ 5].bind('<Button-1>', cbReplace)
    smart_Ls[ 2][ 0].bind('<Button-1>', cbReplace)
    smart_Ls[ 2][ 1].bind('<Button-1>', cbReplace)
    smart_Ls[ 2][ 2].bind('<Button-1>', cbReplace)
    smart_Ls[ 8][ 0].bind('<Button-1>', cbReplace)
    smart_Ls[ 8][ 1].bind('<Button-1>', cbReplace)
    smart_Ls[ 8][ 2].bind('<Button-1>', cbReplace)
    smart_Ls[ 8][ 3].bind('<Button-1>', cbReplace)
    smart_Ls[ 8][15].bind('<Button-1>', cbReplace)
    smart_Ls[ 8][16].bind('<Button-1>', cbReplace)
    smart_Ls[ 8][17].bind('<Button-1>', cbReplace)
    smart_Ls[12][ 0].bind('<Button-1>', cbReplace)
    smart_Ls[12][ 1].bind('<Button-1>', cbReplace)
    smart_Ls[17][ 0].bind('<Button-1>', cbReplacePlus)
    smart_Ls[17][ 1].bind('<Button-1>', cbReplacePlus)
    smart_Ls[17][ 2].bind('<Button-1>', cbReplacePlus)
    # "Умное" добавление варианта
    def smartAdd(entry, label, default):
        entry.config(state='normal')
        i = entry.get().find(label['text'])
        if entry.get() == default:
            entry.delete(0, END)
            entry.insert(0, label['text'])
        elif i == -1:
            entry.insert(END, ', ' + label['text'])
        else:
            entry.delete(i, i + len(label['text']) + 2)
        temp = entry.get().rstrip(', ')
        entry.delete(0, END)
        entry.insert(0, temp)
        if entry.get() == '':
            entry.insert(0, default)
        entry.config(state='disabled')
    def cbSmartAdd(event):
        if event.widget == smart_Ls[ 8][ 4]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][ 5]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][ 6]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][ 7]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][ 8]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][ 9]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][10]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][11]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][12]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][13]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[ 8][14]:
            entry, default = Es[ 8][1], E_defaults[ 8][1]
        if event.widget == smart_Ls[10][ 0]:
            entry, default = Es[10][0], E_defaults[10][0]
        if event.widget == smart_Ls[10][ 1]:
            entry, default = Es[10][0], E_defaults[10][0]
        if event.widget == smart_Ls[10][ 2]:
            entry, default = Es[10][0], E_defaults[10][0]
        if event.widget == smart_Ls[10][ 3]:
            entry, default = Es[10][1], E_defaults[10][1]
        if event.widget == smart_Ls[10][ 4]:
            entry, default = Es[10][1], E_defaults[10][1]
        smartAdd(entry, event.widget, default)
    smart_Ls[ 8][ 4].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][ 5].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][ 6].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][ 7].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][ 8].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][ 9].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][10].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][11].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][12].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][13].bind('<Button-1>', cbSmartAdd)
    smart_Ls[ 8][14].bind('<Button-1>', cbSmartAdd)
    smart_Ls[10][ 0].bind('<Button-1>', cbSmartAdd)
    smart_Ls[10][ 1].bind('<Button-1>', cbSmartAdd)
    smart_Ls[10][ 2].bind('<Button-1>', cbSmartAdd)
    smart_Ls[10][ 3].bind('<Button-1>', cbSmartAdd)
    smart_Ls[10][ 4].bind('<Button-1>', cbSmartAdd)
    # "Умная" замена варианта
    def smartReplace(entry, label, default):
        entry.config(state='normal')
        if entry.get() == label['text']:
            entry.delete(0, END)
            entry.insert(0, default)
        else:
            entry.delete(0, END)
            entry.insert(0, label['text'])
        entry.config(state='disabled')
    def cbSmartReplace(event):
        if event.widget == smart_Ls[ 9][ 0]:
            entry, default = Es[ 9][ 0], E_defaults[ 9][0]
        if event.widget == smart_Ls[ 9][ 1]:
            entry, default = Es[ 9][ 0], E_defaults[ 9][0]
        if event.widget == smart_Ls[ 9][ 2]:
            entry, default = Es[ 9][ 1], E_defaults[ 9][1]
        if event.widget == smart_Ls[ 9][ 3]:
            entry, default = Es[ 9][ 2], E_defaults[ 9][2]
        if event.widget == smart_Ls[ 9][ 4]:
            entry, default = Es[ 9][ 3], E_defaults[ 9][3]
        if event.widget == smart_Ls[10][ 5]:
            entry, default = Es[10][ 2], E_defaults[10][2]
        if event.widget == smart_Ls[10][ 6]:
            entry, default = Es[10][ 2], E_defaults[10][2]
        if event.widget == smart_Ls[10][ 7]:
            entry, default = Es[10][ 2], E_defaults[10][2]
        if event.widget == smart_Ls[10][ 8]:
            entry, default = Es[10][ 3], E_defaults[10][3]
        if event.widget == smart_Ls[10][ 9]:
            entry, default = Es[10][ 3], E_defaults[10][3]
        if event.widget == smart_Ls[10][10]:
            entry, default = Es[10][ 3], E_defaults[10][3]
        if event.widget == smart_Ls[14][ 0]:
            entry, default = Es[14][ 1], E_defaults[14][1]
        if event.widget == smart_Ls[14][ 1]:
            entry, default = Es[14][ 3], ''
        if event.widget == smart_Ls[14][ 2]:
            entry, default = Es[14][ 3], ''
        if event.widget == smart_Ls[14][ 3]:
            entry, default = Es[14][ 4], ''
        if event.widget == smart_Ls[14][ 4]:
            entry, default = Es[14][ 4], ''
        if event.widget == smart_Ls[14][ 5]:
            entry, default = Es[14][ 5], ''
        if event.widget == smart_Ls[14][ 6]:
            entry, default = Es[14][ 5], ''
        if event.widget == smart_Ls[14][ 7]:
            entry, default = Es[14][ 6], ''
        if event.widget == smart_Ls[14][ 8]:
            entry, default = Es[14][ 6], ''
        if event.widget == smart_Ls[14][ 9]:
            entry, default = Es[14][ 7], ''
        if event.widget == smart_Ls[14][10]:
            entry, default = Es[14][ 7], ''
        if event.widget == smart_Ls[14][11]:
            entry, default = Es[14][ 8], ''
        if event.widget == smart_Ls[14][12]:
            entry, default = Es[14][ 8], ''
        if event.widget == smart_Ls[14][13]:
            entry, default = Es[14][ 9], ''
        if event.widget == smart_Ls[14][14]:
            entry, default = Es[14][ 9], ''
        if event.widget == smart_Ls[14][15]:
            entry, default = Es[14][10], ''
        if event.widget == smart_Ls[14][16]:
            entry, default = Es[14][10], ''
        if event.widget == smart_Ls[14][17]:
            entry, default = Es[14][11], ''
        if event.widget == smart_Ls[14][18]:
            entry, default = Es[14][11], ''
        if event.widget == smart_Ls[14][19]:
            entry, default = Es[14][12], ''
        if event.widget == smart_Ls[14][20]:
            entry, default = Es[14][12], ''
        if event.widget == smart_Ls[14][21]:
            entry, default = Es[14][13], ''
        if event.widget == smart_Ls[14][22]:
            entry, default = Es[14][13], ''
        smartReplace(entry, event.widget, default)
    smart_Ls[ 9][ 0].bind('<Button-1>', cbSmartReplace)
    smart_Ls[ 9][ 1].bind('<Button-1>', cbSmartReplace)
    smart_Ls[ 9][ 2].bind('<Button-1>', cbSmartReplace)
    smart_Ls[ 9][ 3].bind('<Button-1>', cbSmartReplace)
    smart_Ls[ 9][ 4].bind('<Button-1>', cbSmartReplace)
    smart_Ls[10][ 5].bind('<Button-1>', cbSmartReplace)
    smart_Ls[10][ 6].bind('<Button-1>', cbSmartReplace)
    smart_Ls[10][ 7].bind('<Button-1>', cbSmartReplace)
    smart_Ls[10][ 8].bind('<Button-1>', cbSmartReplace)
    smart_Ls[10][ 9].bind('<Button-1>', cbSmartReplace)
    smart_Ls[10][10].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 0].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 1].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 2].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 3].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 4].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 5].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 6].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 7].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 8].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][ 9].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][10].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][11].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][12].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][13].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][14].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][15].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][16].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][17].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][18].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][19].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][20].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][21].bind('<Button-1>', cbSmartReplace)
    smart_Ls[14][22].bind('<Button-1>', cbSmartReplace)
## Выпадающие списки
def getOMs(LFs, init, cur_user):
    if cur_user == 'admin':
        user_list = list(init['Врачи'].values())
        user_list.remove('admin')
    else:
        for item in init['Врачи'].values():
            if item.find(cur_user) != -1:
                user_list = [item]
                break
    OM_notes.append(simple_Ls[ 5][ 0].cget('text'))
    OM_notes.append(simple_Ls[13][ 5].cget('text'))
    OM_notes.append(simple_Ls[13][10].cget('text'))
    OM_notes.append(simple_Ls[14][ 2].cget('text'))
    for i in [0, 3, 3, 3]:
        SVs.append(StringVar(LFs[i]))
    OMs.append(OptionMenu(LFs[0], SVs[0], *user_list))
    OMs.append(OptionMenu(LFs[3], SVs[1], *init['Технические средства']))
    OMs.append(OptionMenu(LFs[3], SVs[2], *init['Технические средства']))
    OMs.append(OptionMenu(LFs[3], SVs[3], *init['Методы']))
    OMs[0].config(width=67)
    OMs[1].config(width=47)
    OMs[2].config(width=47)
    OMs[3].config(width=47)
    for item in OMs:
        item.config(font='-size 10', fg='#800000')
    if cur_user != 'admin':
        SVs[0].set(user_list[0])
## Флажки
def getCBs(LFs):
    CB_texts = ('фальсификация выдоха',
                'отказ от сдачи пробы биологического объекта (мочи)',
                'фальсификация пробы биологического объекта (мочи)')
    for i in range(3):
        IVs.append(IntVar(LFs[3]))
    for i in range(len(CB_texts)):
        CBs.append(Checkbutton(LFs[3], variable=IVs[i]))
        CBs[i].config(text=CB_texts[i], onvalue=1, offvalue=0)

# Размещение элементов формы
def Place():
    # Подраздел "I. Паспортная часть"
    simple_Ls[ 0][ 0].place(x= 1*dX, y= 0*dY)
    simple_Ls[ 4][ 0].place(x=10*dX, y= 0*dY)
    simple_Ls[16][ 0].place(x=37*dX, y= 0*dY)
    Es       [ 0][ 0].place(x= 1*dX, y= 1*dY + 1)
    simple_Ls[ 0][ 1].place(x= 5*dX, y= 1*dY)
    simple_Ls[ 4][ 1].place(x= 9*dX, y= 1*dY)
    Es       [ 4][ 0].place(x=14*dX, y= 1*dY + 1)
    simple_Ls[ 4][ 2].place(x=24*dX, y= 1*dY)
    Es       [ 4][ 1].place(x=30*dX, y= 1*dY + 1)
    simple_Ls[16][ 1].place(x=39*dX, y= 1*dY)
    Es       [16][ 0].place(x=44*dX, y= 1*dY + 1)
    simple_Ls[16][ 2].place(x=54*dX, y= 1*dY)
    Es       [16][ 1].place(x=60*dX, y= 1*dY + 1)
    simple_Ls[ 1][ 0].place(x= 0*dX, y= 2*dY)
    simple_Ls[ 1][ 1].place(x=53*dX, y= 2*dY)
    simple_Ls[ 1][ 2].place(x= 1*dX, y= 3*dY)
    Es       [ 1][ 0].place(x=21*dX, y= 3*dY + 1)
    Es       [ 1][ 1].place(x=56*dX, y= 3*dY + 1)
    simple_Ls[ 1][ 3].place(x= 1*dX, y= 4*dY)
    smart_Ls [ 1][ 0].place(x=10*dX, y= 5*dY)
    smart_Ls [ 1][ 1].place(x=26*dX, y= 5*dY)
    smart_Ls [ 1][ 2].place(x=45*dX, y= 5*dY)
    Es       [ 1][ 2].place(x= 1*dX, y= 6*dY + 1)
    simple_Ls[ 1][ 4].place(x= 1*dX, y= 7*dY)
    smart_Ls [ 1][ 3].place(x=57*dX, y= 7*dY)
    Es       [ 1][ 3].place(x= 1*dX, y= 8*dY + 1)
    smart_Ls [ 1][ 4].place(x=34*dX, y= 8*dY)
    smart_Ls [ 1][ 5].place(x=58*dX, y= 8*dY)
    simple_Ls[ 2][ 0].place(x= 0*dX, y= 9*dY)
    smart_Ls [ 2][ 0].place(x= 1*dX, y=10*dY)
    smart_Ls [ 2][ 1].place(x= 1*dX, y=11*dY)
    smart_Ls [ 2][ 2].place(x=35*dX, y=11*dY)
    Es       [ 2][ 0].place(x= 1*dX, y=12*dY + 1)
    simple_Ls[ 2][ 1].place(x= 1*dX, y=13*dY)
    Es       [ 2][ 1].place(x=19*dX, y=13*dY + 1)
    simple_Ls[ 5][ 0].place(x= 0*dX, y=14*dY)
    OMs      [ 0]    .place(x= 1*dX, y=15*dY - 5)
    # Подраздел "II. Общие данные"
    simple_Ls[ 6][ 0].place(x= 0*dX, y= 0*dY)
    Es       [ 6][ 0].place(x= 1*dX, y= 1*dY + 1)
    simple_Ls[ 7][ 0].place(x= 0*dX, y= 2*dY)
    Es       [ 7][ 0].place(x= 1*dX, y= 3*dY + 1)
    simple_Ls[ 8][ 0].place(x= 0*dX, y= 4*dY)
    simple_Ls[ 8][ 1].place(x= 1*dX, y= 5*dY)
    Es       [ 8][ 0].place(x=18*dX, y= 5*dY + 1)
    smart_Ls [ 8][ 0].place(x=29*dX, y= 5*dY)
    smart_Ls [ 8][ 1].place(x=35*dX, y= 5*dY)
    smart_Ls [ 8][ 2].place(x=45*dX, y= 5*dY)
    smart_Ls [ 8][ 3].place(x=51*dX, y= 5*dY)
    simple_Ls[ 8][ 2].place(x= 1*dX, y= 6*dY)
    smart_Ls [ 8][ 4].place(x=11*dX, y= 6*dY)
    smart_Ls [ 8][ 5].place(x=20*dX, y= 6*dY)
    smart_Ls [ 8][ 6].place(x=27*dX, y= 6*dY)
    smart_Ls [ 8][ 7].place(x=37*dX, y= 6*dY)
    smart_Ls [ 8][ 8].place(x=47*dX, y= 6*dY)
    smart_Ls [ 8][ 9].place(x=57*dX, y= 6*dY)
    smart_Ls [ 8][10].place(x=11*dX, y= 7*dY)
    smart_Ls [ 8][11].place(x=19*dX, y= 7*dY)
    smart_Ls [ 8][12].place(x=27*dX, y= 7*dY)
    smart_Ls [ 8][13].place(x=48*dX, y= 7*dY)
    smart_Ls [ 8][14].place(x=56*dX, y= 7*dY)
    Es       [ 8][ 1].place(x= 1*dX, y= 8*dY + 1)
    simple_Ls[ 8][ 3].place(x= 1*dX, y= 9*dY)
    Es       [ 8][ 2].place(x= 1*dX, y=10*dY + 1)
    smart_Ls [ 8][15].place(x=23*dX, y=10*dY)
    smart_Ls [ 8][16].place(x=35*dX, y=10*dY)
    smart_Ls [ 8][17].place(x=52*dX, y=10*dY)
    simple_Ls[ 8][ 4].place(x= 1*dX, y=11*dY)
    Es       [ 8][ 3].place(x=21*dX, y=11*dY + 1)
    simple_Ls[ 8][ 5].place(x=24*dX, y=11*dY)
    # Подраздел "III. Объективный осмотр"
    simple_Ls[ 9][ 0].place(x= 0*dX, y= 0*dY)
    simple_Ls[ 9][ 1].place(x= 1*dX, y= 1*dY)
    Es       [ 9][ 0].place(x=15*dX, y= 1*dY + 1)
    smart_Ls [ 9][ 0].place(x=41*dX, y= 1*dY)
    smart_Ls [ 9][ 1].place(x=49*dX, y= 1*dY)
    simple_Ls[ 9][ 2].place(x= 1*dX, y= 2*dY)
    Es       [ 9][ 1].place(x=15*dX, y= 2*dY + 1)
    smart_Ls [ 9][ 2].place(x=41*dX, y= 2*dY)
    simple_Ls[ 9][ 3].place(x= 1*dX, y= 3*dY)
    Es       [ 9][ 2].place(x=15*dX, y= 3*dY + 1)
    smart_Ls [ 9][ 3].place(x=41*dX, y= 3*dY)
    simple_Ls[ 9][ 4].place(x= 1*dX, y= 4*dY)
    Es       [ 9][ 3].place(x=15*dX, y= 4*dY + 1)
    smart_Ls [ 9][ 4].place(x=41*dX, y= 4*dY)
    simple_Ls[10][ 0].place(x= 0*dX, y= 5*dY)
    simple_Ls[10][ 1].place(x= 1*dX, y= 6*dY)
    smart_Ls [10][ 0].place(x=15*dX, y= 6*dY)
    smart_Ls [10][ 1].place(x=36*dX, y= 6*dY)
    smart_Ls [10][ 2].place(x=52*dX, y= 6*dY)
    Es       [10][ 0].place(x= 1*dX, y= 7*dY + 1)
    simple_Ls[10][ 2].place(x= 1*dX, y= 8*dY)
    smart_Ls [10][ 3].place(x=31*dX, y= 8*dY)
    smart_Ls [10][ 4].place(x=43*dX, y= 8*dY)
    Es       [10][ 1].place(x= 1*dX, y= 9*dY + 1)
    simple_Ls[10][ 3].place(x= 1*dX, y=10*dY)
    Es       [10][ 2].place(x=26*dX, y=10*dY + 1)
    smart_Ls [10][ 5].place(x=41*dX, y=10*dY)
    smart_Ls [10][ 6].place(x=49*dX, y=10*dY)
    smart_Ls [10][ 7].place(x=59*dX, y=10*dY)
    simple_Ls[10][ 4].place(x= 1*dX, y=11*dY)
    Es       [10][ 3].place(x=13*dX, y=12*dY + 1)
    smart_Ls [10][ 8].place(x=28*dX, y=12*dY)
    smart_Ls [10][ 9].place(x=42*dX, y=12*dY)
    smart_Ls [10][10].place(x=54*dX, y=12*dY)
    simple_Ls[10][ 5].place(x= 1*dX, y=13*dY)
    Es       [10][ 4].place(x=21*dX, y=13*dY + 1)
    simple_Ls[10][ 6].place(x=25*dX, y=13*dY)
    simple_Ls[11][ 0].place(x= 0*dX, y=14*dY)
    simple_Ls[11][ 1].place(x= 3*dX, y=15*dY)
    Es       [11][ 0].place(x= 1*dX, y=16*dY + 1)
    simple_Ls[12][ 0].place(x= 0*dX, y=17*dY)
    simple_Ls[12][ 1].place(x= 3*dX, y=18*dY)
    Es       [12][ 0].place(x= 1*dX, y=19*dY + 1)
    smart_Ls [12][ 0].place(x=41*dX, y=19*dY)
    smart_Ls [12][ 1].place(x=49*dX, y=19*dY)
    # Подраздел "IV. Данные освидетельствования"
    simple_Ls[13][ 0].place(x= 0*dX, y= 0*dY)
    simple_Ls[13][ 1].place(x= 1*dX, y= 1*dY)
    simple_Ls[13][ 2].place(x=28*dX, y= 1*dY)
    Es       [13][ 0].place(x=34*dX, y= 1*dY + 1)
    simple_Ls[13][ 3].place(x=43*dX, y= 1*dY)
    Es       [13][ 1].place(x=52*dX, y= 1*dY + 1)
    simple_Ls[13][ 4].place(x=57*dX, y= 1*dY)
    simple_Ls[13][ 5].place(x= 1*dX, y= 2*dY)
    OMs      [ 1]    .place(x=19*dX, y= 2*dY - 5)
    CBs      [ 0]    .place(x=47*dX, y= 3*dY)
    simple_Ls[13][ 6].place(x= 1*dX, y= 4*dY)
    simple_Ls[13][ 7].place(x=28*dX, y= 4*dY)
    Es       [13][ 2].place(x=34*dX, y= 4*dY + 1)
    simple_Ls[13][ 8].place(x=43*dX, y= 4*dY)
    Es       [13][ 3].place(x=52*dX, y= 4*dY + 1)
    simple_Ls[13][ 9].place(x=57*dX, y= 4*dY)
    simple_Ls[13][10].place(x= 1*dX, y= 5*dY)
    OMs      [ 2]    .place(x=19*dX, y= 5*dY - 5)
    simple_Ls[14][ 0].place(x= 0*dX, y= 6*dY)
    Es       [14][ 0].place(x=34*dX, y= 6*dY + 1)
    simple_Ls[14][ 1].place(x=44*dX, y= 6*dY)
    Es       [14][ 1].place(x=51*dX, y= 6*dY + 1)
    smart_Ls [14][ 0].place(x=57*dX, y= 6*dY)
    CBs      [ 1]    .place(x=27*dX, y= 7*dY)
    CBs      [ 2]    .place(x=27*dX, y= 8*dY)
    simple_Ls[14][ 2].place(x= 2*dX, y= 9*dY)
    OMs      [ 3]    .place(x=19*dX, y= 9*dY - 5)
    simple_Ls[14][ 3].place(x= 1*dX, y=10*dY)
    simple_Ls[14][ 4].place(x=44*dX, y=10*dY)
    Es       [14][ 2].place(x=57*dX, y=10*dY + 1)
    simple_Ls[14][ 5].place(x=62*dX, y=10*dY)
    simple_Ls[14][ 6].place(x= 3*dX, y=11*dY)
    Es       [14][ 3].place(x=20*dX, y=11*dY + 1)
    smart_Ls [14][ 1].place(x=24*dX, y=11*dY)
    smart_Ls [14][ 2].place(x=28*dX, y=11*dY)
    simple_Ls[14][ 7].place(x=35*dX, y=11*dY)
    Es       [14][ 4].place(x=52*dX, y=11*dY + 1)
    smart_Ls [14][ 3].place(x=56*dX, y=11*dY)
    smart_Ls [14][ 4].place(x=60*dX, y=11*dY)
    simple_Ls[14][ 8].place(x= 3*dX, y=12*dY)
    Es       [14][ 5].place(x=20*dX, y=12*dY + 1)
    smart_Ls [14][ 5].place(x=24*dX, y=12*dY)
    smart_Ls [14][ 6].place(x=28*dX, y=12*dY)
    simple_Ls[14][ 9].place(x=35*dX, y=12*dY)
    Es       [14][ 6].place(x=52*dX, y=12*dY + 1)
    smart_Ls [14][ 7].place(x=56*dX, y=12*dY)
    smart_Ls [14][ 8].place(x=60*dX, y=12*dY)
    simple_Ls[14][10].place(x= 3*dX, y=13*dY)
    Es       [14][ 7].place(x=20*dX, y=13*dY + 1)
    smart_Ls [14][ 9].place(x=24*dX, y=13*dY)
    smart_Ls [14][10].place(x=28*dX, y=13*dY)
    simple_Ls[14][11].place(x=35*dX, y=13*dY)
    Es       [14][ 8].place(x=52*dX, y=13*dY + 1)
    smart_Ls [14][11].place(x=56*dX, y=13*dY)
    smart_Ls [14][12].place(x=60*dX, y=13*dY)
    simple_Ls[14][12].place(x= 3*dX, y=14*dY)
    Es       [14][ 9].place(x=20*dX, y=14*dY + 1)
    smart_Ls [14][13].place(x=24*dX, y=14*dY)
    smart_Ls [14][14].place(x=28*dX, y=14*dY)
    simple_Ls[14][13].place(x=35*dX, y=14*dY)
    Es       [14][10].place(x=52*dX, y=14*dY + 1)
    smart_Ls [14][15].place(x=56*dX, y=14*dY)
    smart_Ls [14][16].place(x=60*dX, y=14*dY)
    simple_Ls[14][14].place(x= 3*dX, y=15*dY)
    Es       [14][11].place(x=20*dX, y=15*dY + 1)
    smart_Ls [14][17].place(x=24*dX, y=15*dY)
    smart_Ls [14][18].place(x=28*dX, y=15*dY)
    simple_Ls[14][15].place(x=35*dX, y=15*dY)
    Es       [14][12].place(x=52*dX, y=15*dY + 1)
    smart_Ls [14][19].place(x=56*dX, y=15*dY)
    smart_Ls [14][20].place(x=60*dX, y=15*dY)
    simple_Ls[14][16].place(x= 3*dX, y=16*dY)
    Es       [14][13].place(x=20*dX, y=16*dY + 1)
    smart_Ls [14][21].place(x=24*dX, y=16*dY)
    smart_Ls [14][22].place(x=28*dX, y=16*dY)
    simple_Ls[15][ 0].place(x= 0*dX, y=17*dY)
    Es       [15][ 0].place(x= 1*dX, y=18*dY + 1)
    simple_Ls[17][ 0].place(x= 0*dX, y=19*dY)
    smart_Ls [17][ 0].place(x=27*dX, y=19*dY)
    smart_Ls [17][ 1].place(x= 8*dX, y=20*dY)
    smart_Ls [17][ 2].place(x=36*dX, y=20*dY)
    Es       [17][ 0].place(x= 1*dX, y=21*dY + 1)
    simple_Ls[17][ 1].place(x=41*dX, y=21*dY)
    Es       [17][ 1].place(x=46*dX, y=21*dY + 1)

# Вывод индексации списков
def WriteIndexes():
    f = open('index.txt', 'w')
    f.write('simple_Ls\n')
    for i in range(N):
        for j in range(len(simple_Ls[i])):
            f.write('%d\t%d\t%s\n' % (i, j, simple_Ls[i][j].cget('text')))
    f.write('\n')
    f.write('Es\n')
    for i in range(N):
        for j in range(len(Es[i])):
            f.write('%d\t%d\t%d\t%s\n' %
                    (i, j, Es[i][j].cget('width'), E_defaults[i][j]))
    f.write('\n')
    f.write('smart_Ls\n')
    for i in range(N):
        for j in range(len(smart_Ls[i])):
            f.write('%d\t%d\t%s\n' %
                    (i, j, smart_Ls[i][j].cget('text')))
    f.write('\n')
    f.write('OMs\n')
    for i in range(len(OMs)):
        f.write('%d\t%s\t%s\n' % (i, OMs[i].cget('width'), OM_notes[i]))
    f.write('\n')
    f.write('CBs\n')
    for i in range(len(CBs)):
        f.write('%d\t%s\n' % (i, CBs[i].cget('text')))
    f.close()

# Работа с элементаци формы
## Проверка данных формы
def need():
    for i in range(11):
        if Es[14][i + 3].get():
            return True
    return False
def Check():
    temp = True
    # I. Паспортная часть
    if Es[0][0].get():
        if not Es[0][0].get().isnumeric():
            PopupTag(simple_Ls, 'format', (0, 0))
            temp = False
    else:
        PopupTag(simple_Ls, 'enter', (0, 0))
        temp = False
    if not Es[1][0].get():
        PopupTag(simple_Ls, 'enter', (1, 0), (1, 2))
        temp = False
    if Es[4][0].get():
        try: strptime(Es[4][0].get(), '%d.%m.%Y')
        except:
            PopupTag(simple_Ls, 'format', (4, 0), (4, 1))
            temp = False
    else:
        PopupTag(simple_Ls, 'enter', (4, 0), (4, 1))
        temp = False
    if Es[4][1].get():
        try: strptime(Es[4][1].get(), '%H:%M')
        except:
            PopupTag(simple_Ls, 'format', (4, 0), (4, 2))
            temp = False
    else:
        PopupTag(simple_Ls, 'enter', (4, 0), (4, 2))
        temp = False
    if Es[16][0].get():
        try: strptime(Es[16][0].get(), '%d.%m.%Y')
        except:
            PopupTag(simple_Ls, 'format', (16, 0), (16, 1))
            temp = False
    else:
        PopupTag(simple_Ls, 'enter', (16, 0), (16, 1))
        temp = False
    if Es[16][1].get():
        try: strptime(Es[16][1].get(), '%H:%M')
        except:
            PopupTag(simple_Ls, 'format', (16, 0), (16, 2))
            temp = False
    else:
        PopupTag(simple_Ls, 'enter', (16, 0), (16, 2))
        temp = False
    if Es[1][1].get():
        try: strptime(Es[1][1].get(), '%d.%m.%Y')
        except:
            PopupTag(simple_Ls, 'format', (1, 0), (1, 1))
            temp = False
    if not SVs[0].get():
        PopupTag(simple_Ls, 'select', (5, 0))
        temp = False
    # IV. Данные освидетельствования
    if not IVs[0].get():
        if Es[13][1].get():
            try:
                float(Es[13][1].get())
            except:
                PopupTag(simple_Ls, 'format', (13, 1), (13, 3))
                temp = False
            if Es[13][0].get():
                try:
                    strptime(Es[13][0].get(), '%H:%M')
                except:
                    PopupTag(simple_Ls, 'format', (13, 1), (13, 2))
                    temp = False
            else:
                PopupTag(simple_Ls, 'enter', (13, 1), (13, 2))
                temp = False
            if not SVs[1].get():
                PopupTag(simple_Ls, 'select', (13, 1), (13, 5))
                temp = False
        if Es[13][3].get():
            try:
                float(Es[13][3].get())
            except:
                PopupTag(simple_Ls, 'format', (13, 6), (13, 8))
                temp = False
            if Es[13][2].get():
                try:
                    strptime(Es[13][2].get(), '%H:%M')
                except:
                    PopupTag(simple_Ls, 'format', (13, 6), (13, 7))
                    temp = False
            else:
                PopupTag(simple_Ls, 'enter', (13, 6), (13, 7))
                temp = False
            if not SVs[2].get():
                PopupTag(simple_Ls, 'select', (13, 6), (13, 10))
                temp = False
    if Es[14][0].get():
        try: strptime(Es[14][0].get(), '%H:%M')
        except:
            PopupTag(simple_Ls, 'format', (14, 0))
            temp = False
        if not SVs[3].get():
            PopupTag(simple_Ls, 'enter', (14, 0), (14, 2))
            temp = False
        if not Es[14][2].get() and need():
            PopupTag(simple_Ls, 'enter', (14, 0), (14, 4))
            temp = False
    if Es[17][1].get():
        try: strptime(Es[17][1].get(), '%d.%m.%Y')
        except:
            PopupTag(simple_Ls, 'format', (17, 0), (17, 1))
            temp = False
    elif Es[17][0].get():
        PopupTag(simple_Ls, 'enter', (17, 0), (17, 1))
        temp = False
    # Последовательность событий
    try:
        temp1 = strptime(Es[ 4][0].get() + Es[ 4][1].get(), '%d.%m.%Y%H:%M')
        temp2 = strptime(Es[16][0].get() + Es[16][1].get(), '%d.%m.%Y%H:%M')
        if not temp1 < temp2:
            PopupTag(simple_Ls, 'ratio', (4, 0), (16, 0))
            temp = False
    except: pass
    try:
        temp2 = strptime(Es[16][1].get(), '%H:%M')
        if Es[13][1].get() and not Es[13][3].get():
            temp1 = strptime(Es[13][0].get(), '%H:%M')
            temp3 = temp1.tm_hour + temp1.tm_min/60
            temp4 = temp2.tm_hour + temp2.tm_min/60
            if temp1 > temp2 and temp3 - temp4 < 23:
                PopupTag(simple_Ls, 'ratio', (13, 1), (16, 0))
                temp = False
        if Es[13][3].get():
            temp1 = strptime(Es[13][2].get(), '%H:%M')
            temp3 = temp1.tm_hour + temp1.tm_min/60
            temp4 = temp2.tm_hour + temp2.tm_min/60
            if temp1 > temp2 and temp3 - temp4 < 23:
                PopupTag(simple_Ls, 'ratio', (13, 6), (16, 0))
                temp = False
    except: pass
    try:
        temp1 = strptime(Es[13][0].get(), '%H:%M')
        temp2 = strptime(Es[13][2].get(), '%H:%M')
        temp3 = temp1.tm_hour*60 + temp1.tm_min
        temp4 = temp2.tm_hour*60 + temp2.tm_min
        if ((temp4 - temp3 < 15 or temp4 - temp3 > 20) and
            (temp4 - temp3 + 1440 < 15 or temp4 - temp3 + 1440 > 20)):
            PopupTag(simple_Ls, 'ratio', (13, 1), (13, 6))
            temp = False
    except: pass
    return temp
## Чтение данных из формы
def getDataLines():
    lines = []
    for i in range(58):
        lines.append('')
    lines[ 0] =        Es[ 0][ 0].get()
    lines[ 1] = simple_Ls[ 0][ 1]['text']
    lines[ 2] =        Es[ 1][ 0].get()
    lines[ 3] =        Es[ 1][ 1].get()
    lines[ 4] =        Es[ 1][ 2].get()
    lines[ 5] =        Es[ 1][ 3].get()
    lines[ 6] =        Es[ 2][ 0].get()
    lines[ 7] =        Es[ 2][ 1].get()
    lines[ 8] =        Es[ 4][ 0].get()
    lines[ 9] =        Es[ 4][ 1].get()
    lines[10] =           SVs[ 0].get()
    lines[11] =        Es[ 6][ 0].get()
    lines[12] =        Es[ 7][ 0].get()
    lines[13] =        Es[ 8][ 0].get()
    lines[14] =        Es[ 8][ 1].get()
    lines[15] =        Es[ 8][ 2].get()
    lines[16] =        Es[ 8][ 3].get()
    lines[17] =        Es[ 9][ 0].get()
    lines[18] =        Es[ 9][ 1].get()
    lines[19] =        Es[ 9][ 2].get()
    lines[20] =        Es[ 9][ 3].get()
    lines[21] =        Es[10][ 0].get()
    lines[22] =        Es[10][ 1].get()
    lines[23] =        Es[10][ 2].get()
    lines[24] =        Es[10][ 3].get()
    lines[25] =        Es[10][ 4].get()
    lines[26] =        Es[11][ 0].get()
    lines[27] =        Es[12][ 0].get()
    lines[28] =        Es[13][ 0].get()
    lines[29] =        Es[13][ 1].get()
    lines[30] =           SVs[ 1].get()
    lines[31] =       str(IVs[ 0].get())
    lines[32] =        Es[13][ 2].get()
    lines[33] =        Es[13][ 3].get()
    lines[34] =           SVs[ 2].get()
    lines[35] =        Es[14][ 0].get()
    lines[36] =        Es[14][ 1].get()
    lines[37] =       str(IVs[ 1].get())
    lines[38] =       str(IVs[ 2].get())
    lines[39] =           SVs[ 3].get()
    lines[40] =        Es[14][ 2].get()
    lines[41] = simple_Ls[14][ 5]['text']
    # Вещества
    for i in range(42, 53):
        if Es[14][i - 39].get():
            lines[i] = simple_Ls[14][i - 36].cget('text') +\
                       ':' + Es[14][i - 39].get()
    #
    lines[53] =        Es[15][ 0].get()
    lines[54] =        Es[16][ 0].get()
    lines[55] =        Es[16][ 1].get()
    lines[56] =        Es[17][ 0].get()
    lines[57] =        Es[17][ 1].get()
    return lines
## Запись данных в форму
def setLine(entry, line):
    temp = entry.cget('state') == 'disabled'
    if temp:
        entry.config(state='normal')
    entry.delete(0, END)
    entry.insert(0, line)
    if temp:
        entry.config(state='disabled')
def setDataLines(lines):
    setLine(Es[ 0][ 0],          lines[ 0])
    simple_Ls [ 0][ 1]['text'] = lines[ 1]
    setLine(Es[ 1][ 0],          lines[ 2])
    setLine(Es[ 1][ 1],          lines[ 3])
    setLine(Es[ 1][ 2],          lines[ 4])
    setLine(Es[ 1][ 3],          lines[ 5])
    setLine(Es[ 2][ 0],          lines[ 6])
    setLine(Es[ 2][ 1],          lines[ 7])
    setLine(Es[ 4][ 0],          lines[ 8])
    setLine(Es[ 4][ 1],          lines[ 9])
    SVs[0].set(                  lines[10])
    setLine(Es[ 6][ 0],          lines[11])
    setLine(Es[ 7][ 0],          lines[12])
    setLine(Es[ 8][ 0],          lines[13])
    setLine(Es[ 8][ 1],          lines[14])
    setLine(Es[ 8][ 2],          lines[15])
    setLine(Es[ 8][ 3],          lines[16])
    setLine(Es[ 9][ 0],          lines[17])
    setLine(Es[ 9][ 1],          lines[18])
    setLine(Es[ 9][ 2],          lines[19])
    setLine(Es[ 9][ 3],          lines[20])
    setLine(Es[10][ 0],          lines[21])
    setLine(Es[10][ 1],          lines[22])
    setLine(Es[10][ 2],          lines[23])
    setLine(Es[10][ 3],          lines[24])
    setLine(Es[10][ 4],          lines[25])
    setLine(Es[11][ 0],          lines[26])
    setLine(Es[12][ 0],          lines[27])
    setLine(Es[13][ 0],          lines[28])
    setLine(Es[13][ 1],          lines[29])
    SVs[1].set(                  lines[30])
    IVs[0].set(                  lines[31])
    setLine(Es[13][ 2],          lines[32])
    setLine(Es[13][ 3],          lines[33])
    SVs[2].set(                  lines[34])
    setLine(Es[14][ 0],          lines[35])
    setLine(Es[14][ 1],          lines[36])
    IVs[1].set(                  lines[37])
    IVs[2].set(                  lines[38])
    SVs[3].set(                  lines[39])
    setLine(Es[14][ 2],          lines[40])
    simple_Ls [14][ 5]['text'] = lines[41]
    # Вещества
    for i in range(42, 53):
        if lines[i]:
            simple_Ls [14][i - 36].config(text=lines[i].split(':')[0])
            setLine(Es[14][i - 39],            lines[i].split(':')[1])
        else:
            setLine(Es[14][i - 39], '')
    #
    setLine(Es[15][ 0],          lines[53])
    setLine(Es[16][ 0],          lines[54])
    setLine(Es[16][ 1],          lines[55])
    setLine(Es[17][ 0],          lines[56])
    setLine(Es[17][ 1],          lines[57])
## Подготовка данных к печати
def getMonth(n):
    if n ==  1: return 'января'
    if n ==  2: return 'февраля'
    if n ==  3: return 'марта'
    if n ==  4: return 'апреля'
    if n ==  5: return 'мая'
    if n ==  6: return 'июня'
    if n ==  7: return 'июля'
    if n ==  8: return 'августа'
    if n ==  9: return 'сентября'
    if n == 10: return 'октября'
    if n == 11: return 'ноября'
    if n == 12: return 'декабря'
def getDateLine(line):
    t = strptime(line, '%d.%m.%Y')
    return '%d %s %d г.' % (t.tm_mday, getMonth(t.tm_mon), t.tm_year)
def getLineMP(entry):
    if entry.get() == minus: return 'отрицательный'
    if entry.get() == plus:  return 'положительный'
def getPrintData(init):
    data = []
    for i in range(19):
        data.append([])
    data[0].append(init['Организация'])
    data[0].append(Es[0][0].get() + simple_Ls[0][1]['text'])
    data[0].append(getDateLine(Es[4][0].get()))
    data[1].append(Es[1][0].get())
    data[1].append(Es[1][1].get())
    data[1].append(Es[1][2].get())
    data[1].append(Es[1][3].get())
    data[2].append(Es[2][0].get())
    data[2].append(Es[2][1].get())
    data[3].append(init['Подразделение'])
    data[4].append(Es[4][0].get() + ' ' + Es[4][1].get())
    data[5].append(SVs[0].get().partition(', ')[0])
    data[5].append(SVs[0].get().partition(', ')[2])
    data[6].append(Es[6][0].get())
    data[7].append(Es[7][0].get())
    data[8].append(Es[8][0].get())
    data[8].append(Es[8][1].get())
    data[8].append(Es[8][2].get())
    if Es[8][3].get():
        data[8].append(Es[8][3].get() + ' ' + simple_Ls[8][5]['text'])
    else:
        data[8].append('не проводилось')
    data[9].append(Es[9][0].get())
    data[9].append(Es[9][1].get())
    data[9].append(Es[9][2].get())
    data[9].append(Es[9][3].get())
    data[10].append(Es[10][0].get())
    data[10].append(Es[10][1].get())
    data[10].append(Es[10][2].get())
    data[10].append(Es[10][3].get())
    if Es[10][4].get():
        data[10].append(Es[10][4].get() + ' ' + simple_Ls[10][6]['text'])
    else:
        data[10].append('не проводилось')
    data[11].append(Es[11][0].get())
    data[12].append(Es[12][0].get())
    if Es[13][1].get():
        data[13].append('%s, %s, %s %s' % (Es[13][0].get(), SVs[1].get(),
                        Es[13][1].get(), simple_Ls[13][4]['text']))
    else:
        data[13].append('не проводилось')
    if Es[13][3].get():
        data[13].append('%s, %s, %s %s' % (Es[13][2].get(), SVs[2].get(),
                        Es[13][3].get(), simple_Ls[13][9]['text']))
    else:
        if Es[13][1].get() and float(Es[13][1].get()) <= 0.16:
            data[13].append('''не проводилось в связи с
                отрицательным результатом первого исследования''')
        else: data[13].append('не проводилось')
    if IVs[0].get():
        data[13][0] = CBs[0]['text']
        data[13][1] = 'не проводилось'
    if Es[14][0].get():
        data[14].append('%s (%s)' % (Es[14][0].get(), Es[14][1].get()))
        data[14].append(init['Лаборатория'] + ', ' + SVs[3].get())
        for i in range(3, 13):
            if Es[14][i].get():
                data[14][1] += ', %s: %s' % (simple_Ls[14][i + 3]['text'],
                                             getLineMP(Es[14][i]))
        data[14][1] += ', № ' + Es[14][2].get() + simple_Ls[14][5]['text']
    else:
        data[14].append('''забор биологического объекта для
            химико-токсикологических исследований не осуществлялся''')
        data[14].append('нет')
    if IVs[1].get():
        data[14][0] = CBs[1]['text']
        data[14][1] = 'нет'
    if IVs[2].get():
        data[14][0] = CBs[2]['text']
        data[14][1] = 'нет'
    data[15].append(Es[15][0].get())
    data[16].append(Es[16][0].get() + ' ' + Es[16][1].get())
    data[17].append(Es[17][0].get())
    data[17].append(Es[17][1].get())
    data[18].append(SVs[0].get().partition(',')[0])
    return data

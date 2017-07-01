from data import get_entries_data, get_simple_labels_data
from events import bind_entries_events
from popup import popup_tag
from time import strftime, strptime
from tkinter import (Checkbutton, END, Entry, IntVar,
                     Label, OptionMenu, StringVar)


form_length = 18
simple_labels = []
entries = []
entries_default = []
smart_labels = []
minus = '«-»'
plus = '«+»'


def init_simple_labels(label_frames, init):

    for i in range(form_length):
        simple_labels.append([])

    for item in get_simple_labels_data(init['Вещества']):
        simple_labels[item[0]].append(
            Label(label_frames[item[1]], text=item[2]))

    for i_item in simple_labels:
        for j_item in i_item:
            j_item.config(font='-size 10')


def init_entries(label_frames):

    ed = get_entries_data()
    entries_state = []

    for i in range(form_length):
        entries.append([])
        entries_default.append([])
        entries_state.append([])

    for item in ed:
        entries[item[0]].append(
            Entry(label_frames[item[1]], width=item[2],
                  font='-size 10', fg='#800000'))
        entries_default[item[0]].append(item[4])
        entries_state[item[0]].append(item[3])

    for i in range(form_length):
        for j in range(len(entries[i])):
            entries[i][j].insert(0, entries_default[i][j])
            if not entries_state[i][j]:
                entries[i][j].config(state='disabled', disabledforeground='#800000')

    bind_entries_events(entries)


def getSmartLs(label_frames):   # ЗАКЛАДКА
    for i in range(form_length):
        smart_labels.append([])
    # Текст надписей
    lines = (
'протокол о направлении на медицинское освидетельствование',
'письменное направление работодателя',
'от медицинского освидетельствования отказался',
'состояние опьянения не установлено')
    smart_labels[ 1].append(Label(label_frames[0], text='Хабаровский край'))
    smart_labels[ 1].append(Label(label_frames[0], text='Комсомольский район'))
    smart_labels[ 1].append(Label(label_frames[0], text='г. Комсомольск-на-Амуре'))
    smart_labels[ 1].append(Label(label_frames[0], text='протокола'))
    smart_labels[ 1].append(Label(label_frames[0], text='водительского удостоверения'))
    smart_labels[ 1].append(Label(label_frames[0], text='паспорта'))
    smart_labels[ 2].append(Label(label_frames[0], text=lines[0]))
    smart_labels[ 2].append(Label(label_frames[0], text=lines[1]))
    smart_labels[ 2].append(Label(label_frames[0], text='личное заявление'))
    smart_labels[ 8].append(Label(label_frames[1], text='ясное'))
    smart_labels[ 8].append(Label(label_frames[1], text='оглушение'))
    smart_labels[ 8].append(Label(label_frames[1], text='сопор'))
    smart_labels[ 8].append(Label(label_frames[1], text='кома'))
    smart_labels[ 8].append(Label(label_frames[1], text='напряжён'))
    smart_labels[ 8].append(Label(label_frames[1], text='замкнут'))
    smart_labels[ 8].append(Label(label_frames[1], text='раздражён'))
    smart_labels[ 8].append(Label(label_frames[1], text='возбуждён'))
    smart_labels[ 8].append(Label(label_frames[1], text='агрессивен'))
    smart_labels[ 8].append(Label(label_frames[1], text='эйфоричен'))
    smart_labels[ 8].append(Label(label_frames[1], text='болтлив'))
    smart_labels[ 8].append(Label(label_frames[1], text='суетлив'))
    smart_labels[ 8].append(Label(label_frames[1], text='настроение неустойчиво'))
    smart_labels[ 8].append(Label(label_frames[1], text='сонлив'))
    smart_labels[ 8].append(Label(label_frames[1], text='заторможен'))
    smart_labels[ 8].append(Label(label_frames[1], text='ориентирован'))
    smart_labels[ 8].append(Label(label_frames[1], text='ориентация снижена'))
    smart_labels[ 8].append(Label(label_frames[1], text='дезориентирован'))
    smart_labels[ 9].append(Label(label_frames[2], text='сужены'))
    smart_labels[ 9].append(Label(label_frames[2], text='расширены'))
    smart_labels[ 9].append(Label(label_frames[2], text='вялая'))
    smart_labels[ 9].append(Label(label_frames[2], text='инъекция сосудов конъюнктивы'))
    smart_labels[ 9].append(Label(label_frames[2], text='есть'))
    smart_labels[10].append(Label(label_frames[2], text='нарушение артикуляции'))
    smart_labels[10].append(Label(label_frames[2], text='смазанность речи'))
    smart_labels[10].append(Label(label_frames[2], text='речь бессвязная'))
    smart_labels[10].append(Label(label_frames[2], text='шатающаяся'))
    smart_labels[10].append(Label(label_frames[2], text='пошатывание при поворотах'))
    smart_labels[10].append(Label(label_frames[2], text='устойчив'))
    smart_labels[10].append(Label(label_frames[2], text='неустойчив'))
    smart_labels[10].append(Label(label_frames[2], text='падает'))
    smart_labels[10].append(Label(label_frames[2], text='выполняет точно'))
    smart_labels[10].append(Label(label_frames[2], text='промахивание'))
    smart_labels[10].append(Label(label_frames[2], text='не выполняет'))
    smart_labels[12].append(Label(label_frames[2], text='отрицает'))
    smart_labels[12].append(Label(label_frames[2], text='употреблял спиртное'))
    smart_labels[14].append(Label(label_frames[3], text='кровь'))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[14].append(Label(label_frames[3], text=minus))
    smart_labels[14].append(Label(label_frames[3], text=plus))
    smart_labels[17].append(Label(label_frames[3], text=lines[2]))
    smart_labels[17].append(Label(label_frames[3], text='установлено состояние опьянения'))
    smart_labels[17].append(Label(label_frames[3], text=lines[3]))
    # Размер, подчёркивание и цвет текста
    for i in range(form_length):
        for item in smart_labels[i]:
            item.config(font='-size 10 -underline true', fg='#000080')
    # Реакция на указатель мыши
    def cbEnter(event):
        event.widget['font'] = '-size 10 -underline false'
    def cbLeave(event):
        event.widget['font'] = '-size 10 -underline true'
    for i in range(form_length):
        for item in smart_labels[i]:
            item.bind('<Enter>', cbEnter)
            item.bind('<Leave>', cbLeave)
    # Добавление варианта
    def cbAdd(event):
        if entries[1][2].get().find(event.widget['text']) == -1:
            entries[1][2].insert(END, event.widget['text'] + ', ')
    smart_labels[1][0].bind('<Button-1>', cbAdd)
    smart_labels[1][1].bind('<Button-1>', cbAdd)
    smart_labels[1][2].bind('<Button-1>', cbAdd)
    # Замена варианта
    def replace(entry, label):
        entry.delete(0, END)
        entry.insert(0, label['text'])
    def cbReplace(event):
        if event.widget == smart_labels[1][ 3]: entry = entries[ 1][3]
        if event.widget == smart_labels[1][ 4]: entry = entries[ 1][3]
        if event.widget == smart_labels[1][ 5]: entry = entries[ 1][3]
        if event.widget == smart_labels[2][ 0]: entry = entries[ 2][0]
        if event.widget == smart_labels[2][ 1]: entry = entries[ 2][0]
        if event.widget == smart_labels[2][ 2]: entry = entries[ 2][0]
        if event.widget == smart_labels[8][ 0]: entry = entries[ 8][0]
        if event.widget == smart_labels[8][ 1]: entry = entries[ 8][0]
        if event.widget == smart_labels[8][ 2]: entry = entries[ 8][0]
        if event.widget == smart_labels[8][ 3]: entry = entries[ 8][0]
        if event.widget == smart_labels[8][15]: entry = entries[ 8][2]
        if event.widget == smart_labels[8][16]: entry = entries[ 8][2]
        if event.widget == smart_labels[8][17]: entry = entries[ 8][2]
        if event.widget == smart_labels[12][0]: entry = entries[12][0]
        if event.widget == smart_labels[12][1]: entry = entries[12][0]
        replace(entry, event.widget)
    def cbReplacePlus(event):
        entries[17][0].config(state='normal')
        replace(entries[17][0], event.widget)
        entries[17][0].config(state='disabled')
        if not entries[17][1].get():
            entries[17][1].insert(0, strftime('%d.%m.%Y'))
    smart_labels[ 1][ 3].bind('<Button-1>', cbReplace)
    smart_labels[ 1][ 4].bind('<Button-1>', cbReplace)
    smart_labels[ 1][ 5].bind('<Button-1>', cbReplace)
    smart_labels[ 2][ 0].bind('<Button-1>', cbReplace)
    smart_labels[ 2][ 1].bind('<Button-1>', cbReplace)
    smart_labels[ 2][ 2].bind('<Button-1>', cbReplace)
    smart_labels[ 8][ 0].bind('<Button-1>', cbReplace)
    smart_labels[ 8][ 1].bind('<Button-1>', cbReplace)
    smart_labels[ 8][ 2].bind('<Button-1>', cbReplace)
    smart_labels[ 8][ 3].bind('<Button-1>', cbReplace)
    smart_labels[ 8][15].bind('<Button-1>', cbReplace)
    smart_labels[ 8][16].bind('<Button-1>', cbReplace)
    smart_labels[ 8][17].bind('<Button-1>', cbReplace)
    smart_labels[12][ 0].bind('<Button-1>', cbReplace)
    smart_labels[12][ 1].bind('<Button-1>', cbReplace)
    smart_labels[17][ 0].bind('<Button-1>', cbReplacePlus)
    smart_labels[17][ 1].bind('<Button-1>', cbReplacePlus)
    smart_labels[17][ 2].bind('<Button-1>', cbReplacePlus)
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
        if event.widget == smart_labels[ 8][ 4]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][ 5]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][ 6]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][ 7]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][ 8]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][ 9]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][10]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][11]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][12]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][13]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[ 8][14]:
            entry, default = entries[ 8][1], entries_default[ 8][1]
        if event.widget == smart_labels[10][ 0]:
            entry, default = entries[10][0], entries_default[10][0]
        if event.widget == smart_labels[10][ 1]:
            entry, default = entries[10][0], entries_default[10][0]
        if event.widget == smart_labels[10][ 2]:
            entry, default = entries[10][0], entries_default[10][0]
        if event.widget == smart_labels[10][ 3]:
            entry, default = entries[10][1], entries_default[10][1]
        if event.widget == smart_labels[10][ 4]:
            entry, default = entries[10][1], entries_default[10][1]
        smartAdd(entry, event.widget, default)
    smart_labels[ 8][ 4].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][ 5].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][ 6].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][ 7].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][ 8].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][ 9].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][10].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][11].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][12].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][13].bind('<Button-1>', cbSmartAdd)
    smart_labels[ 8][14].bind('<Button-1>', cbSmartAdd)
    smart_labels[10][ 0].bind('<Button-1>', cbSmartAdd)
    smart_labels[10][ 1].bind('<Button-1>', cbSmartAdd)
    smart_labels[10][ 2].bind('<Button-1>', cbSmartAdd)
    smart_labels[10][ 3].bind('<Button-1>', cbSmartAdd)
    smart_labels[10][ 4].bind('<Button-1>', cbSmartAdd)
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
        if event.widget == smart_labels[ 9][ 0]:
            entry, default = entries[ 9][ 0], entries_default[ 9][0]
        if event.widget == smart_labels[ 9][ 1]:
            entry, default = entries[ 9][ 0], entries_default[ 9][0]
        if event.widget == smart_labels[ 9][ 2]:
            entry, default = entries[ 9][ 1], entries_default[ 9][1]
        if event.widget == smart_labels[ 9][ 3]:
            entry, default = entries[ 9][ 2], entries_default[ 9][2]
        if event.widget == smart_labels[ 9][ 4]:
            entry, default = entries[ 9][ 3], entries_default[ 9][3]
        if event.widget == smart_labels[10][ 5]:
            entry, default = entries[10][ 2], entries_default[10][2]
        if event.widget == smart_labels[10][ 6]:
            entry, default = entries[10][ 2], entries_default[10][2]
        if event.widget == smart_labels[10][ 7]:
            entry, default = entries[10][ 2], entries_default[10][2]
        if event.widget == smart_labels[10][ 8]:
            entry, default = entries[10][ 3], entries_default[10][3]
        if event.widget == smart_labels[10][ 9]:
            entry, default = entries[10][ 3], entries_default[10][3]
        if event.widget == smart_labels[10][10]:
            entry, default = entries[10][ 3], entries_default[10][3]
        if event.widget == smart_labels[14][ 0]:
            entry, default = entries[14][ 1], entries_default[14][1]
        if event.widget == smart_labels[14][ 1]:
            entry, default = entries[14][ 3], ''
        if event.widget == smart_labels[14][ 2]:
            entry, default = entries[14][ 3], ''
        if event.widget == smart_labels[14][ 3]:
            entry, default = entries[14][ 4], ''
        if event.widget == smart_labels[14][ 4]:
            entry, default = entries[14][ 4], ''
        if event.widget == smart_labels[14][ 5]:
            entry, default = entries[14][ 5], ''
        if event.widget == smart_labels[14][ 6]:
            entry, default = entries[14][ 5], ''
        if event.widget == smart_labels[14][ 7]:
            entry, default = entries[14][ 6], ''
        if event.widget == smart_labels[14][ 8]:
            entry, default = entries[14][ 6], ''
        if event.widget == smart_labels[14][ 9]:
            entry, default = entries[14][ 7], ''
        if event.widget == smart_labels[14][10]:
            entry, default = entries[14][ 7], ''
        if event.widget == smart_labels[14][11]:
            entry, default = entries[14][ 8], ''
        if event.widget == smart_labels[14][12]:
            entry, default = entries[14][ 8], ''
        if event.widget == smart_labels[14][13]:
            entry, default = entries[14][ 9], ''
        if event.widget == smart_labels[14][14]:
            entry, default = entries[14][ 9], ''
        if event.widget == smart_labels[14][15]:
            entry, default = entries[14][10], ''
        if event.widget == smart_labels[14][16]:
            entry, default = entries[14][10], ''
        if event.widget == smart_labels[14][17]:
            entry, default = entries[14][11], ''
        if event.widget == smart_labels[14][18]:
            entry, default = entries[14][11], ''
        if event.widget == smart_labels[14][19]:
            entry, default = entries[14][12], ''
        if event.widget == smart_labels[14][20]:
            entry, default = entries[14][12], ''
        if event.widget == smart_labels[14][21]:
            entry, default = entries[14][13], ''
        if event.widget == smart_labels[14][22]:
            entry, default = entries[14][13], ''
        smartReplace(entry, event.widget, default)
    smart_labels[ 9][ 0].bind('<Button-1>', cbSmartReplace)
    smart_labels[ 9][ 1].bind('<Button-1>', cbSmartReplace)
    smart_labels[ 9][ 2].bind('<Button-1>', cbSmartReplace)
    smart_labels[ 9][ 3].bind('<Button-1>', cbSmartReplace)
    smart_labels[ 9][ 4].bind('<Button-1>', cbSmartReplace)
    smart_labels[10][ 5].bind('<Button-1>', cbSmartReplace)
    smart_labels[10][ 6].bind('<Button-1>', cbSmartReplace)
    smart_labels[10][ 7].bind('<Button-1>', cbSmartReplace)
    smart_labels[10][ 8].bind('<Button-1>', cbSmartReplace)
    smart_labels[10][ 9].bind('<Button-1>', cbSmartReplace)
    smart_labels[10][10].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 0].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 1].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 2].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 3].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 4].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 5].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 6].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 7].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 8].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][ 9].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][10].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][11].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][12].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][13].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][14].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][15].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][16].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][17].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][18].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][19].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][20].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][21].bind('<Button-1>', cbSmartReplace)
    smart_labels[14][22].bind('<Button-1>', cbSmartReplace)


# Создание выпадающих списков.
string_vars = []
option_menus = []
option_menus_note = []


def getOMs(label_frames, init, cur_user):
    if cur_user == 'admin':
        user_list = list(init['Врачи'].values())
        user_list.remove('admin')
    else:
        for item in init['Врачи'].values():
            if item.find(cur_user) != -1:
                user_list = [item]
                break
    option_menus_note.append(simple_labels[ 5][ 0].cget('text'))
    option_menus_note.append(simple_labels[13][ 5].cget('text'))
    option_menus_note.append(simple_labels[13][10].cget('text'))
    option_menus_note.append(simple_labels[14][ 2].cget('text'))
    for i in [0, 3, 3, 3]:
        string_vars.append(StringVar(label_frames[i]))
    option_menus.append(OptionMenu(label_frames[0], string_vars[0], *user_list))
    option_menus.append(OptionMenu(label_frames[3], string_vars[1], *init['Технические средства']))
    option_menus.append(OptionMenu(label_frames[3], string_vars[2], *init['Технические средства']))
    option_menus.append(OptionMenu(label_frames[3], string_vars[3], *init['Методы']))
    option_menus[0].config(width=67)
    option_menus[1].config(width=47)
    option_menus[2].config(width=47)
    option_menus[3].config(width=47)
    for item in option_menus:
        item.config(font='-size 10', fg='#800000')
    if cur_user != 'admin':
        string_vars[0].set(user_list[0])


# Создание флажков.
checkbuttons_text = []
int_vars = []
checkbuttons = []


def getCBs(label_frames):
    CB_texts = ('фальсификация выдоха',
                'отказ от сдачи пробы биологического объекта (мочи)',
                'фальсификация пробы биологического объекта (мочи)')
    for i in range(3):
        int_vars.append(IntVar(label_frames[3]))
    for i in range(len(CB_texts)):
        checkbuttons.append(Checkbutton(label_frames[3], variable=int_vars[i]))
        checkbuttons[i].config(text=CB_texts[i], onvalue=1, offvalue=0)


# Размещение элементов формы.
dX = 8      # шаг сетки по X
dY = 28     # шаг сетки по Y
def Place():
    # Подраздел "I. Паспортная часть"
    simple_labels[ 0][ 0].place(x= 1*dX, y= 0*dY)
    simple_labels[ 4][ 0].place(x=10*dX, y= 0*dY)
    simple_labels[16][ 0].place(x=37*dX, y= 0*dY)
    entries       [ 0][ 0].place(x=1 * dX, y=1 * dY + 1)
    simple_labels[ 0][ 1].place(x= 5*dX, y= 1*dY)
    simple_labels[ 4][ 1].place(x= 9*dX, y= 1*dY)
    entries       [ 4][ 0].place(x=14 * dX, y=1 * dY + 1)
    simple_labels[ 4][ 2].place(x=24*dX, y= 1*dY)
    entries       [ 4][ 1].place(x=30 * dX, y=1 * dY + 1)
    simple_labels[16][ 1].place(x=39*dX, y= 1*dY)
    entries       [16][ 0].place(x=44 * dX, y=1 * dY + 1)
    simple_labels[16][ 2].place(x=54*dX, y= 1*dY)
    entries       [16][ 1].place(x=60 * dX, y=1 * dY + 1)
    simple_labels[ 1][ 0].place(x= 0*dX, y= 2*dY)
    simple_labels[ 1][ 1].place(x=53*dX, y= 2*dY)
    simple_labels[ 1][ 2].place(x= 1*dX, y= 3*dY)
    entries       [ 1][ 0].place(x=21 * dX, y=3 * dY + 1)
    entries       [ 1][ 1].place(x=56 * dX, y=3 * dY + 1)
    simple_labels[ 1][ 3].place(x= 1*dX, y= 4*dY)
    smart_labels [ 1][ 0].place(x=10 * dX, y=5 * dY)
    smart_labels [ 1][ 1].place(x=26 * dX, y=5 * dY)
    smart_labels [ 1][ 2].place(x=45 * dX, y=5 * dY)
    entries       [ 1][ 2].place(x=1 * dX, y=6 * dY + 1)
    simple_labels[ 1][ 4].place(x= 1*dX, y= 7*dY)
    smart_labels [ 1][ 3].place(x=57 * dX, y=7 * dY)
    entries       [ 1][ 3].place(x=1 * dX, y=8 * dY + 1)
    smart_labels [ 1][ 4].place(x=34 * dX, y=8 * dY)
    smart_labels [ 1][ 5].place(x=58 * dX, y=8 * dY)
    simple_labels[ 2][ 0].place(x= 0*dX, y= 9*dY)
    smart_labels [ 2][ 0].place(x=1 * dX, y=10 * dY)
    smart_labels [ 2][ 1].place(x=1 * dX, y=11 * dY)
    smart_labels [ 2][ 2].place(x=35 * dX, y=11 * dY)
    entries       [ 2][ 0].place(x=1 * dX, y=12 * dY + 1)
    simple_labels[ 2][ 1].place(x= 1*dX, y=13*dY)
    entries       [ 2][ 1].place(x=19 * dX, y=13 * dY + 1)
    simple_labels[ 5][ 0].place(x= 0*dX, y=14*dY)
    option_menus      [ 0]    .place(x=1 * dX, y=15 * dY - 5)
    # Подраздел "II. Общие данные"
    simple_labels[ 6][ 0].place(x= 0*dX, y= 0*dY)
    entries       [ 6][ 0].place(x=1 * dX, y=1 * dY + 1)
    simple_labels[ 7][ 0].place(x= 0*dX, y= 2*dY)
    entries       [ 7][ 0].place(x=1 * dX, y=3 * dY + 1)
    simple_labels[ 8][ 0].place(x= 0*dX, y= 4*dY)
    simple_labels[ 8][ 1].place(x= 1*dX, y= 5*dY)
    entries       [ 8][ 0].place(x=18 * dX, y=5 * dY + 1)
    smart_labels [ 8][ 0].place(x=29 * dX, y=5 * dY)
    smart_labels [ 8][ 1].place(x=35 * dX, y=5 * dY)
    smart_labels [ 8][ 2].place(x=45 * dX, y=5 * dY)
    smart_labels [ 8][ 3].place(x=51 * dX, y=5 * dY)
    simple_labels[ 8][ 2].place(x= 1*dX, y= 6*dY)
    smart_labels [ 8][ 4].place(x=11 * dX, y=6 * dY)
    smart_labels [ 8][ 5].place(x=20 * dX, y=6 * dY)
    smart_labels [ 8][ 6].place(x=27 * dX, y=6 * dY)
    smart_labels [ 8][ 7].place(x=37 * dX, y=6 * dY)
    smart_labels [ 8][ 8].place(x=47 * dX, y=6 * dY)
    smart_labels [ 8][ 9].place(x=57 * dX, y=6 * dY)
    smart_labels [ 8][10].place(x=11 * dX, y=7 * dY)
    smart_labels [ 8][11].place(x=19 * dX, y=7 * dY)
    smart_labels [ 8][12].place(x=27 * dX, y=7 * dY)
    smart_labels [ 8][13].place(x=48 * dX, y=7 * dY)
    smart_labels [ 8][14].place(x=56 * dX, y=7 * dY)
    entries       [ 8][ 1].place(x=1 * dX, y=8 * dY + 1)
    simple_labels[ 8][ 3].place(x= 1*dX, y= 9*dY)
    entries       [ 8][ 2].place(x=1 * dX, y=10 * dY + 1)
    smart_labels [ 8][15].place(x=23 * dX, y=10 * dY)
    smart_labels [ 8][16].place(x=35 * dX, y=10 * dY)
    smart_labels [ 8][17].place(x=52 * dX, y=10 * dY)
    simple_labels[ 8][ 4].place(x= 1*dX, y=11*dY)
    entries       [ 8][ 3].place(x=21 * dX, y=11 * dY + 1)
    simple_labels[ 8][ 5].place(x=24*dX, y=11*dY)
    # Подраздел "III. Объективный осмотр"
    simple_labels[ 9][ 0].place(x= 0*dX, y= 0*dY)
    simple_labels[ 9][ 1].place(x= 1*dX, y= 1*dY)
    entries       [ 9][ 0].place(x=15 * dX, y=1 * dY + 1)
    smart_labels [ 9][ 0].place(x=41 * dX, y=1 * dY)
    smart_labels [ 9][ 1].place(x=49 * dX, y=1 * dY)
    simple_labels[ 9][ 2].place(x= 1*dX, y= 2*dY)
    entries       [ 9][ 1].place(x=15 * dX, y=2 * dY + 1)
    smart_labels [ 9][ 2].place(x=41 * dX, y=2 * dY)
    simple_labels[ 9][ 3].place(x= 1*dX, y= 3*dY)
    entries       [ 9][ 2].place(x=15 * dX, y=3 * dY + 1)
    smart_labels [ 9][ 3].place(x=41 * dX, y=3 * dY)
    simple_labels[ 9][ 4].place(x= 1*dX, y= 4*dY)
    entries       [ 9][ 3].place(x=15 * dX, y=4 * dY + 1)
    smart_labels [ 9][ 4].place(x=41 * dX, y=4 * dY)
    simple_labels[10][ 0].place(x= 0*dX, y= 5*dY)
    simple_labels[10][ 1].place(x= 1*dX, y= 6*dY)
    smart_labels [10][ 0].place(x=15 * dX, y=6 * dY)
    smart_labels [10][ 1].place(x=36 * dX, y=6 * dY)
    smart_labels [10][ 2].place(x=52 * dX, y=6 * dY)
    entries       [10][ 0].place(x=1 * dX, y=7 * dY + 1)
    simple_labels[10][ 2].place(x= 1*dX, y= 8*dY)
    smart_labels [10][ 3].place(x=31 * dX, y=8 * dY)
    smart_labels [10][ 4].place(x=43 * dX, y=8 * dY)
    entries       [10][ 1].place(x=1 * dX, y=9 * dY + 1)
    simple_labels[10][ 3].place(x= 1*dX, y=10*dY)
    entries       [10][ 2].place(x=26 * dX, y=10 * dY + 1)
    smart_labels [10][ 5].place(x=41 * dX, y=10 * dY)
    smart_labels [10][ 6].place(x=49 * dX, y=10 * dY)
    smart_labels [10][ 7].place(x=59 * dX, y=10 * dY)
    simple_labels[10][ 4].place(x= 1*dX, y=11*dY)
    entries       [10][ 3].place(x=13 * dX, y=12 * dY + 1)
    smart_labels [10][ 8].place(x=28 * dX, y=12 * dY)
    smart_labels [10][ 9].place(x=42 * dX, y=12 * dY)
    smart_labels [10][10].place(x=54 * dX, y=12 * dY)
    simple_labels[10][ 5].place(x= 1*dX, y=13*dY)
    entries       [10][ 4].place(x=21 * dX, y=13 * dY + 1)
    simple_labels[10][ 6].place(x=25*dX, y=13*dY)
    simple_labels[11][ 0].place(x= 0*dX, y=14*dY)
    simple_labels[11][ 1].place(x= 3*dX, y=15*dY)
    entries       [11][ 0].place(x=1 * dX, y=16 * dY + 1)
    simple_labels[12][ 0].place(x= 0*dX, y=17*dY)
    simple_labels[12][ 1].place(x= 3*dX, y=18*dY)
    entries       [12][ 0].place(x=1 * dX, y=19 * dY + 1)
    smart_labels [12][ 0].place(x=41 * dX, y=19 * dY)
    smart_labels [12][ 1].place(x=49 * dX, y=19 * dY)
    # Подраздел "IV. Данные освидетельствования"
    simple_labels[13][ 0].place(x= 0*dX, y= 0*dY)
    simple_labels[13][ 1].place(x= 1*dX, y= 1*dY)
    simple_labels[13][ 2].place(x=28*dX, y= 1*dY)
    entries       [13][ 0].place(x=34 * dX, y=1 * dY + 1)
    simple_labels[13][ 3].place(x=43*dX, y= 1*dY)
    entries       [13][ 1].place(x=52 * dX, y=1 * dY + 1)
    simple_labels[13][ 4].place(x=57*dX, y= 1*dY)
    simple_labels[13][ 5].place(x= 1*dX, y= 2*dY)
    option_menus      [ 1]    .place(x=19 * dX, y=2 * dY - 5)
    checkbuttons      [ 0]    .place(x=47 * dX, y=3 * dY)
    simple_labels[13][ 6].place(x= 1*dX, y= 4*dY)
    simple_labels[13][ 7].place(x=28*dX, y= 4*dY)
    entries       [13][ 2].place(x=34 * dX, y=4 * dY + 1)
    simple_labels[13][ 8].place(x=43*dX, y= 4*dY)
    entries       [13][ 3].place(x=52 * dX, y=4 * dY + 1)
    simple_labels[13][ 9].place(x=57*dX, y= 4*dY)
    simple_labels[13][10].place(x= 1*dX, y= 5*dY)
    option_menus      [ 2]    .place(x=19 * dX, y=5 * dY - 5)
    simple_labels[14][ 0].place(x= 0*dX, y= 6*dY)
    entries       [14][ 0].place(x=34 * dX, y=6 * dY + 1)
    simple_labels[14][ 1].place(x=44*dX, y= 6*dY)
    entries       [14][ 1].place(x=51 * dX, y=6 * dY + 1)
    smart_labels [14][ 0].place(x=57 * dX, y=6 * dY)
    checkbuttons      [ 1]    .place(x=27 * dX, y=7 * dY)
    checkbuttons      [ 2]    .place(x=27 * dX, y=8 * dY)
    simple_labels[14][ 2].place(x= 2*dX, y= 9*dY)
    option_menus      [ 3]    .place(x=19 * dX, y=9 * dY - 5)
    simple_labels[14][ 3].place(x= 1*dX, y=10*dY)
    simple_labels[14][ 4].place(x=44*dX, y=10*dY)
    entries       [14][ 2].place(x=57 * dX, y=10 * dY + 1)
    simple_labels[14][ 5].place(x=62*dX, y=10*dY)
    simple_labels[14][ 6].place(x= 3*dX, y=11*dY)
    entries       [14][ 3].place(x=20 * dX, y=11 * dY + 1)
    smart_labels [14][ 1].place(x=24 * dX, y=11 * dY)
    smart_labels [14][ 2].place(x=28 * dX, y=11 * dY)
    simple_labels[14][ 7].place(x=35*dX, y=11*dY)
    entries       [14][ 4].place(x=52 * dX, y=11 * dY + 1)
    smart_labels [14][ 3].place(x=56 * dX, y=11 * dY)
    smart_labels [14][ 4].place(x=60 * dX, y=11 * dY)
    simple_labels[14][ 8].place(x= 3*dX, y=12*dY)
    entries       [14][ 5].place(x=20 * dX, y=12 * dY + 1)
    smart_labels [14][ 5].place(x=24 * dX, y=12 * dY)
    smart_labels [14][ 6].place(x=28 * dX, y=12 * dY)
    simple_labels[14][ 9].place(x=35*dX, y=12*dY)
    entries       [14][ 6].place(x=52 * dX, y=12 * dY + 1)
    smart_labels [14][ 7].place(x=56 * dX, y=12 * dY)
    smart_labels [14][ 8].place(x=60 * dX, y=12 * dY)
    simple_labels[14][10].place(x= 3*dX, y=13*dY)
    entries       [14][ 7].place(x=20 * dX, y=13 * dY + 1)
    smart_labels [14][ 9].place(x=24 * dX, y=13 * dY)
    smart_labels [14][10].place(x=28 * dX, y=13 * dY)
    simple_labels[14][11].place(x=35*dX, y=13*dY)
    entries       [14][ 8].place(x=52 * dX, y=13 * dY + 1)
    smart_labels [14][11].place(x=56 * dX, y=13 * dY)
    smart_labels [14][12].place(x=60 * dX, y=13 * dY)
    simple_labels[14][12].place(x= 3*dX, y=14*dY)
    entries       [14][ 9].place(x=20 * dX, y=14 * dY + 1)
    smart_labels [14][13].place(x=24 * dX, y=14 * dY)
    smart_labels [14][14].place(x=28 * dX, y=14 * dY)
    simple_labels[14][13].place(x=35*dX, y=14*dY)
    entries       [14][10].place(x=52 * dX, y=14 * dY + 1)
    smart_labels [14][15].place(x=56 * dX, y=14 * dY)
    smart_labels [14][16].place(x=60 * dX, y=14 * dY)
    simple_labels[14][14].place(x= 3*dX, y=15*dY)
    entries       [14][11].place(x=20 * dX, y=15 * dY + 1)
    smart_labels [14][17].place(x=24 * dX, y=15 * dY)
    smart_labels [14][18].place(x=28 * dX, y=15 * dY)
    simple_labels[14][15].place(x=35*dX, y=15*dY)
    entries       [14][12].place(x=52 * dX, y=15 * dY + 1)
    smart_labels [14][19].place(x=56 * dX, y=15 * dY)
    smart_labels [14][20].place(x=60 * dX, y=15 * dY)
    simple_labels[14][16].place(x= 3*dX, y=16*dY)
    entries       [14][13].place(x=20 * dX, y=16 * dY + 1)
    smart_labels [14][21].place(x=24 * dX, y=16 * dY)
    smart_labels [14][22].place(x=28 * dX, y=16 * dY)
    simple_labels[15][ 0].place(x= 0*dX, y=17*dY)
    entries       [15][ 0].place(x=1 * dX, y=18 * dY + 1)
    simple_labels[17][ 0].place(x= 0*dX, y=19*dY)
    smart_labels [17][ 0].place(x=27 * dX, y=19 * dY)
    smart_labels [17][ 1].place(x=8 * dX, y=20 * dY)
    smart_labels [17][ 2].place(x=36 * dX, y=20 * dY)
    entries       [17][ 0].place(x=1 * dX, y=21 * dY + 1)
    simple_labels[17][ 1].place(x=41*dX, y=21*dY)
    entries       [17][ 1].place(x=46 * dX, y=21 * dY + 1)

# Вывод индексации списков.
def WriteIndexes():
    f = open('index.txt', 'w')
    f.write('simple_labels\n')
    for i in range(form_length):
        for j in range(len(simple_labels[i])):
            f.write('%d\t%d\t%s\n' % (i, j, simple_labels[i][j].cget('text')))
    f.write('\n')
    f.write('Es\n')
    for i in range(form_length):
        for j in range(len(entries[i])):
            f.write('%d\t%d\t%d\t%s\n' %
                    (i, j, entries[i][j].cget('width'), entries_default[i][j]))
    f.write('\n')
    f.write('smart_Ls\n')
    for i in range(form_length):
        for j in range(len(smart_labels[i])):
            f.write('%d\t%d\t%s\n' %
                    (i, j, smart_labels[i][j].cget('text')))
    f.write('\n')
    f.write('OMs\n')
    for i in range(len(option_menus)):
        f.write('%d\t%s\t%s\n' % (i, option_menus[i].cget('width'), option_menus_note[i]))
    f.write('\n')
    f.write('CBs\n')
    for i in range(len(checkbuttons)):
        f.write('%d\t%s\n' % (i, checkbuttons[i].cget('text')))
    f.close()

# Работа с элементаци формы.
#  Проверка данных формы
def need():
    for i in range(11):
        if entries[14][i + 3].get():
            return True
    return False
def Check():
    temp = True
    # I. Паспортная часть
    if entries[0][0].get():
        if not entries[0][0].get().isnumeric():
            popup_tag(simple_labels, 'format', (0, 0))
            temp = False
    else:
        popup_tag(simple_labels, 'enter', (0, 0))
        temp = False
    if not entries[1][0].get():
        popup_tag(simple_labels, 'enter', (1, 0), (1, 2))
        temp = False
    if entries[4][0].get():
        try: strptime(entries[4][0].get(), '%d.%m.%Y')
        except:
            popup_tag(simple_labels, 'format', (4, 0), (4, 1))
            temp = False
    else:
        popup_tag(simple_labels, 'enter', (4, 0), (4, 1))
        temp = False
    if entries[4][1].get():
        try: strptime(entries[4][1].get(), '%H:%M')
        except:
            popup_tag(simple_labels, 'format', (4, 0), (4, 2))
            temp = False
    else:
        popup_tag(simple_labels, 'enter', (4, 0), (4, 2))
        temp = False
    if entries[16][0].get():
        try: strptime(entries[16][0].get(), '%d.%m.%Y')
        except:
            popup_tag(simple_labels, 'format', (16, 0), (16, 1))
            temp = False
    else:
        popup_tag(simple_labels, 'enter', (16, 0), (16, 1))
        temp = False
    if entries[16][1].get():
        try: strptime(entries[16][1].get(), '%H:%M')
        except:
            popup_tag(simple_labels, 'format', (16, 0), (16, 2))
            temp = False
    else:
        popup_tag(simple_labels, 'enter', (16, 0), (16, 2))
        temp = False
    if entries[1][1].get():
        try: strptime(entries[1][1].get(), '%d.%m.%Y')
        except:
            popup_tag(simple_labels, 'format', (1, 0), (1, 1))
            temp = False
    if not string_vars[0].get():
        popup_tag(simple_labels, 'select', (5, 0))
        temp = False
    # IV. Данные освидетельствования
    if not int_vars[0].get():
        if entries[13][1].get():
            try:
                float(entries[13][1].get())
            except:
                popup_tag(simple_labels, 'format', (13, 1), (13, 3))
                temp = False
            if entries[13][0].get():
                try:
                    strptime(entries[13][0].get(), '%H:%M')
                except:
                    popup_tag(simple_labels, 'format', (13, 1), (13, 2))
                    temp = False
            else:
                popup_tag(simple_labels, 'enter', (13, 1), (13, 2))
                temp = False
            if not string_vars[1].get():
                popup_tag(simple_labels, 'select', (13, 1), (13, 5))
                temp = False
        if entries[13][3].get():
            try:
                float(entries[13][3].get())
            except:
                popup_tag(simple_labels, 'format', (13, 6), (13, 8))
                temp = False
            if entries[13][2].get():
                try:
                    strptime(entries[13][2].get(), '%H:%M')
                except:
                    popup_tag(simple_labels, 'format', (13, 6), (13, 7))
                    temp = False
            else:
                popup_tag(simple_labels, 'enter', (13, 6), (13, 7))
                temp = False
            if not string_vars[2].get():
                popup_tag(simple_labels, 'select', (13, 6), (13, 10))
                temp = False
    if entries[14][0].get():
        try: strptime(entries[14][0].get(), '%H:%M')
        except:
            popup_tag(simple_labels, 'format', (14, 0))
            temp = False
        if not string_vars[3].get():
            popup_tag(simple_labels, 'enter', (14, 0), (14, 2))
            temp = False
        if not entries[14][2].get() and need():
            popup_tag(simple_labels, 'enter', (14, 0), (14, 4))
            temp = False
    if entries[17][1].get():
        try: strptime(entries[17][1].get(), '%d.%m.%Y')
        except:
            popup_tag(simple_labels, 'format', (17, 0), (17, 1))
            temp = False
    elif entries[17][0].get():
        popup_tag(simple_labels, 'enter', (17, 0), (17, 1))
        temp = False
    # Последовательность событий
    try:
        temp1 = strptime(entries[ 4][0].get() + entries[ 4][1].get(), '%d.%m.%Y%H:%M')
        temp2 = strptime(entries[16][0].get() + entries[16][1].get(), '%d.%m.%Y%H:%M')
        if not temp1 < temp2:
            popup_tag(simple_labels, 'ratio', (4, 0), (16, 0))
            temp = False
    except: pass
    try:
        temp2 = strptime(entries[16][1].get(), '%H:%M')
        if entries[13][1].get() and not entries[13][3].get():
            temp1 = strptime(entries[13][0].get(), '%H:%M')
            temp3 = temp1.tm_hour + temp1.tm_min/60
            temp4 = temp2.tm_hour + temp2.tm_min/60
            if temp1 > temp2 and temp3 - temp4 < 23:
                popup_tag(simple_labels, 'ratio', (13, 1), (16, 0))
                temp = False
        if entries[13][3].get():
            temp1 = strptime(entries[13][2].get(), '%H:%M')
            temp3 = temp1.tm_hour + temp1.tm_min/60
            temp4 = temp2.tm_hour + temp2.tm_min/60
            if temp1 > temp2 and temp3 - temp4 < 23:
                popup_tag(simple_labels, 'ratio', (13, 6), (16, 0))
                temp = False
    except: pass
    try:
        temp1 = strptime(entries[13][0].get(), '%H:%M')
        temp2 = strptime(entries[13][2].get(), '%H:%M')
        temp3 = temp1.tm_hour*60 + temp1.tm_min
        temp4 = temp2.tm_hour*60 + temp2.tm_min
        if ((temp4 - temp3 < 15 or temp4 - temp3 > 20) and
            (temp4 - temp3 + 1440 < 15 or temp4 - temp3 + 1440 > 20)):
            popup_tag(simple_labels, 'ratio', (13, 1), (13, 6))
            temp = False
    except: pass
    return temp
#  Чтение данных из формы
def getDataLines():
    lines = []
    for i in range(58):
        lines.append('')
    lines[ 0] =        entries[ 0][ 0].get()
    lines[ 1] = simple_labels[ 0][ 1]['text']
    lines[ 2] =        entries[ 1][ 0].get()
    lines[ 3] =        entries[ 1][ 1].get()
    lines[ 4] =        entries[ 1][ 2].get()
    lines[ 5] =        entries[ 1][ 3].get()
    lines[ 6] =        entries[ 2][ 0].get()
    lines[ 7] =        entries[ 2][ 1].get()
    lines[ 8] =        entries[ 4][ 0].get()
    lines[ 9] =        entries[ 4][ 1].get()
    lines[10] =           string_vars[ 0].get()
    lines[11] =        entries[ 6][ 0].get()
    lines[12] =        entries[ 7][ 0].get()
    lines[13] =        entries[ 8][ 0].get()
    lines[14] =        entries[ 8][ 1].get()
    lines[15] =        entries[ 8][ 2].get()
    lines[16] =        entries[ 8][ 3].get()
    lines[17] =        entries[ 9][ 0].get()
    lines[18] =        entries[ 9][ 1].get()
    lines[19] =        entries[ 9][ 2].get()
    lines[20] =        entries[ 9][ 3].get()
    lines[21] =        entries[10][ 0].get()
    lines[22] =        entries[10][ 1].get()
    lines[23] =        entries[10][ 2].get()
    lines[24] =        entries[10][ 3].get()
    lines[25] =        entries[10][ 4].get()
    lines[26] =        entries[11][ 0].get()
    lines[27] =        entries[12][ 0].get()
    lines[28] =        entries[13][ 0].get()
    lines[29] =        entries[13][ 1].get()
    lines[30] =           string_vars[ 1].get()
    lines[31] =       str(int_vars[ 0].get())
    lines[32] =        entries[13][ 2].get()
    lines[33] =        entries[13][ 3].get()
    lines[34] =           string_vars[ 2].get()
    lines[35] =        entries[14][ 0].get()
    lines[36] =        entries[14][ 1].get()
    lines[37] =       str(int_vars[ 1].get())
    lines[38] =       str(int_vars[ 2].get())
    lines[39] =           string_vars[ 3].get()
    lines[40] =        entries[14][ 2].get()
    lines[41] = simple_labels[14][ 5]['text']
    # Вещества
    for i in range(42, 53):
        if entries[14][i - 39].get():
            lines[i] = simple_labels[14][i - 36].cget('text') +\
                       ':' + entries[14][i - 39].get()
    #
    lines[53] =        entries[15][ 0].get()
    lines[54] =        entries[16][ 0].get()
    lines[55] =        entries[16][ 1].get()
    lines[56] =        entries[17][ 0].get()
    lines[57] =        entries[17][ 1].get()
    return lines
#  Запись данных в форму
def setLine(entry, line):
    temp = entry.cget('state') == 'disabled'
    if temp:
        entry.config(state='normal')
    entry.delete(0, END)
    entry.insert(0, line)
    if temp:
        entry.config(state='disabled')
def setDataLines(lines):
    setLine(entries[ 0][ 0], lines[ 0])
    simple_labels [ 0][ 1]['text'] = lines[ 1]
    setLine(entries[ 1][ 0], lines[ 2])
    setLine(entries[ 1][ 1], lines[ 3])
    setLine(entries[ 1][ 2], lines[ 4])
    setLine(entries[ 1][ 3], lines[ 5])
    setLine(entries[ 2][ 0], lines[ 6])
    setLine(entries[ 2][ 1], lines[ 7])
    setLine(entries[ 4][ 0], lines[ 8])
    setLine(entries[ 4][ 1], lines[ 9])
    string_vars[0].set(lines[10])
    setLine(entries[ 6][ 0], lines[11])
    setLine(entries[ 7][ 0], lines[12])
    setLine(entries[ 8][ 0], lines[13])
    setLine(entries[ 8][ 1], lines[14])
    setLine(entries[ 8][ 2], lines[15])
    setLine(entries[ 8][ 3], lines[16])
    setLine(entries[ 9][ 0], lines[17])
    setLine(entries[ 9][ 1], lines[18])
    setLine(entries[ 9][ 2], lines[19])
    setLine(entries[ 9][ 3], lines[20])
    setLine(entries[10][ 0], lines[21])
    setLine(entries[10][ 1], lines[22])
    setLine(entries[10][ 2], lines[23])
    setLine(entries[10][ 3], lines[24])
    setLine(entries[10][ 4], lines[25])
    setLine(entries[11][ 0], lines[26])
    setLine(entries[12][ 0], lines[27])
    setLine(entries[13][ 0], lines[28])
    setLine(entries[13][ 1], lines[29])
    string_vars[1].set(lines[30])
    int_vars[0].set(lines[31])
    setLine(entries[13][ 2], lines[32])
    setLine(entries[13][ 3], lines[33])
    string_vars[2].set(lines[34])
    setLine(entries[14][ 0], lines[35])
    setLine(entries[14][ 1], lines[36])
    int_vars[1].set(lines[37])
    int_vars[2].set(lines[38])
    string_vars[3].set(lines[39])
    setLine(entries[14][ 2], lines[40])
    simple_labels [14][ 5]['text'] = lines[41]
    # Вещества
    for i in range(42, 53):
        if lines[i]:
            simple_labels [14][i - 36].config(text=lines[i].split(':')[0])
            setLine(entries[14][i - 39], lines[i].split(':')[1])
        else:
            setLine(entries[14][i - 39], '')
    #
    setLine(entries[15][ 0], lines[53])
    setLine(entries[16][ 0], lines[54])
    setLine(entries[16][ 1], lines[55])
    setLine(entries[17][ 0], lines[56])
    setLine(entries[17][ 1], lines[57])
#  Подготовка данных к печати
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
    data[0].append(entries[0][0].get() + simple_labels[0][1]['text'])
    data[0].append(getDateLine(entries[4][0].get()))
    data[1].append(entries[1][0].get())
    data[1].append(entries[1][1].get())
    data[1].append(entries[1][2].get())
    data[1].append(entries[1][3].get())
    data[2].append(entries[2][0].get())
    data[2].append(entries[2][1].get())
    data[3].append(init['Подразделение'])
    data[4].append(entries[4][0].get() + ' ' + entries[4][1].get())
    data[5].append(string_vars[0].get().partition(', ')[0])
    data[5].append(string_vars[0].get().partition(', ')[2])
    data[6].append(entries[6][0].get())
    data[7].append(entries[7][0].get())
    data[8].append(entries[8][0].get())
    data[8].append(entries[8][1].get())
    data[8].append(entries[8][2].get())
    if entries[8][3].get():
        data[8].append(entries[8][3].get() + ' ' + simple_labels[8][5]['text'])
    else:
        data[8].append('не проводилось')
    data[9].append(entries[9][0].get())
    data[9].append(entries[9][1].get())
    data[9].append(entries[9][2].get())
    data[9].append(entries[9][3].get())
    data[10].append(entries[10][0].get())
    data[10].append(entries[10][1].get())
    data[10].append(entries[10][2].get())
    data[10].append(entries[10][3].get())
    if entries[10][4].get():
        data[10].append(entries[10][4].get() + ' ' + simple_labels[10][6]['text'])
    else:
        data[10].append('не проводилось')
    data[11].append(entries[11][0].get())
    data[12].append(entries[12][0].get())
    if entries[13][1].get():
        data[13].append('%s, %s, %s %s' % (entries[13][0].get(), string_vars[1].get(),
                                           entries[13][1].get(), simple_labels[13][4]['text']))
    else:
        data[13].append('не проводилось')
    if entries[13][3].get():
        data[13].append('%s, %s, %s %s' % (entries[13][2].get(), string_vars[2].get(),
                                           entries[13][3].get(), simple_labels[13][9]['text']))
    else:
        if entries[13][1].get() and float(entries[13][1].get()) <= 0.16:
            data[13].append('''не проводилось в связи с
                отрицательным результатом первого исследования''')
        else: data[13].append('не проводилось')
    if int_vars[0].get():
        data[13][0] = checkbuttons[0]['text']
        data[13][1] = 'не проводилось'
    if entries[14][0].get():
        data[14].append('%s (%s)' % (entries[14][0].get(), entries[14][1].get()))
        data[14].append(init['Лаборатория'] + ', ' + string_vars[3].get())
        for i in range(3, 13):
            if entries[14][i].get():
                data[14][1] += ', %s: %s' % (simple_labels[14][i + 3]['text'],
                                             getLineMP(entries[14][i]))
        data[14][1] += ', № ' + entries[14][2].get() + simple_labels[14][5]['text']
    else:
        data[14].append('''забор биологического объекта для
            химико-токсикологических исследований не осуществлялся''')
        data[14].append('нет')
    if int_vars[1].get():
        data[14][0] = checkbuttons[1]['text']
        data[14][1] = 'нет'
    if int_vars[2].get():
        data[14][0] = checkbuttons[2]['text']
        data[14][1] = 'нет'
    data[15].append(entries[15][0].get())
    data[16].append(entries[16][0].get() + ' ' + entries[16][1].get())
    data[17].append(entries[17][0].get())
    data[17].append(entries[17][1].get())
    data[18].append(string_vars[0].get().partition(',')[0])
    return data

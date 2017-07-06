from data import *
from event import *
from popup import *
from time import strptime
from tkinter import (Checkbutton, END, Entry, IntVar,
                     Label, OptionMenu, StringVar)

form_length = 18

simple_labels = []

entries = []
entries_default = []

smart_labels = []

string_vars = []
option_menus = []
option_menus_note = []

int_vars = []
checkbuttons = []

dX = 8
dY = 28


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
    entries_state = []
    for i in range(form_length):
        entries.append([])
        entries_default.append([])
        entries_state.append([])

    for item in get_entries_data():
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


def init_smart_labels(label_frames):
    for i in range(form_length):
        smart_labels.append([])

    for item in get_smart_labels_data():
        smart_labels[item[0]].append(
            Label(label_frames[item[1]], text=item[2]))

    bind_smart_labels_events(smart_labels, entries, entries_default)


def init_option_menus(label_frames, init, cur_user):
    option_menus_note.append(simple_labels[5][0].cget('text'))
    option_menus_note.append(simple_labels[13][5].cget('text'))
    option_menus_note.append(simple_labels[13][10].cget('text'))
    option_menus_note.append(simple_labels[14][2].cget('text'))
    for i in [3, 3, 3]:
        string_vars.append(StringVar(label_frames[i]))
    option_menus.append(OptionMenu(
        label_frames[3], string_vars[1], *init['Технические средства']))
    option_menus.append(OptionMenu(
        label_frames[3], string_vars[2], *init['Технические средства']))
    option_menus.append(OptionMenu(
        label_frames[3], string_vars[3], *init['Методы']))


def place():
    # Подраздел "IV. Данные освидетельствования"
    simple_labels[13][0].place(x=0 * dX, y=0 * dY)
    simple_labels[13][1].place(x=1 * dX, y=1 * dY)
    simple_labels[13][2].place(x=28 * dX, y=1 * dY)
    entries[13][0].place(x=34 * dX, y=1 * dY + 1)
    simple_labels[13][3].place(x=43 * dX, y=1 * dY)
    entries[13][1].place(x=52 * dX, y=1 * dY + 1)
    simple_labels[13][4].place(x=57 * dX, y=1 * dY)
    simple_labels[13][5].place(x=1 * dX, y=2 * dY)
    option_menus[1].place(x=19 * dX, y=2 * dY - 5)
    checkbuttons[0].place(x=47 * dX, y=3 * dY)
    simple_labels[13][6].place(x=1 * dX, y=4 * dY)
    simple_labels[13][7].place(x=28 * dX, y=4 * dY)
    entries[13][2].place(x=34 * dX, y=4 * dY + 1)
    simple_labels[13][8].place(x=43 * dX, y=4 * dY)
    entries[13][3].place(x=52 * dX, y=4 * dY + 1)
    simple_labels[13][9].place(x=57 * dX, y=4 * dY)
    simple_labels[13][10].place(x=1 * dX, y=5 * dY)
    option_menus[2].place(x=19 * dX, y=5 * dY - 5)
    simple_labels[14][0].place(x=0 * dX, y=6 * dY)
    entries[14][0].place(x=34 * dX, y=6 * dY + 1)
    simple_labels[14][1].place(x=44 * dX, y=6 * dY)
    entries[14][1].place(x=51 * dX, y=6 * dY + 1)
    smart_labels[14][0].place(x=57 * dX, y=6 * dY)
    checkbuttons[1].place(x=27 * dX, y=7 * dY)
    checkbuttons[2].place(x=27 * dX, y=8 * dY)
    simple_labels[14][2].place(x=2 * dX, y=9 * dY)
    option_menus[3].place(x=19 * dX, y=9 * dY - 5)
    simple_labels[14][3].place(x=1 * dX, y=10 * dY)
    simple_labels[14][4].place(x=44 * dX, y=10 * dY)
    entries[14][2].place(x=57 * dX, y=10 * dY + 1)
    simple_labels[14][5].place(x=62 * dX, y=10 * dY)
    simple_labels[14][6].place(x=3 * dX, y=11 * dY)
    entries[14][3].place(x=20 * dX, y=11 * dY + 1)
    smart_labels[14][1].place(x=24 * dX, y=11 * dY)
    smart_labels[14][2].place(x=28 * dX, y=11 * dY)
    simple_labels[14][7].place(x=35 * dX, y=11 * dY)
    entries[14][4].place(x=52 * dX, y=11 * dY + 1)
    smart_labels[14][3].place(x=56 * dX, y=11 * dY)
    smart_labels[14][4].place(x=60 * dX, y=11 * dY)
    simple_labels[14][8].place(x=3 * dX, y=12 * dY)
    entries[14][5].place(x=20 * dX, y=12 * dY + 1)
    smart_labels[14][5].place(x=24 * dX, y=12 * dY)
    smart_labels[14][6].place(x=28 * dX, y=12 * dY)
    simple_labels[14][9].place(x=35 * dX, y=12 * dY)
    entries[14][6].place(x=52 * dX, y=12 * dY + 1)
    smart_labels[14][7].place(x=56 * dX, y=12 * dY)
    smart_labels[14][8].place(x=60 * dX, y=12 * dY)
    simple_labels[14][10].place(x=3 * dX, y=13 * dY)
    entries[14][7].place(x=20 * dX, y=13 * dY + 1)
    smart_labels[14][9].place(x=24 * dX, y=13 * dY)
    smart_labels[14][10].place(x=28 * dX, y=13 * dY)
    simple_labels[14][11].place(x=35 * dX, y=13 * dY)
    entries[14][8].place(x=52 * dX, y=13 * dY + 1)
    smart_labels[14][11].place(x=56 * dX, y=13 * dY)
    smart_labels[14][12].place(x=60 * dX, y=13 * dY)
    simple_labels[14][12].place(x=3 * dX, y=14 * dY)
    entries[14][9].place(x=20 * dX, y=14 * dY + 1)
    smart_labels[14][13].place(x=24 * dX, y=14 * dY)
    smart_labels[14][14].place(x=28 * dX, y=14 * dY)
    simple_labels[14][13].place(x=35 * dX, y=14 * dY)
    entries[14][10].place(x=52 * dX, y=14 * dY + 1)
    smart_labels[14][15].place(x=56 * dX, y=14 * dY)
    smart_labels[14][16].place(x=60 * dX, y=14 * dY)
    simple_labels[14][14].place(x=3 * dX, y=15 * dY)
    entries[14][11].place(x=20 * dX, y=15 * dY + 1)
    smart_labels[14][17].place(x=24 * dX, y=15 * dY)
    smart_labels[14][18].place(x=28 * dX, y=15 * dY)
    simple_labels[14][15].place(x=35 * dX, y=15 * dY)
    entries[14][12].place(x=52 * dX, y=15 * dY + 1)
    smart_labels[14][19].place(x=56 * dX, y=15 * dY)
    smart_labels[14][20].place(x=60 * dX, y=15 * dY)
    simple_labels[14][16].place(x=3 * dX, y=16 * dY)
    entries[14][13].place(x=20 * dX, y=16 * dY + 1)
    smart_labels[14][21].place(x=24 * dX, y=16 * dY)
    smart_labels[14][22].place(x=28 * dX, y=16 * dY)
    simple_labels[15][0].place(x=0 * dX, y=17 * dY)
    entries[15][0].place(x=1 * dX, y=18 * dY + 1)
    simple_labels[17][0].place(x=0 * dX, y=19 * dY)
    smart_labels[17][0].place(x=27 * dX, y=19 * dY)
    smart_labels[17][1].place(x=8 * dX, y=20 * dY)
    smart_labels[17][2].place(x=36 * dX, y=20 * dY)
    entries[17][0].place(x=1 * dX, y=21 * dY + 1)
    simple_labels[17][1].place(x=41 * dX, y=21 * dY)
    entries[17][1].place(x=46 * dX, y=21 * dY + 1)


def write_indexes():
    f = open('index.txt', 'w')
    f.write('simple_labels\n')
    for i in range(form_length):
        for j in range(len(simple_labels[i])):
            f.write('%d\t%d\t%s\n' % (i, j, simple_labels[i][j].cget('text')))
    f.write('\n')
    f.write('entries\n')
    for i in range(form_length):
        for j in range(len(entries[i])):
            f.write('%d\t%d\t%d\t%s\n' %
                    (i, j, entries[i][j].cget('width'), entries_default[i][j]))
    f.write('\n')
    f.write('smart_labels\n')
    for i in range(form_length):
        for j in range(len(smart_labels[i])):
            f.write('%d\t%d\t%s\n' %
                    (i, j, smart_labels[i][j].cget('text')))
    f.write('\n')
    f.write('option_menus\n')
    for i in range(len(option_menus)):
        f.write('%d\t%s\t%s\n' % (i, option_menus[i].cget('width'), option_menus_note[i]))
    f.write('\n')
    f.write('checkbuttons\n')
    for i in range(len(checkbuttons)):
        f.write('%d\t%s\n' % (i, checkbuttons[i].cget('text')))
    f.close()


def check():
    b = True

    # I. Паспортная часть
    if entries[0][0].get():
        if not entries[0][0].get().isnumeric():
            popup_tag(simple_labels, 'format', (0, 0))
            b = False
    else:
        popup_tag(simple_labels, 'enter', (0, 0))
        b = False
    if not entries[1][0].get():
        popup_tag(simple_labels, 'enter', (1, 0), (1, 2))
        b = False
    if entries[4][0].get():
        try:
            strptime(entries[4][0].get(), '%d.%m.%Y')
        except ValueError:
            popup_tag(simple_labels, 'format', (4, 0), (4, 1))
            b = False
    else:
        popup_tag(simple_labels, 'enter', (4, 0), (4, 1))
        b = False
    if entries[4][1].get():
        try:
            strptime(entries[4][1].get(), '%H:%M')
        except ValueError:
            popup_tag(simple_labels, 'format', (4, 0), (4, 2))
            b = False
    else:
        popup_tag(simple_labels, 'enter', (4, 0), (4, 2))
        b = False
    if entries[16][0].get():
        try:
            strptime(entries[16][0].get(), '%d.%m.%Y')
        except ValueError:
            popup_tag(simple_labels, 'format', (16, 0), (16, 1))
            b = False
    else:
        popup_tag(simple_labels, 'enter', (16, 0), (16, 1))
        b = False
    if entries[16][1].get():
        try:
            strptime(entries[16][1].get(), '%H:%M')
        except ValueError:
            popup_tag(simple_labels, 'format', (16, 0), (16, 2))
            b = False
    else:
        popup_tag(simple_labels, 'enter', (16, 0), (16, 2))
        b = False
    if entries[1][1].get():
        try:
            strptime(entries[1][1].get(), '%d.%m.%Y')
        except ValueError:
            popup_tag(simple_labels, 'format', (1, 0), (1, 1))
            b = False
    if not string_vars[0].get():
        popup_tag(simple_labels, 'select', (5, 0))
        b = False

    # IV. Данные освидетельствования
    if not int_vars[0].get():
        if entries[13][1].get():
            try:
                float(entries[13][1].get())
            except ValueError:
                popup_tag(simple_labels, 'format', (13, 1), (13, 3))
                b = False
            if entries[13][0].get():
                try:
                    strptime(entries[13][0].get(), '%H:%M')
                except ValueError:
                    popup_tag(simple_labels, 'format', (13, 1), (13, 2))
                    b = False
            else:
                popup_tag(simple_labels, 'enter', (13, 1), (13, 2))
                b = False
            if not string_vars[1].get():
                popup_tag(simple_labels, 'select', (13, 1), (13, 5))
                b = False
        if entries[13][3].get():
            try:
                float(entries[13][3].get())
            except ValueError:
                popup_tag(simple_labels, 'format', (13, 6), (13, 8))
                b = False
            if entries[13][2].get():
                try:
                    strptime(entries[13][2].get(), '%H:%M')
                except ValueError:
                    popup_tag(simple_labels, 'format', (13, 6), (13, 7))
                    b = False
            else:
                popup_tag(simple_labels, 'enter', (13, 6), (13, 7))
                b = False
            if not string_vars[2].get():
                popup_tag(simple_labels, 'select', (13, 6), (13, 10))
                b = False
    if entries[14][0].get():
        def need():
            for i in range(11):
                if entries[14][i + 3].get():
                    return True
            return False
        try:
            strptime(entries[14][0].get(), '%H:%M')
        except ValueError:
            popup_tag(simple_labels, 'format', (14, 0))
            b = False
        if not string_vars[3].get():
            popup_tag(simple_labels, 'enter', (14, 0), (14, 2))
            b = False
        if not entries[14][2].get() and need():
            popup_tag(simple_labels, 'enter', (14, 0), (14, 4))
            b = False
    if entries[17][1].get():
        try:
            strptime(entries[17][1].get(), '%d.%m.%Y')
        except ValueError:
            popup_tag(simple_labels, 'format', (17, 0), (17, 1))
            b = False
    elif entries[17][0].get():
        popup_tag(simple_labels, 'enter', (17, 0), (17, 1))
        b = False

    # Последовательность событий
    try:
        temp1 = strptime(entries[4][0].get() + entries[4][1].get(), '%d.%m.%Y%H:%M')
        temp2 = strptime(entries[16][0].get() + entries[16][1].get(), '%d.%m.%Y%H:%M')
        if not temp1 < temp2:
            popup_tag(simple_labels, 'ratio', (4, 0), (16, 0))
            b = False
    except ValueError:
        pass
    try:
        temp2 = strptime(entries[16][1].get(), '%H:%M')
        if entries[13][1].get() and not entries[13][3].get():
            temp1 = strptime(entries[13][0].get(), '%H:%M')
            temp3 = temp1.tm_hour + temp1.tm_min / 60
            temp4 = temp2.tm_hour + temp2.tm_min / 60
            if temp1 > temp2 and temp3 - temp4 < 23:
                popup_tag(simple_labels, 'ratio', (13, 1), (16, 0))
                b = False
        if entries[13][3].get():
            temp1 = strptime(entries[13][2].get(), '%H:%M')
            temp3 = temp1.tm_hour + temp1.tm_min / 60
            temp4 = temp2.tm_hour + temp2.tm_min / 60
            if temp1 > temp2 and temp3 - temp4 < 23:
                popup_tag(simple_labels, 'ratio', (13, 6), (16, 0))
                b = False
    except ValueError:
        pass
    try:
        temp1 = strptime(entries[13][0].get(), '%H:%M')
        temp2 = strptime(entries[13][2].get(), '%H:%M')
        temp3 = temp1.tm_hour * 60 + temp1.tm_min
        temp4 = temp2.tm_hour * 60 + temp2.tm_min
        if ((temp4 - temp3 < 15 or temp4 - temp3 > 20) and
                (temp4 - temp3 + 1440 < 15 or temp4 - temp3 + 1440 > 20)):
            popup_tag(simple_labels, 'ratio', (13, 1), (13, 6))
            b = False
    except ValueError:
        pass
    return b


def get_data_lines():
    lines = []
    for i in range(58):
        lines.append('')
    lines[0] = entries[0][0].get()
    lines[1] = simple_labels[0][1]['text']
    lines[2] = entries[1][0].get()
    lines[3] = entries[1][1].get()
    lines[4] = entries[1][2].get()
    lines[5] = entries[1][3].get()
    lines[6] = entries[2][0].get()
    lines[7] = entries[2][1].get()
    lines[8] = entries[4][0].get()
    lines[9] = entries[4][1].get()
    lines[10] = string_vars[0].get()
    lines[11] = entries[6][0].get()
    lines[12] = entries[7][0].get()
    lines[13] = entries[8][0].get()
    lines[14] = entries[8][1].get()
    lines[15] = entries[8][2].get()
    lines[16] = entries[8][3].get()
    lines[17] = entries[9][0].get()
    lines[18] = entries[9][1].get()
    lines[19] = entries[9][2].get()
    lines[20] = entries[9][3].get()
    lines[21] = entries[10][0].get()
    lines[22] = entries[10][1].get()
    lines[23] = entries[10][2].get()
    lines[24] = entries[10][3].get()
    lines[25] = entries[10][4].get()
    lines[26] = entries[11][0].get()
    lines[27] = entries[12][0].get()
    lines[28] = entries[13][0].get()
    lines[29] = entries[13][1].get()
    lines[30] = string_vars[1].get()
    lines[31] = str(int_vars[0].get())
    lines[32] = entries[13][2].get()
    lines[33] = entries[13][3].get()
    lines[34] = string_vars[2].get()
    lines[35] = entries[14][0].get()
    lines[36] = entries[14][1].get()
    lines[37] = str(int_vars[1].get())
    lines[38] = str(int_vars[2].get())
    lines[39] = string_vars[3].get()
    lines[40] = entries[14][2].get()
    lines[41] = simple_labels[14][5]['text']
    for i in range(42, 53):
        if entries[14][i - 39].get():
            lines[i] = simple_labels[14][i - 36].cget('text') + \
                       ':' + entries[14][i - 39].get()
    lines[53] = entries[15][0].get()
    lines[54] = entries[16][0].get()
    lines[55] = entries[16][1].get()
    lines[56] = entries[17][0].get()
    lines[57] = entries[17][1].get()
    return lines


def set_data_lines(lines):
    def set_line(entry, line):
        b = entry.cget('state') == 'disabled'
        if b:
            entry.config(state='normal')
        entry.delete(0, END)
        entry.insert(0, line)
        if b:
            entry.config(state='disabled')

    set_line(entries[0][0], lines[0])
    simple_labels[0][1]['text'] = lines[1]
    set_line(entries[1][0], lines[2])
    set_line(entries[1][1], lines[3])
    set_line(entries[1][2], lines[4])
    set_line(entries[1][3], lines[5])
    set_line(entries[2][0], lines[6])
    set_line(entries[2][1], lines[7])
    set_line(entries[4][0], lines[8])
    set_line(entries[4][1], lines[9])
    string_vars[0].set(lines[10])
    set_line(entries[6][0], lines[11])
    set_line(entries[7][0], lines[12])
    set_line(entries[8][0], lines[13])
    set_line(entries[8][1], lines[14])
    set_line(entries[8][2], lines[15])
    set_line(entries[8][3], lines[16])
    set_line(entries[9][0], lines[17])
    set_line(entries[9][1], lines[18])
    set_line(entries[9][2], lines[19])
    set_line(entries[9][3], lines[20])
    set_line(entries[10][0], lines[21])
    set_line(entries[10][1], lines[22])
    set_line(entries[10][2], lines[23])
    set_line(entries[10][3], lines[24])
    set_line(entries[10][4], lines[25])
    set_line(entries[11][0], lines[26])
    set_line(entries[12][0], lines[27])
    set_line(entries[13][0], lines[28])
    set_line(entries[13][1], lines[29])
    string_vars[1].set(lines[30])
    int_vars[0].set(lines[31])
    set_line(entries[13][2], lines[32])
    set_line(entries[13][3], lines[33])
    string_vars[2].set(lines[34])
    set_line(entries[14][0], lines[35])
    set_line(entries[14][1], lines[36])
    int_vars[1].set(lines[37])
    int_vars[2].set(lines[38])
    string_vars[3].set(lines[39])
    set_line(entries[14][2], lines[40])
    simple_labels[14][5]['text'] = lines[41]
    for i in range(42, 53):
        if lines[i]:
            simple_labels[14][i - 36].config(text=lines[i].split(':')[0])
            set_line(entries[14][i - 39], lines[i].split(':')[1])
        else:
            set_line(entries[14][i - 39], '')
    set_line(entries[15][0], lines[53])
    set_line(entries[16][0], lines[54])
    set_line(entries[16][1], lines[55])
    set_line(entries[17][0], lines[56])
    set_line(entries[17][1], lines[57])


def get_print_data(init):
    def get_date_line(line):
        month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        t = strptime(line, '%d.%m.%Y')
        return '%d %s %d г.' % (t.tm_mday, month[t.tm_mon - 1], t.tm_year)

    data = []
    for i in range(19):
        data.append([])
    data[0].append(init['Организация'])
    data[0].append(entries[0][0].get() + simple_labels[0][1]['text'])
    data[0].append(get_date_line(entries[4][0].get()))
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
        else:
            data[13].append('не проводилось')
    if int_vars[0].get():
        data[13][0] = checkbuttons[0]['text']
        data[13][1] = 'не проводилось'
    if entries[14][0].get():
        data[14].append('%s (%s)' % (entries[14][0].get(),
                                     entries[14][1].get()))
        data[14].append(init['Лаборатория'] + ', ' + string_vars[3].get())
        for i in range(3, 13):
            temp = entries[14][i].get()
            if temp:
                result = None
                if temp == minus:
                    result = 'отрицательный'
                if temp == plus:
                    result = 'положительный'
                data[14][1] += ', %s: %s' % (
                    simple_labels[14][i + 3]['text'], result)
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

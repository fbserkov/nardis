from tkinter.messagebox import showerror, showinfo, showwarning


dat_name = 'nardis.db'      # имя файла базы данных
exe_name = 'nardis.exe'     # имя файла приложения
pdf_name = 'nardis.pdf'     # имя pdf-файла для печати


def popup_name(name, line=''):
    # Сообщения
    if name == exe_name:
        if line:
            showerror('Ошибка', 'Не найдена метка:\n%s (%s)' % (line, name))
            #dqRoot()
            raise SystemExit
        else:
            showinfo('Сообщение', 'Приложение уже запущено:\n%s' % name)
    if name == pdf_name:
        showinfo('Сообщение', 'Необходимо закрыть:\n%s' % name)
    # Ошибки
    if name == dat_name:
        showinfo('Ошибка', 'Файл не найден:\n%s' % name)
        raise SystemExit


def popup_tag(simple_Ls, tag, item1, item2 = None):
    # Предупреждения
    lineA, lineB = simple_Ls[item1[0]][item1[1]]['text'], ''
    if item2:
        lineB = simple_Ls[item2[0]][item2[1]]['text']
    if tag == 'enter':
        line = 'Необходимо заполнить:\n%s' % lineA
        if lineB:
            line += '\n(%s)' % lineB
        showwarning('Предупреждение', line)
    if tag == 'select':
        line = 'Необходимо выбрать:\n%s' % lineA
        if lineB:
            line += '\n(%s)' % lineB
        showwarning('Предупреждение', line)
    if tag == 'format':
        line = 'Неверный формат:\n%s' % lineA
        if lineB:
            line += '\n(%s)' % lineB
        showwarning('Предупреждение', line)
    if tag == 'ratio':
        showwarning('Предупреждение',
                    'Неверное соотношение:\n%s\n%s' % (lineA, lineB))

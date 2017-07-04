from tkinter.messagebox import showerror, showinfo, showwarning


exe_name = 'nardis.exe'     # имя файла приложения
pdf_name = 'nardis.pdf'     # имя pdf-файла для печати


def popup_name(name, line=''):
    # Сообщения
    if name == exe_name:
        if line:
            showerror('Ошибка', 'Метка не найдена:\n%s (%s)' % (line, name))
            #dqRoot()
            raise SystemExit
    if name == pdf_name:
        showinfo('Сообщение', 'Документ необходимо закрыть:\n%s' % name)


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

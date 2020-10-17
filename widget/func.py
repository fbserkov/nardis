from time import strftime
from tkinter import END


def replace_plus(entry1, label, entry2):
    entry1.config(state='normal')
    replace(entry1, label)
    entry1.config(state='disabled')
    if not entry2.get():
        entry2.insert(0, strftime('%d.%m.%Y'))


def smart_add(entry, label, default):
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


def smart_replace(entry, label, default):
    entry.config(state='normal')
    if entry.get() == label['text']:
        entry.delete(0, END)
        entry.insert(0, default)
    else:
        entry.delete(0, END)
        entry.insert(0, label['text'])
    entry.config(state='disabled')

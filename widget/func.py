from tkinter import END


def smart_replace(entry, label, default):
    entry.config(state='normal')
    if entry.get() == label['text']:
        entry.delete(0, END)
        entry.insert(0, default)
    else:
        entry.delete(0, END)
        entry.insert(0, label['text'])
    entry.config(state='disabled')

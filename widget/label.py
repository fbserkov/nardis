from time import strftime
from tkinter import END, Label, LEFT, RIGHT


class LabelBase(Label):
    def __init__(self, master, text, bind, place=RIGHT):
        Label.__init__(
            self, master, text=text, fg='#000080',
            font='-size 10 -underline true'
        )
        if place == LEFT or place == RIGHT:
            self.pack(side=place)
        else:
            self.grid(**place)
        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)
        if type(bind) != tuple:  # TODO delete
            return
        if bind[0] == 'replace_smart':
            self.bind('<Button-1>', lambda e: self.replace_smart(
                e.widget, bind[1], bind[2]))
        elif bind[0] == 'add_smart':
            self.bind('<Button-1>', lambda e: self.add_smart(
                e.widget, bind[1], bind[2]))
        elif bind[0] == 'add':
            self.bind('<Button-1>', lambda e: self.add(e.widget, bind[1]))

    @staticmethod
    def add(label, entry):
        if entry.get().find(label['text']) == -1:
            entry.insert(END, label['text'] + ', ')

    @staticmethod
    def add_smart(label, entry, default):
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

    @staticmethod
    def enter(event):
        event.widget['font'] = '-size 10 -underline false'

    @staticmethod
    def leave(event):
        event.widget['font'] = '-size 10 -underline true'

    @staticmethod
    def replace(label, entry):
        entry.delete(0, END)
        entry.insert(0, label['text'])

    @staticmethod
    def replace_smart(label, entry, default):
        entry.config(state='normal')
        if entry.get() == label['text']:
            entry.delete(0, END)
            entry.insert(0, default)
        else:
            entry.delete(0, END)
            entry.insert(0, label['text'])
        entry.config(state='disabled')


class LabelReplace(LabelBase):
    def __init__(self, master, text, bind, place=RIGHT):
        LabelBase.__init__(self, master, text, bind, place)
        self.bind('<Button-1>', lambda e: self.replace(e.widget, bind))


class LabelReplace2(LabelBase):
    def __init__(self, master, text, bind, place=RIGHT):
        LabelBase.__init__(self, master, text, bind, place)
        self.bind('<Button-1>', lambda e: self.replace_2(
            e.widget, bind[0], bind[1]))

    def replace_2(self, label, entry, date):
        entry.config(state='normal')
        self.replace(label, entry)
        entry.config(state='disabled')
        if not date.get():
            date.insert(0, strftime('%d.%m.%Y'))

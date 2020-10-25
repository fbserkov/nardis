from time import strftime
from tkinter import END, Label, LEFT, OptionMenu, RIGHT, StringVar, X


class LabelBase(Label):
    def __init__(self, master, text, place=RIGHT):
        Label.__init__(
            self, master, text=text, fg='#000080',
            font='-size 10 -underline true',
        )
        if place == LEFT or place == RIGHT:
            self.pack(side=place)
        else:
            self.grid(**place)
        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

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


class LabelAdd(LabelBase):
    def __init__(self, master, text, bind, place=RIGHT):
        LabelBase.__init__(self, master, text, place)
        self.bind('<Button-1>', lambda e: self.add(e.widget, bind))

    @staticmethod
    def add(label, entry):
        if entry.get().find(label['text']) == -1:
            entry.insert(END, label['text'] + ', ')


class LabelAddSmart(LabelBase):
    def __init__(self, master, text, bind, place=RIGHT):
        LabelBase.__init__(self, master, text, place)
        self.bind('<Button-1>', lambda e: self.add_smart(
            e.widget, bind[0], bind[1]))

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


class LabelReplace(LabelBase):
    def __init__(self, master, text, bind, place=RIGHT):
        LabelBase.__init__(self, master, text, place)
        self.bind('<Button-1>', lambda e: self.replace(e.widget, bind))


class LabelReplaceSmart(LabelBase):
    def __init__(self, master, text, bind, place=RIGHT):
        LabelBase.__init__(self, master, text, place)
        self.bind('<Button-1>', lambda e: self.replace_smart(
            e.widget, bind[0], bind[1]))

    @staticmethod
    def replace_smart(label, entry, default):
        to_default = False
        entry.config(state='normal')
        if entry.get() == label['text']:
            entry.delete(0, END)
            entry.insert(0, default)
            to_default = True
        else:
            entry.delete(0, END)
            entry.insert(0, label['text'])
        entry.config(state='disabled')
        return to_default


class LabelReplaceSmartDate(LabelReplaceSmart):
    def __init__(self, master, text, bind, place=RIGHT):
        LabelBase.__init__(self, master, text, place)
        self.bind('<Button-1>', lambda e: self.replace_smart_date(
            e.widget, bind[0], bind[1], bind[2]))

    def replace_smart_date(self, label, entry, default, date):
        if self.replace_smart(label, entry, default):
            date.delete(0, END)
            return
        if len(date.get()) < 10:
            date.delete(0, END)
            date.insert(0, strftime('%d.%m.%Y'))


class OptionMenuSmart(OptionMenu):
    def __init__(self, master, values, default=None):
        string_var = StringVar(master)
        if default:
            string_var.set(default)
        OptionMenu.__init__(self, master, string_var, *values)
        self.config(font='-size 10', fg='#800000')
        self.pack(fill=X)

from time import strftime
from tkinter import END, Entry, Label, LEFT, OptionMenu, RIGHT, StringVar, X


class EntryBase(Entry):
    def __init__(self, master, width=None, default=None):
        Entry.__init__(self, master, font='-size 10', fg='#800000')
        self.default = default
        if width:
            self['width'] = width

    def init(self):
        self.delete(0, END)
        if self.default:
            self.insert(0, self.default)


class EntryDisabled(EntryBase):  # TODO default logic
    def __init__(self, master, width=None, default=None):
        EntryBase.__init__(self, master, width)
        if default:
            self.insert(0, default)
        self.config(state='disabled', disabledforeground='#800000')


class EntrySmart(EntryBase):
    def __init__(self, master, width, default=None):
        EntryBase.__init__(self, master, width=width, default=default)
        self.length, self.default, self.separator = width, default, '.'
        self.bind('<KeyRelease>', self.key_release)

    def init(self):
        self.delete(0, END)
        if self.default:
            self.insert(0, strftime(self.default))

    def key_release(self, event):
        length = len(event.widget.get())
        if self.condition(length):
            event.widget.insert(END, self.separator)
        if length > self.length:
            event.widget.delete(self.length, END)

    @staticmethod
    def condition(_):
        assert False, 'method must be overridden'


class EntryDate(EntrySmart):
    def __init__(self, master, default=None):
        EntrySmart.__init__(self, master, width=10, default=default)
        self.condition = lambda length: length == 2 or length == 5
        self.pack(side=LEFT)


class EntryResult(EntrySmart):
    def __init__(self, master):
        EntrySmart.__init__(self, master, width=4)
        self.condition = lambda length: length == 1
        self.pack(side=LEFT)


class EntryTime(EntrySmart):
    def __init__(self, master, default=None):
        EntrySmart.__init__(self, master, width=5, default=default)
        self.separator = ':'
        self.condition = lambda length: length == 2
        self.pack(side=LEFT)


class EntryYear(EntrySmart):
    def __init__(self, master, default=None):
        EntrySmart.__init__(self, master, width=2, default=default)
        self.condition = lambda length: False


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
        self.string_var, self.default = StringVar(master), default
        OptionMenu.__init__(self, master, self.string_var, *values)
        self.config(font='-size 10', fg='#800000')
        self.pack(fill=X)

    def init(self):
        if self.default:
            self.string_var.set(self.default)
        else:
            self.string_var.set('')

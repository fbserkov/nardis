from time import strftime, strptime
from tkinter import (
    Checkbutton, END, Entry, IntVar, Label, LEFT, Listbox,
    MULTIPLE, OptionMenu, RIGHT, StringVar, Text, X,
)


class CheckbuttonSmart(Checkbutton):
    def __init__(self, master, line, default=0):
        self.default, self._int_var = default, IntVar(master)
        Checkbutton.__init__(
            self, master, text=line,
            variable=self._int_var, onvalue=1, offvalue=0,
        )

    @staticmethod
    def check(_):
        pass

    def get(self):
        return self._int_var.get()

    def init(self):
        self._int_var.set(self.default)

    def set(self, value):
        return self._int_var.set(value)


class EntryBase(Entry):
    def __init__(self, master, width=None, default=None):
        Entry.__init__(self, master, font='-size 10', fg='#800000')
        self.default = default
        if width:
            self['width'] = width

    def check(self, _):
        return not self.get()

    def init(self, line=None):
        self.delete(0, END)
        if line is not None:
            self.insert(0, line)
        elif self.default:
            self.insert(0, self.default)


class EntryDisabled(EntryBase):
    def __init__(self, master, width=None, default=None):
        EntryBase.__init__(self, master, width, default)
        self.config(state='disabled', disabledforeground='#800000')

    def init(self, line=None):
        self.config(state='normal')
        EntryBase.init(self, line)
        self.config(state='disabled')


class EntrySmart(EntryBase):
    def __init__(self, master, width, default=None):
        EntryBase.__init__(self, master, width, default)
        self.length, self.default, self.separator = width, default, '.'
        self.condition = lambda length: False
        self.bind('<KeyRelease>', self.key_release)

    def check(self, exc):
        if EntryBase.check(self, exc):
            return True
        if len(self.get()) < self.length:
            raise exc

    def init(self, line=None):
        self.delete(0, END)
        if line is not None:
            self.insert(0, line)
        elif self.default:
            self.insert(0, strftime(self.default))

    def key_release(self, event):
        length = len(event.widget.get())
        if self.condition(length):
            event.widget.insert(END, self.separator)
        if length > self.length:
            event.widget.delete(self.length, END)


class EntryDate(EntrySmart):
    def __init__(self, master, default=None):
        EntrySmart.__init__(self, master, width=10, default=default)
        self.condition = lambda length: length == 2 or length == 5
        self.pack(side=LEFT)

    def check(self, exc):
        exc.add('Неверно указана дата')
        if EntrySmart.check(self, exc):
            return
        try:
            strptime(self.get(), '%d.%m.%Y')
        except ValueError:
            raise exc


class EntryResult(EntrySmart):
    def __init__(self, master):
        EntrySmart.__init__(self, master, width=4)
        self.condition = lambda length: length == 1
        self.pack(side=LEFT)

    def check(self, exc):
        exc.add('Неверно указан результат')
        if EntrySmart.check(self, exc):
            return
        try:
            float(self.get())
        except ValueError:
            raise exc


class EntryTime(EntrySmart):
    def __init__(self, master, default=None):
        EntrySmart.__init__(self, master, width=5, default=default)
        self.separator = ':'
        self.condition = lambda length: length == 2
        self.pack(side=LEFT)

    def check(self, exc):
        exc.add('Неверно указано время')
        if EntrySmart.check(self, exc):
            return
        try:
            strptime(self.get(), '%H:%M')
        except ValueError:
            raise exc


class EntryTimer(EntrySmart):
    def __init__(self, master):
        EntrySmart.__init__(self, master, width=2)

    def check(self, exc):
        exc.add('Неверно указаны секунды')
        if EntryBase.check(self, exc):
            return
        if not self.get().isdigit():
            raise exc


class EntryYear(EntrySmart):
    def __init__(self, master, default=None):
        EntrySmart.__init__(self, master, width=2, default=default)

    def check(self, exc):
        exc.add('Неверно указан год')
        if EntrySmart.check(self, exc):
            return
        if not self.get().isdigit():
            raise exc


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


class ListboxSmart(Listbox):
    def __init__(self, master, sign, choices):
        Listbox.__init__(
            self, master, height=5, selectmode=MULTIPLE, exportselection=False,
            font='-size 10', fg='#800000', selectforeground='#800000',
        )
        self.sign, self.choices = sign, choices

    @staticmethod
    def check(_):
        pass

    def get_result(self, result):
        for index in self.curselection():
            result[self.get(index)] = self.sign

    def init(self):
        self.selection_clear(0, END)
        self['listvariable'] = StringVar(self.master, value=self.choices)

    def set_result(self, result):
        for index, choice in enumerate(self.choices):
            if result.get(choice) == self.sign:
                self.selection_set(index)
        for key in result:
            if key not in self.choices:
                if result[key] == self.sign:
                    self.insert(END, key)
                    self.selection_set(self.index(END) - 1)

    def update_choices(self, choices):
        self.selection_clear(0, END)
        self.choices = choices
        self['listvariable'] = StringVar(self.master, value=self.choices)


class OptionMenuSmart(OptionMenu):
    def __init__(self, master, values):
        self.string_var = StringVar(master)
        OptionMenu.__init__(self, master, self.string_var, *values)
        self.config(
            font='-size 10', fg='#800000', disabledforeground='#800000')
        self['menu'].config(
            font='-size 10', fg='#800000', activeforeground='#800000')
        self.pack(fill=X)

    @staticmethod
    def check(_):
        pass

    def init(self):
        if self['state'] == 'normal':
            self.string_var.set('')


class TextSmart(Text):
    def __init__(self, master, height):
        Text.__init__(
            self, master, height=height, font='-size 10', fg='#800000')

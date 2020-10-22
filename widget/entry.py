from tkinter import Entry, LEFT, END


class EntryBase(Entry):
    def __init__(self, master, width=None):
        Entry.__init__(self, master, font='-size 10', fg='#800000')
        if width:
            self['width'] = width


class EntryDisabled(EntryBase):
    def __init__(self, master, width=None, default=None):
        EntryBase.__init__(self, master, width)
        if default:
            self.insert(0, default)
        self.config(state='disabled', disabledforeground='#800000')


class EntrySmart(EntryBase):
    def __init__(self, master, width, default=None):
        self.length, self.separator = width, '.'
        EntryBase.__init__(self, master, width=self.length)
        if default:
            self.insert(0, default)
        self.pack(side=LEFT)
        self.bind('<KeyRelease>', self.key_release)

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


class EntryResult(EntrySmart):
    def __init__(self, master):
        EntrySmart.__init__(self, master, width=4)
        self.condition = lambda length: length == 1


class EntryTime(EntrySmart):
    def __init__(self, master, default=None):
        EntrySmart.__init__(self, master, width=5, default=default)
        self.separator = ':'
        self.condition = lambda length: length == 2

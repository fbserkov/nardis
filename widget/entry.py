from tkinter import Entry, LEFT, END


class EntryBase(Entry):
    def __init__(self, master, width, text=None):
        self.length, self.separator = width, '.'
        Entry.__init__(
            self, master, width=self.length, font='-size 10', fg='#800000')
        if text:
            self.insert(0, text)
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


class EntryDate(EntryBase):
    def __init__(self, master, text=None):
        EntryBase.__init__(self, master, width=10, text=text)
        self.condition = lambda length: length == 2 or length == 5


class EntryResult(EntryBase):
    def __init__(self, master):
        EntryBase.__init__(self, master, width=4)
        self.condition = lambda length: length == 1


class EntryTime(EntryBase):
    def __init__(self, master, text=None):
        EntryBase.__init__(self, master, width=5, text=text)
        self.separator = ':'
        self.condition = lambda length: length == 2
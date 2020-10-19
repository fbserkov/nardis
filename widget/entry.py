from tkinter import Entry, LEFT, END


class EntryDate(Entry):
    def __init__(self, master, text=None):
        Entry.__init__(self, master, width=10, font='-size 10', fg='#800000')
        self.pack(side=LEFT)
        if text:
            self.insert(0, text)
        self.bind('<KeyRelease>', self.key_release_date)

    @staticmethod
    def key_release_date(event):
        length = len(event.widget.get())
        if length == 2 or length == 5:
            event.widget.insert(END, '.')
        if length > 10:
            event.widget.delete(10, END)


class EntryResult(Entry):
    def __init__(self, master):
        Entry.__init__(self, master, width=4, font='-size 10', fg='#800000')
        self.pack(side=LEFT)
        self.bind('<KeyRelease>', self.key_release_result)

    @staticmethod
    def key_release_result(event):
        length = len(event.widget.get())
        if length == 1:
            event.widget.insert(END, '.')
        if length > 4:
            event.widget.delete(4, END)


class EntryTime(Entry):
    def __init__(self, master, text=None):
        Entry.__init__(self, master, width=5, font='-size 10', fg='#800000')
        self.pack(side=LEFT)
        if text:
            self.insert(0, text)
        self.bind('<KeyRelease>', self.key_release_time)

    @staticmethod
    def key_release_time(event):
        length = len(event.widget.get())
        if length == 2:
            event.widget.insert(END, ':')
        if length > 5:
            event.widget.delete(5, END)

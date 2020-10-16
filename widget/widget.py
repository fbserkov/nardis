import time
from tkinter import END, Entry, Label, LEFT


class DateEntry(Entry):
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


class SmartLabel(Label):
    def __init__(self, master, text):
        Label.__init__(
            self, master, text=text, fg='#000080',
            font='-size 10 -underline true'
        )
        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

    @staticmethod
    def enter(event):
        event.widget['font'] = '-size 10 -underline false'

    @staticmethod
    def leave(event):
        event.widget['font'] = '-size 10 -underline true'


class TimeEntry(Entry):
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

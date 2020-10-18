from time import strftime
from tkinter import END, Entry, Frame, Label, LEFT, RIGHT, X


def get_frames(master, length):
    frames = []
    for i in range(length):
        frame = Frame(master)
        frame.pack(fill=X)
        frames.append(frame)
    return frames


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


class ResultEntry(Entry):
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


class SmartLabel(Label):
    def __init__(self, master, text, place=RIGHT, bind=None):  # TODO: del None
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
        if not bind:  # TODO: delete this if
            return
        if bind[0] == 'add_smart':
            self.bind('<Button-1>', lambda e: self.add_smart(
                e.widget, bind[1], bind[2]))
        elif bind[0] == 'replace':
            self.bind('<Button-1>', lambda e: self.replace(e.widget, bind[1]))
        elif bind[0] == 'add':
            self.bind('<Button-1>', lambda e: self.add(e.widget, bind[1]))
        elif bind[0] == 'replace_2':
            self.bind('<Button-1>', lambda e: self.replace_2(
                e.widget, bind[1], bind[2]))

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

    def replace_2(self, label, entry, date):
        entry.config(state='normal')
        self.replace(label, entry)
        entry.config(state='disabled')
        if not date.get():
            date.insert(0, strftime('%d.%m.%Y'))


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

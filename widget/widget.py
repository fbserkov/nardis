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
    def __init__(self, master, text, place=RIGHT, entry=None, bind=None):  # TODO don't Nones
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
        if entry:  # TODO add and bind, delete if
            self.bind('<Button-1>', lambda e: self.add(entry, e.widget))

    @staticmethod
    def enter(event):
        event.widget['font'] = '-size 10 -underline false'

    @staticmethod
    def leave(event):
        event.widget['font'] = '-size 10 -underline true'

    @staticmethod
    def add(entry, label):
        if entry.get().find(label['text']) == -1:
            entry.insert(END, label['text'] + ', ')


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

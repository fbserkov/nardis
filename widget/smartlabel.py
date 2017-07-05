from tkinter import Label


class SmartLabel(Label):
    def __init__(self, master, text):
        Label.__init__(self, master, text=text, fg='#000080',
                       font='-size 10 -underline true')
        self.bind('<Enter>', enter)
        self.bind('<Leave>', leave)


def enter(event):
    event.widget['font'] = '-size 10 -underline false'


def leave(event):
    event.widget['font'] = '-size 10 -underline true'

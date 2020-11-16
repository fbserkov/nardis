from tkinter import (
    Button, E, Frame, Listbox, RIGHT, Scrollbar, StringVar, W, X, Y)
from part import CommonPart, ExaminationPart, PassportPart, SurveyPart


class SubFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.is_visible = False

    def hide(self):
        self.forget()
        self.is_visible = False

    def show(self):
        self.pack(fill=X)
        self.is_visible = True


class ActsList(Frame):
    def __init__(self, app):
        Frame.__init__(self, bd=4)
        self._app, self._choices, self.is_visible = app, StringVar(), False

        listbox = Listbox(master=self, listvariable=self._choices, height=32)
        scrollbar = Scrollbar(self, command=listbox.yview)
        listbox['yscrollcommand'] = scrollbar.set

        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.pack(fill=X)
        listbox.bind(
            '<Double-1>', lambda e: app.init(e.widget.curselection()[0]))
        listbox.bind('<Double-1>', lambda _: app.menu.switch_list(), add='+')

    def _update(self):
        self._choices.set(self._app.db.get_acts_titles())

    def hide(self):
        self.forget()
        self.is_visible = False

    def show(self):
        self._update()
        self.pack(fill=X)
        self.is_visible = True


class FormParts(Frame):
    def __init__(self):
        Frame.__init__(self)
        self._index, self.is_visible = 0, False  # TODO is_visible isn't use

        frame = Frame(self)
        self._buttons = (
            Button(frame, text='I'), Button(frame, text='II'),
            Button(frame, text='III'), Button(frame, text='IV'),
        )
        min_width = max(button.winfo_reqwidth() for button in self._buttons)
        for i, button in enumerate(self._buttons):
            frame.columnconfigure(i, weight=1, minsize=min_width)
            button.grid(row=0, column=i, sticky=E + W)
            button['command'] = lambda j=i: self._switch_part(j + 1)
        frame.pack(fill=X)

        self._parts = (
            PassportPart(self), CommonPart(self),
            SurveyPart(self), ExaminationPart(self),
        )

    def _switch_part(self, index):
        if self._index == index:
            return
        self._parts[self._index - 1].forget()
        self._buttons[self._index - 1].config(font='-size 10')
        if index:
            self._parts[index - 1].pack(fill=X)
            self._buttons[index - 1].config(font='-size 10 -weight bold')
        self._index = index

    def check(self):
        for part in self._parts:
            part.check()

    def init(self):
        for part in self._parts:
            part.init()
        self._parts[0].update()

    def insert(self):
        for part in self._parts:
            for item in part.items.values():
                item.insert()

    def hide(self):
        self.forget()
        self.is_visible = False

    def select(self):
        for part in self._parts:
            for item in part.items.values():
                item.select()

    def show(self):
        self._switch_part(1)
        self.pack(fill=X)
        self.is_visible = True


class Settings(SubFrame):
    def __init__(self):
        SubFrame.__init__(self)

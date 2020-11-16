from tkinter import (
    Button, E, END, Entry, Frame, Label, LEFT, Listbox,
    N, RIGHT, Scrollbar, StringVar, Text, W, X, Y,
)
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


class ActsList(SubFrame):
    def __init__(self, app):
        SubFrame.__init__(self)
        self['bd'] = 4
        self._app, self._choices = app, StringVar()

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

    def show(self):
        self._update()
        SubFrame.show(self)


class FormParts(SubFrame):
    def __init__(self):
        SubFrame.__init__(self)
        self._index = 0

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

    def select(self):
        for part in self._parts:
            for item in part.items.values():
                item.select()

    def show(self):
        self._switch_part(1)
        SubFrame.show(self)


class Settings(SubFrame):
    def __init__(self, db):
        self.db = db
        SubFrame.__init__(self)

        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        Label(frame, text='Организация:').pack(side=LEFT, anchor=N)
        self.organization = Text(frame, height=5)
        self.organization.pack()

        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        Label(frame, text='Подразделение:').pack(side=LEFT)
        self.subdivision = StringVar(frame)
        Entry(frame, textvariable=self.subdivision).pack(fill=X)

    def hide(self):
        self.save()
        SubFrame.hide(self)

    def init(self):
        self.organization.delete('1.0', END)
        self.organization.insert('1.0', self.db.select('organization'))
        self.subdivision.set(self.db.select('subdivision'))

    def save(self):
        self.db.insert(
            'organization', self.organization.get('1.0', END + '-1c'))
        self.db.insert('subdivision', self.subdivision.get())
        self.db.save_settings()

    def show(self):
        self.init()
        SubFrame.show(self)

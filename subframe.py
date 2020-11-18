from tkinter import (
    Button, E, END, Frame, Label, LEFT, Listbox, N,
    RIGHT, S, Scrollbar, StringVar, Text, W, X, Y,
)

# from item import CheckException
from part import CommonPart, ExaminationPart, PassportPart, SurveyPart
from widget import CheckbuttonSmart, EntryBase


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

    def update_menu(self):
        self._parts[0].update_menu()
        self._parts[3].update_menu()


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
        self.subdivision = EntryBase(frame)
        self.subdivision.pack(fill=X)

        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        Label(frame, text='Врачи:').pack(side=LEFT, anchor=N)
        self.doctors = Text(frame, height=5)
        self.doctors.pack()

        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        Label(frame, text='Технические средства:').pack(side=LEFT, anchor=N)
        self.devices = Text(frame, height=5)
        self.devices.pack()

        frame = Frame(self, bd=4)
        frame.pack(fill=X)
        Label(frame, text='Лаборатория:').pack(side=LEFT)
        self.laboratory = EntryBase(frame)
        self.laboratory.pack(fill=X)

        sup_frame = Frame(self)
        sup_frame.columnconfigure(0, weight=1)
        sup_frame.columnconfigure(1, weight=1)
        sup_frame.pack(fill=X)

        frame = Frame(sup_frame, bd=4)
        frame.grid(row=0, column=0, rowspan=3)
        Label(frame, text='Вещества:').pack(anchor=W)
        self.substances = Text(frame, height=12)
        self.substances.pack()

        frame = Frame(sup_frame, bd=4)
        frame.grid(row=0, column=1, sticky=N)
        Label(frame, text='Методы исследования:').pack(anchor=W)
        self.methods = Text(frame, height=8)
        self.methods.pack()

        frame = Frame(sup_frame, bd=4)
        frame.grid(row=1, column=1)
        Label(frame, text='Номер следующего акта:').pack(side=LEFT)
        self.next_number = EntryBase(frame)
        self.next_number.pack()

        frame = Frame(sup_frame, bd=4)
        frame.grid(row=2, column=1, sticky=S)
        Label(frame, text='Пароль:').pack(side=LEFT)
        self.button = CheckbuttonSmart(frame, line='скрыть', default=1)
        self.button['command'] = self._switch_entry
        self.button.pack(side=RIGHT)
        self.password = EntryBase(frame)
        self.password.pack(side=RIGHT)

    def _switch_entry(self):
        self.password['show'] = '●' if self.button.get() else ''

    def check(self):
        # raise CheckException('Здесь могла быть ваша реклама.')  # TODO
        pass

    def hide(self):
        SubFrame.hide(self)

    def init(self):
        self.organization.delete('1.0', END)
        self.organization.insert('1.0', self.db.select('organization'))

        self.subdivision.init(self.db.select('subdivision'))

        self.doctors.delete('1.0', END)
        self.doctors.insert(
            '1.0', '\n'.join(
                k + ': ' + v for k, v in self.db.select('doctors').items()))

        self.devices.delete('1.0', END)
        self.devices.insert('1.0', '\n'.join(self.db.select('devices')))

        self.laboratory.init(self.db.select('laboratory'))

        self.substances.delete('1.0', END)
        self.substances.insert('1.0', '\n'.join(self.db.select('substances')))

        self.methods.delete('1.0', END)
        self.methods.insert('1.0', '\n'.join(self.db.select('methods')))

        self.next_number.init(self.db.select('next_number'))

        self.button.init()
        self._switch_entry()
        self.password.init(self.db.select('password'))

    def save(self):
        self.db.insert(
            'organization', self.organization.get('1.0', END + '-1c'))

        self.db.insert('subdivision', self.subdivision.get())

        self.db.insert(
            'doctors', dict(
                doctor.split(': ') for doctor
                in self.doctors.get('1.0', END + '-1c').split('\n')
            )
        )

        self.db.insert(
            'devices', self.devices.get('1.0', END + '-1c').split('\n'))

        self.db.insert('laboratory', self.laboratory.get())

        self.db.insert(
            'substances', self.substances.get('1.0', END + '-1c').split('\n'))

        self.db.insert(
            'methods', self.methods.get('1.0', END + '-1c').split('\n'))

        self.db.insert('next_number', self.next_number.get())

        self.db.insert('password', self.password.get())

        self.db.save_settings()

    def show(self):
        SubFrame.show(self)

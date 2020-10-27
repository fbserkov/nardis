from tkinter import Button, Entry, OptionMenu, StringVar, X
from window.window import WindowBase


class WindowAuth(WindowBase):
    def __init__(self, database):
        WindowBase.__init__(self)
        self.root.title('Введите пароль')

        years = database.get_years()
        sv = StringVar(self.root)
        sv.set(years[-1])
        om = OptionMenu(self.root, sv, *years)
        om.config(font='-size 10', fg='#800000')
        om.pack(fill=X)

        def cb():
            if database.authentication(e.get(), int(sv.get())):
                self.root.destroy()
                self.root.quit()
        e = Entry(self.root, font='-size 14', show='●')
        e.bind('<Key-Return>', lambda _: cb())
        e.pack()
        e.focus()

        Button(self.root, font='-size 10', text='OK', command=cb).pack(fill=X)
        self.centering(width=200, height=88)
        self.root.mainloop()

from tkinter import OptionMenu, StringVar, X


class OptionMenuSmart(OptionMenu):
    def __init__(self, master, values, default=None):
        string_var = StringVar(master)
        if default:
            string_var.set(default)
        OptionMenu.__init__(self, master, string_var, *values)
        self.config(font='-size 10', fg='#800000')
        self.pack(fill=X)

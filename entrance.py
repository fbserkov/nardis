import sys
from tkinter import Button, Entry, OptionMenu, StringVar, Tk, X


class Entrance:
    def __init__(self, database):
        root = Tk()
        root.title('Введите пароль')
        if not sys.platform == 'linux':
            root.iconbitmap('nardis.ico')

        years = database.get_years()
        sv = StringVar(root)
        sv.set(years[-1])
        om = OptionMenu(root, sv, *years)
        om.config(font='-size 10', fg='#800000')
        om.pack(fill=X)

        def cb():
            if database.authentication(e.get(), int(sv.get())):
                root.destroy()
                root.quit()
        e = Entry(root, font='-size 14', show='●')
        e.bind('<Key-Return>', lambda _: cb())
        e.pack()
        e.focus()

        Button(root, font='-size 10', text='OK', command=cb).pack(fill=X)
        centering(root, width=200, height=88)
        root.mainloop()


def centering(root, width, height):
    if not (width and height):
        root.update()
        width = root.winfo_width()
        height = root.winfo_height()
        print('%dx%d' % (width, height))

    if sys.platform == 'linux':
        frame, title = 0, 37    # Ubuntu
    else:
        frame, title = 3, 26    # Windows XP

    left = (root.winfo_screenwidth() - (width + 2 * frame)) / 2
    top = (root.winfo_screenheight() - (height + 2 * frame + title)) / 2
    root.geometry('%dx%d+%d+%d' % (width, height, left, top))
    root.resizable(False, False)

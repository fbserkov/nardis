from tkinter import END


def bind_entries_events(entries):

    def cb_key_release_date(event):
        l = len(event.widget.get())
        if l == 2 or l == 5:
            event.widget.insert(END, '.')
        if l > 10:
            event.widget.delete(10, END)

    def cb_key_release_time(event):
        l = len(event.widget.get())
        if l == 2:
            event.widget.insert(END, ':')
        if l > 5:
            event.widget.delete(5, END)

    def cb_key_release_result(event):
        l = len(event.widget.get())
        if l == 1:
            event.widget.insert(END, '.')
        if l > 4:
            event.widget.delete(4, END)

    entries[1][1].bind('<KeyRelease>',  cb_key_release_date)
    entries[4][0].bind('<KeyRelease>',  cb_key_release_date)
    entries[4][1].bind('<KeyRelease>',  cb_key_release_time)
    entries[13][0].bind('<KeyRelease>', cb_key_release_time)
    entries[13][1].bind('<KeyRelease>', cb_key_release_result)
    entries[13][2].bind('<KeyRelease>', cb_key_release_time)
    entries[13][3].bind('<KeyRelease>', cb_key_release_result)
    entries[14][0].bind('<KeyRelease>', cb_key_release_time)
    entries[16][0].bind('<KeyRelease>', cb_key_release_date)
    entries[16][1].bind('<KeyRelease>', cb_key_release_time)
    entries[17][1].bind('<KeyRelease>', cb_key_release_date)

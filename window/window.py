import sys
from tkinter import Tk


class Window:
    def __init__(self):
        self.root = Tk()
        if not sys.platform == 'linux':
            self.root.iconbitmap('nardis.ico')

    def centering(self, width=0, height=0):
        if not (width and height):
            self.root.update()
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            print('{}x{}'.format(width, height))
        if sys.platform == 'linux':
            frame, title = 0, 37  # Ubuntu
        else:
            frame, title = 3, 26  # Windows XP
        left = (self.root.winfo_screenwidth() - (width + 2 * frame)) / 2
        top = (self.root.winfo_screenheight() - (height + 2 * frame + title)) / 2
        self.root.geometry('%ix%i+%i+%i' % (width, height, left, top))
        self.root.resizable(False, False)

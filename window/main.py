from window.window import Window


class Main(Window):
    def __init__(self):
        Window.__init__(self)
        self.root.title('Наркологическая экспертиза')
        self.centering()    # было 551x672 (высота < 768)
        self.root.mainloop()

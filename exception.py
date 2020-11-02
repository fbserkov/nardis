class CheckException(Exception):
    def __init__(self):
        self.text = ''

    def add(self, text):
        self.text += text

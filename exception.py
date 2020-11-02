class CheckException(Exception):
    def __init__(self, text):
        self.text = text

    def add(self, text):
        self.text += text

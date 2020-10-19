from tkinter import Frame, X


def get_frames(master, length):
    frames = []
    for i in range(length):
        frame = Frame(master)
        frame.pack(fill=X)
        frames.append(frame)
    return frames

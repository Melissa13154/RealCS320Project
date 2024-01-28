import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage

backgroundColor = "#D1FFB0"

class StartingLabel:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(self.root, text = "Click button below to start timer", font=('MS Sans Serif', 20), bg= backgroundColor)
        self.label.place(relx=.5, rely=.1, anchor="center")


class StartButton:
    def __init__(self, root):
        self.root = root
        self.button = tk.Button(self.root, text = "Start", width=15, command=self.handleMouseClick)
        self.button.place(relx= 0.5, rely = 0.8, anchor='n')
        self.clicks = 0

    #changes text back and forth each click (kind of scuffed but it works)
    def handleMouseClick(self):
        self.clicks = self.clicks+1

        if((self.clicks)%2 != 0):
            self.button.config(text = "Stop")
        else:
            self.button.config(text = "Start")


class Timer:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(self.root, text="00:00", font=('MS Sans Serif', 20), bg=backgroundColor)
        self.label.place(relx= 0.5, rely=0.75, anchor='center')


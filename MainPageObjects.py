import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage
from datetime import datetime

backgroundColor = "#D1FFB0"

class StartingLabel:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(self.root, text = "Enter a time and click start", font=('MS Sans Serif', 20), bg= backgroundColor)
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

        if(self.clicks%2 != 0):
            self.button.config(text = "Stop")
        else:
            self.button.config(text = "Start")

            

class TimerTimeOptions:
    def __init__(self, root):
        self.root = root

        self.timeOptions = ('00:10:00',
                            '00:15:00',
                            '00:20:00',
                            '00:30:00',
                            '00:45:00',
                            '01:00:00')

        self.menu = tk.OptionMenu(self.root, tk.StringVar(self.root), self.timeOptions[0], *self.timeOptions)
        self.menu.pack() #just throwing it in for now



class Timer:
    def __init__(self, root):
        self.root = root

        self.timeLeft = "00-15-00"
        self.timeLeftLabel = str(datetime.strptime(self.timeLeft, "%H-%M-%S"))
        self.timeLeftLabel = self.timeLeftLabel.split()
        self.timeLeftLabel = self.timeLeftLabel[1]
        
        self.label = tk.Label(self.root, text=self.timeLeftLabel, font=('MS Sans Serif', 20), bg=backgroundColor)
        self.label.place(relx= 0.5, rely=0.75, anchor='center')

    def countDown(self):
        pass
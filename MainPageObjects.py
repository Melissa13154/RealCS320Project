import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage
from datetime import datetime

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
        now = datetime.now()    # Not sure if this is the right place to put this
                                # Use now() function to get datatime obj containing date and time - LPC

        self.clicks = self.clicks+1

        if((self.clicks)%2 != 0):
            self.button.config(text = "Stop")
            stopTimeAsString = 0
            stopTimeAsString = now.strftime("%H%M") # Attempting to capture stop time when "stop" is clicked - LPC
            stopTime = int(stopTimeAsString)

            if stopTime != 0:
                timeElapsed = (stopTime - startTime) # Might actually need to convert these from strings to ints? - LPC
                # timer.label = timeElapsed TODO: Change label to show time elapsed rather than 00:00

        else:
            self.button.config(text = "Start")
            startTimeAsString = now.strftime("%H%M") # Attempting to capture the start time when "start" is clicked - LPC
            startTime = int(startTimeAsString)

class Timer:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(self.root, text="00:00", font=('MS Sans Serif', 20), bg=backgroundColor)
        self.label.place(relx= 0.5, rely=0.75, anchor='center')


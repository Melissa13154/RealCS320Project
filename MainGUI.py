import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import * # Is this necessary?
from tkinter import ttk # For accessing Notebook widget

import MainPageObjects
import TimerObject

backgroundColor = "#D1FFB0"

TK_SILENCE_DEPRECATION=1 #suppress warnings

class MainFrame:
    def __init__(self):
        self.root = tk.Tk() #creates main root
        self.root.config(bg= backgroundColor)
        self.root.title("Track Timer 1.0.0") #title display at the top
        self.root.geometry('500x700') #inital dimensions of window

        notebook = ttk.Notebook(self.root)
        tab1 = Frame(notebook)
        tab2 = Frame(notebook)
        notebook.add(tab1, text = "Main")
        notebook.add(tab2, text = "Goal Dash")
        notebook.pack()
        Label(tab2, text = "The Goal Dashboard will go here.", width = 50, height = 50).pack()

        #image of clock    
        self.image1 = Canvas(self.root, width =350, height=350)
        self.image1.place(relx=.5, rely=.4, anchor="center")
        self.photo1 = PhotoImage(file='Images/Clock2-resized.gif') #TODO: Figure out how to make corners transparent
        self.image1.create_image((1, 1), anchor='nw',image= self.photo1)

main = MainFrame()
mainLabel = MainPageObjects.StartingLabel(main.root)
timer = TimerObject.Timer(main.root)
goalDashboardButton = MainPageObjects.GoalDashboardButton(main.root)

main.root.mainloop() 
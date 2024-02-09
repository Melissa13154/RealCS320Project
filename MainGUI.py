import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import * # Is this necessary?
from tkinter import ttk # For accessing Notebook widget

import MainPageObjects
import TimerObject
import TimerFrameObject

backgroundColor = "#3A7069"

TK_SILENCE_DEPRECATION=1 #suppress warnings

class MainFrame(tk.Tk):
    def __init__(self):
        #self.root = ?
        container = tk.Frame(self)

noteBock = MainFrame()
TimerFrame = TimerFrameObject.TimerFrame(MainFrame.root)
timer = TimerObject.Timer(MainFrame.root)
goalDashboardButton = MainPageObjects.GoalDashboardButton(MainFrame.root)

main.root.mainloop() 

### IMPORTS ###
import tkinter as tk
from tkinter import *
from tkinter import ttk # For accessing Notebook widget

import TimerObject
import TimerTags
import GoalsTabObjects

### DETAILS ###
TK_SILENCE_DEPRECATION=1 # Supress warnings
backgroundColor = "#3A7069"

#s = ttk.Style()
#s.configure('TFrame', background='red')

class OuterFrame:
    ### CREATING INSTANCE OF GUI ###
    root = tk.Tk() 
    root.title('Our Wonderful Time Tracking GUI 1.0.0') # Title displays at the top
    root.minsize(500, 700) 

    ### CREATE INSTANCE OF NOTEBOOK ###
    notebook = ttk.Notebook(root)

    ### CREATE TABS ###
    mainTab = ttk.Frame(notebook)
    tagsTab = ttk.Frame(notebook)
    goalsTab = ttk.Frame(notebook)

    ### POPULATE NOTEBOOK WITH TABS ###
    notebook.add(mainTab, text = "Main Menu")
    notebook.add(tagsTab, text = "Tags Menu")
    notebook.add(goalsTab, text = "Goal Dashboard")
    notebook.pack(expand = 1, fill = 'both')

    # TODO: Add more widgets here : https://docs.python.org/3/library/tkinter.ttk.html

def main():
    outerFrame = OuterFrame()

    #mainTab
    mainFrame = TimerObject.TimerFrame(outerFrame.mainTab)
    timer = TimerObject.Timer(outerFrame.mainTab)

    #tagsTab
    tagBtn = TimerTags.Tags(outerFrame.tagsTab)

    #goalsTab
    goalFrame = GoalsTabObjects.GoalsFrameIntro(outerFrame.goalsTab)
    setGoalDropdown = GoalsTabObjects.GoalsFrameDropdown(outerFrame.goalsTab)

    ### MAINLOOP CALL ###
    outerFrame.root.mainloop()

main()
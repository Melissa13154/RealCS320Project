### IMPORTS ###
import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import * # Is this necessary?
from tkinter import ttk # For accessing Notebook widget

import MainPageObjects
import TimerObject
import TimerFrameObject
import TimerTags

### DETAILS ###
TK_SILENCE_DEPRECATION=1 # Supress warnings
backgroundColor = "#3A7069"
IMAGES = "ClockResized.gif"

### OUTERFRAME CLASS  ###
class OuterFrame:
    root = tk.Tk() # Creates main root
    root.title('Our Wonderful Time Tracking GUI 1.0.0') # Title displays at the top
    #root.geometry = ('500 x 700') # Initial dimensions of window
    root.minsize(500, 700) # Hmm, this one seems to work and not the root.geometry statement above

    ### CREATE NOTEBOOK ###
    notebook = ttk.Notebook(root) # Create Notebook

    ### CREATE TABS ###
    mainTab = ttk.Frame(notebook)
    tagsTab = ttk.Frame(notebook)
    goalsTab = ttk.Frame(notebook)

    ### POPULATE NOTEBOOK WITH TABS ###
    notebook.add(mainTab, text = "Main Menu")
    notebook.add(tagsTab, text = "Tags Menu")
    notebook.add(goalsTab, text = "Goal Dashboard")
    notebook.pack(expand = 1, fill = 'both')

    ### ADD TO mainTab ###
    Label(mainTab, text = "Put frame with timer, clock image, start/stop button here.").pack()
    # TODO: Add more widgets here : https://docs.python.org/3/library/tkinter.ttk.html
    # Add TimerObject, TimerFrameObjects, etc.  Will this be a possible?

    ### ADD TO tagsTab ###
    Label(tagsTab, text = "Make new tags here.").pack()

    ### ADD TO goalsTab ###
    Label(goalsTab, text = "Goals Dashboard here.").pack()

### CREATE OBJECT ###
outerFrame = OuterFrame()

### MAINLOOP CALL ###
outerFrame.root.mainloop()

### IMPORTS ###
import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import * # Is this necessary?
from tkinter import ttk # For accessing Notebook widget
#from tkinter.ttk import *

import TimerObject
import TimerTags
import GoalsTabObjects

### DETAILS ###
TK_SILENCE_DEPRECATION=1 # Supress warnings
backgroundColor = "#3A7069"
IMAGES = "ClockResized.gif"

#s = ttk.Style()
#s.configure('TFrame', background='red')

### OUTERFRAME CLASS  ###
class OuterFrame:
    def __init__(self):
        self.root = tk.Tk() # Creates main root
        self.root.title('Our Wonderful Time Tracking GUI 1.0.0') # Title displays at the top
        #root.geometry = ('500 x 700') # Initial dimensions of window
        self.root.minsize(500, 700) # Hmm, this one seems to work and not the root.geometry statement above

        ### CREATE NOTEBOOK ###
        self.notebook = ttk.Notebook(self.root) # Create Notebook

        ### CREATE TABS ###
        self.mainTab = ttk.Frame(self.notebook)
        self.tagsTab = ttk.Frame(self.notebook)
        #self.goalsTab = ttk.Frame(self.notebook, style='TFrame')
        self.goalsTab = ttk.Frame(self.notebook)

        ### POPULATE NOTEBOOK WITH TABS ###
        self.notebook.add(self.mainTab, text = "Main Menu")
        self.notebook.add(self.tagsTab, text = "Tags Menu")
        self.notebook.add(self.goalsTab, text = "Goal Dashboard")
        self.notebook.pack(expand = 1, fill = 'both')

        ### ADD TO mainTab ###
        #Label(self.mainTab, text = "Put frame with timer, clock image, start/stop button here.").pack()
        # Add TimerObject, TimerFrameObjects, etc.  Will this be a possible?
                                                        #^^yes it will >:)

        ### ADD TO tagsTab ###
        Label(self.tagsTab, text = "Make new tags here.").pack()

        ### ADD TO goalsTab ###
        #Label(self.goalsTab, text = "Goals Dashboard here.").pack()


def main():
    ### CREATE OBJECT ###
    outerFrame = OuterFrame()

    #mainTab
    mainFrame = TimerObject.TimerFrame(outerFrame.mainTab)
    timer = TimerObject.Timer(outerFrame.mainTab)

    #tagsTab
    tagFrame = TimerTags.GoalDashboardButton(outerFrame.tagsTab)

    #goalsTab
    goalFrame = GoalsTabObjects.GoalsFrame(outerFrame.goalsTab)

    ### MAINLOOP CALL ###
    outerFrame.root.mainloop()

main()

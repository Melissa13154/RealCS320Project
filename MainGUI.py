### IMPORTS ###
import tkinter as tk
from tkinter import *
from tkinter import ttk # For accessing Notebook widget

import csv

import TimerObject
import TimerTags
import GoalsTabObjects
import databaseInit

### DETAILS ###
TK_SILENCE_DEPRECATION=1 # Supress warnings
backgroundColor = "#3A7069"

### OUTERFRAME CLASS ###
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

### CREATE DATABASE ONCE ###
#timerDB = databaseInit.DB()

### MAIN FUNCTION ###
def main():

    ### TIMETAGS VARIABLES ###
    timeDatabase = 'timeDatabase.csv'
    timeTagOptions = []

    ### FUNCTION TO READ IN TIMETAGS FROM DATABASE TO CREATE TAGS LIST ###
    def readInTimeTagsFromDatabase(timeDatabase, timeTagOptions):
        with open (timeDatabase, mode = 'r') as timeDatabase:
            csvReader = csv.reader(timeDatabase)
            next(csvReader) # Skip column titles, begin at row below that
            for row in csvReader:
                timeTagOptions.append(row[0])
            print("Finished assembling timeTagOptions list from timeDatabase.")
            print(f"Contents of list: {timeTagOptions}")

    ### CREATE TIMETAGS LIST FROM DATABASE ###
    readInTimeTagsFromDatabase(timeDatabase, timeTagOptions)

    outerFrame = OuterFrame()

    #mainTab
    mainFrame = TimerObject.TimerFrame(outerFrame.mainTab)
    timer = TimerObject.Timer(outerFrame.mainTab, timeTagOptions)

    #tagsTab
    tagBtn = TimerTags.CreateTags(outerFrame.tagsTab)
    #DBconnection, DBcur = timerDB.getConnectionInfo()

    #goalsTab
    goalFrame = GoalsTabObjects.GoalsFrameSetup(outerFrame.goalsTab)
    setGoal = GoalsTabObjects.GoalsFrameSetGoal(outerFrame.goalsTab, timeTagOptions)

    ### MAINLOOP CALL ###
    outerFrame.root.mainloop()

### CALL MAIN FUNCTION ###
main()
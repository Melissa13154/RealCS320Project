### IMPORTS ###
import tkinter as tk
from tkinter import *
from tkinter import ttk # For accessing Notebook widget

import csv

import TimerObject
import TimerTags
import GoalsTabObjects
import GoalsProgressObjects
import databaseInit

### DETAILS ###
TK_SILENCE_DEPRECATION=1 # Supress warnings
backgroundColor = "#87ccab"

### OUTERFRAME CLASS ###
class OuterFrame:
    ### CREATING INSTANCE OF GUI ###
    root = tk.Tk() 
    root.title('Our Wonderful Time Tracking GUI 1.0.0') # Title displays at the top
    root.minsize(500, 700) 

    ### CREATE INSTANCE OF NOTEBOOK ###
    notebook = ttk.Notebook(root)

    s = ttk.Style()
    s.configure('new.TFrame', background = backgroundColor)

    ### CREATE TABS ###
    mainTab = ttk.Frame(notebook, style='new.TFrame')
    tagsTab = ttk.Frame(notebook)
    goalsTab = ttk.Frame(notebook)
    goalsProgressTab = ttk.Frame(notebook)

    ### POPULATE NOTEBOOK WITH TABS ###
    notebook.add(mainTab, text = "Main Menu")
    notebook.add(tagsTab, text = "Tags Menu")
    notebook.add(goalsTab, text = "Set a Goal")
    notebook.add(goalsProgressTab, text = "Goal Progress")
    notebook.pack(expand = 1, fill = 'both')

    # TODO: Add more widgets here : https://docs.python.org/3/library/tkinter.ttk.html

### CREATE DATABASE ONCE ###
#timerDB = databaseInit.DB()

### RUN THIS TO INIITIALIZE ###
def initialize():

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

    return timeTagOptions

### MAIN FUNCTION ###
def main():
    
    ### RUN INITIAIZE FUNCTION, FUNCTION RETURNS THE LIST OF TIMETAG OPTIONS ###
    timeTagOptions = initialize()

    outerFrame = OuterFrame()
    # # ### TIMETAGS VARIABLES ###
    # timeDatabase = 'timeDatabase.csv'
    # timeTagOptions = []

    # ### FUNCTION TO READ IN TIMETAGS FROM DATABASE TO CREATE TAGS LIST ###
    # def readInTimeTagsFromDatabase(timeDatabase, timeTagOptions):
    #     with open (timeDatabase, mode = 'r') as timeDatabase:
    #         csvReader = csv.reader(timeDatabase)
    #         next(csvReader) # Skip column titles, begin at row below that
    #         for row in csvReader:
    #             timeTagOptions.append(row[0])
    #         print("Finished assembling timeTagOptions list from timeDatabase.")
    #         print(f"Contents of list: {timeTagOptions}")

    # ### CREATE TIMETAGS LIST FROM DATABASE ###
    # readInTimeTagsFromDatabase(timeDatabase, timeTagOptions)

    # outerFrame = OuterFrame()

    #mainTab
    mainFrame = TimerObject.TimerFrame(outerFrame.mainTab, timeTagOptions)

    #tagsTab
    #TimerTags.taginit(outerFrame.tagsTab, timerDB)

    #goalsTab
    goalFrame = GoalsTabObjects.GoalsFrameSetup(outerFrame.goalsTab, timeTagOptions)
    setGoal = GoalsTabObjects.GoalsFrameSetGoal(outerFrame.goalsTab, timeTagOptions)

    #goalsProgressTab
    goalProgressFrame = GoalsProgressObjects.GoalsProgressFrameSetup(outerFrame.goalsProgressTab, timeTagOptions)

    ### MAINLOOP CALL ###
    outerFrame.root.mainloop()


### CALL MAIN FUNCTION ###
main()
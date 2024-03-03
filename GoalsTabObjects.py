import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
import csv

backgroundColor = "#3A7069"

class GoalsFrameSetup(tk.Frame):
    def __init__(self, root, timeTagOptions):
        self.root = root
        self.timeTagOptions = timeTagOptions

        self.image = Image.open("graphPaper.jpg")
        self.photo_image = ImageTk.PhotoImage(self.image)

        background_label = ttk.Label(root, image=self.photo_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)       
        
        self.header = tk.Label(self.root, text = "Set a Goal!", font=('MS Sans Serif', 40))
        self.header.place(relx=.5, rely=.10, anchor = "center")

        ### CHECK IF LIST IS EMPTY ###
        listIsEmpty = True
        listIsEmpty = self.checkIfGoalsListIsEmpty()
        if listIsEmpty: 
            print("No TimeTags Exist.  Please populate the database first.")
            self.pleasePopulateTagsList = tk.Label(self.root, text = "Please Populate your Goal Tags in the Tags Tab", font=('MS Sans Serif', 20))
            self.pleasePopulateTagsList.place(relx=.5, rely=.19, anchor = "center")
        else:
            print("TimeTags have been populated.  List is NOT empty.")
            self.instructions = tk.Label(self.root, text = "Select a category + time goal below:", font=('MS Sans Serif', 20))
            self.instructions.place(relx=.5, rely=.19, anchor = "center")

    ### CHECK IF GOALS LIST IS EMPTY ###
    def checkIfGoalsListIsEmpty(self):
        if len(self.timeTagOptions) == 0:
            return True
        else: 
            return False
    

class GoalsFrameSetGoal(tk.Frame):
    def __init__(self, root, timeTagOptions):
        self.root = root
        self.timeTagOptions = timeTagOptions
        self.currentlySettingGoal = False

        ### TIMETAGS VARIABLES ###
        #timeDatabase = 'timeDatabase.csv'
        #timeTagOptions = []

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

        self.selectedGoal = tk.StringVar(root)

        self.selectedTimeGoal = tk.StringVar(root)

        style = ttk.Style()
        style.configure('Custom.TMenubutton', background='red') # I can change width here, but color not appearing on my computer
        self.goalDropdownMenu = ttk.OptionMenu(root, self.selectedGoal, *timeTagOptions, style='Custom.TMenubutton')
        self.goalDropdownMenu.place(relx=0.5, rely=0.25, anchor = "center")

        self.fifteenMins = ttk.Radiobutton(root, text="15 mins", variable=self.selectedTimeGoal, value="15")
        self.fifteenMins.place(relx=.1, rely=.30)

        self.thirtyMins = ttk.Radiobutton(root, text="30 mins", variable=self.selectedTimeGoal, value="30")
        self.thirtyMins.place(relx=.3, rely=.30)

        self.fortyFiveMins = ttk.Radiobutton(root, text="45 mins", variable=self.selectedTimeGoal, value="45")
        self.fortyFiveMins.place(relx=.5, rely=.30)

        self.sixtyMins = ttk.Radiobutton(root, text="60 mins", variable=self.selectedTimeGoal, value="60")
        self.sixtyMins.place(relx=.7, rely=.30)

        self.setGoalButton = ttk.Button(root, text="Confirm Goal", command=self.setGoal)
        self.setGoalButton.place(relx=0.5, rely=0.37, anchor = "center")


    ### SET GOAL FUNCTION ###
    def setGoal(self):
        self.currentlySettingGoal = not self.currentlySettingGoal

        if(self.currentlySettingGoal):
            self.goalToTrack = self.selectedGoal.get()
            self.goalTimeDuration = self.selectedTimeGoal.get()
            print("Setting goal for:", self.goalToTrack)
            print("Time goal:", self.goalTimeDuration)
            self.setGoalButton.config(text = "Refresh and Set a New Goal") #change button label
            self.checkIfGoalAlreadyExists() # Call the next function

        else:
            self.setGoalButton.config(text = "Confirm Goal") #change button label
        
    ### FIND GOAL ROW IN DATABASE ###
    def checkIfGoalAlreadyExists(self):
        print("Entered the checkIfGoalAlreadyExists function.")
        with open('timeDatabase.csv', mode='r') as timeDatabase:
            csvReader = csv.reader(timeDatabase)
            print("Opened timeDatabase.csv")
            rowNumber = 0
            for row in csvReader:
                if row[0] == self.goalToTrack:
                    print("Goal found in database")
                    print(f"Goal found on row: {rowNumber} (row 0 is column titles).")
                    return
                rowNumber += 1
            print("Goal not found in database") # All rows searched, goal not found.
            return

    ### PRINT GOAL IN TERMINAL (for testing purposes) ###
    def printSelectedGoal(self):
        self.printThis = self.selectedGoal.get()
        print("You're setting a goal for:", self.printThis)

    def printSelectedGoalOnGUI(self):
        self.printThisOnScreen = self.selectedGoal.get()
        if self.printThisOnScreen != '':
            self.goalConfirmed = tk.Label(self.root, text=self.printThisOnScreen, font=('MS Sans Serif', 20), bg = backgroundColor)
            self.goalConfirmed.place(relx=.5, rely=.45, anchor = "center")
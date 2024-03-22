import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
import csv

from GoalsTabObjects import checkIfGoalsListIsEmpty

backgroundColor = "#3A7069"

# ### CREATE EMPTY LIST FOR ROWS WITH GOALS ###
# rowsWithGoals = []

### CREATE A LIST WITH ROWS OF ALL TIMETAGS WITH ASSOC. GOALS ###
def createListOfRowsWithGoals():
    print("Creating a list of the rows that have goals set for them.")
    rowsWithGoals = []
    with open('timeDatabase.csv', mode='r') as timeDatabase:
        csvReader = csv.reader(timeDatabase)
        print("Opened timeDatabase.csv")
        for index, row in enumerate(csvReader):
            if row[2] == "1":
                print("This row has a goal set.  Adding to rowswithGoals list")
                rowsWithGoals.append(index)
        return rowsWithGoals


### GOALSFRAMESETUP CLASS ###
class GoalsProgressFrameSetup(tk.Frame):
    def __init__(self, root, timeTagOptions):
        self.root = root
        self.timeTagOptions = timeTagOptions
        self.image = Image.open("graphPaper.jpg")
        self.photo_image = ImageTk.PhotoImage(self.image)

        background_label = ttk.Label(root, image=self.photo_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)       
        
        self.header = tk.Label(self.root, text = "Your Progress", font=('MS Sans Serif', 40))
        self.header.place(relx=.5, rely=.10, anchor = "center")

        ### CHECK IF LIST IS EMPTY ###
        listIsEmpty = True
        listIsEmpty = checkIfGoalsListIsEmpty(timeTagOptions)
        if listIsEmpty: 
            print("No TimeTags Exist.  Please populate the database first.")
            self.pleasePopulateTagsList = tk.Label(self.root, text = "Please Populate your Goal Tags in the Tags Tab", font=('MS Sans Serif', 20))
            self.pleasePopulateTagsList.place(relx=.5, rely=.19, anchor = "center")
        else:
            print("TimeTags have been populated.  List is NOT empty.")
            newRowsList = []
            newRowsList = createListOfRowsWithGoals()
            print("Finished making list.")
            print("Rows with goals: ", newRowsList)
            # for row in newRowsList:
            #     print(row)
            # print(*newRowsList, sep = ", ")
            #self.instructions = tk.Label(self.root, text = "Select a category + time goal below:", font=('MS Sans Serif', 20))
            #self.instructions.place(relx=.5, rely=.19, anchor = "center")

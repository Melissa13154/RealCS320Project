import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
import csv

backgroundColor = "#3A7069"

### CHECK IF GOALS LIST IS EMPTY ###
def checkIfGoalsListIsEmpty(timeTagOptions):
    return all(tags == '' for tags in timeTagOptions)


### DOES TIMETAG EXIST IN DATABASE FUNCTION ###
def doesTimeTagExist(goalToTrack):
    print("Checking if the timeTag exists in the database")
    with open('timeDatabase.csv', mode='r') as timeDatabase:
        csvReader = csv.reader(timeDatabase)
        print("Opened timeDatabase.csv")
        for row in csvReader:
            if row[0] == goalToTrack:
                print("Goal found in database")
                return True
        print("Goal not found in database") # All rows searched, goal not found.
        return False


### FIND GOAL ROW IN DATABASE ###
def findRow(goalToTrack):
    print("Entered the findRow function.")
    with open('timeDatabase.csv', mode='r') as timeDatabase:
        csvReader = csv.reader(timeDatabase)
        print("Opened timeDatabase.csv")
        rowNumber = 0
        for row in csvReader:
            if row[0] == goalToTrack:
                print(f"Goal found on row: {rowNumber} (row 0 is column titles).")
                return rowNumber
            rowNumber += 1
        print("Goal not found in database") # All rows searched, goal not found.
        return 9999


### HAS GOAL ALREADY BEEN SET FOR THIS TIMETAG FUNCTION ###
def doesThisTimeTagAlreadyHaveAGoal(rowNumber):
    columnNumber = 4
    print("Checking if a goal has already been set for this timeTag.")
    with open('timeDatabase.csv', mode='r') as timeDatabase:
        csvReader = csv.reader(timeDatabase)
        print("Opened timeDatabase.csv")
        for index, row in enumerate(csvReader):
            if index == rowNumber:
                if row[columnNumber] == "0":
                    print("Goal has NOT been set.")
                    print("rownumber: " + str(rowNumber))
                    print("colnumber: " + str(columnNumber))
                    return False
                else:
                    print("Goal has been set already.")
                    print("rownumber: " + str(rowNumber))
                    print("colnumber: " + str(columnNumber))
                    return True


### CHECK IF GOAL HAS BEEN REACHED FUNCTION ###
def checkIfGoalHasBeenReached(rowNumber):
    totalTimeColumn = 3
    timeAccumulatedColumn = 6
    valueInTimeColumn = 0
    valueInTimeAccumulatedColumn = 0
    print("Checking if a goal has been reached.")
    with open('timeDatabase.csv', mode='r') as timeDatabase:
        csvReader = csv.reader(timeDatabase)
        print("Opened timeDatabase.csv")
        for index, row in enumerate(csvReader):
            if index == rowNumber:
                valueInTimeColumn = int(row[totalTimeColumn])
                valueInTimeAccumulatedColumn = int(row[timeAccumulatedColumn])
                if ((valueInTimeAccumulatedColumn >= valueInTimeColumn) and (valueInTimeColumn != 0) and (valueInTimeAccumulatedColumn != 0)):
                    print("You have achieved your goal.")
                    return True
                else:
                    print("You have not achieved your goal yet.  Keep at it.")
                    return False

### GOALSFRAMESETUP CLASS ###
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
        listIsEmpty = checkIfGoalsListIsEmpty(timeTagOptions)
        if listIsEmpty: 
            print("No TimeTags Exist.  Please populate the database first.")
            self.pleasePopulateTagsList = tk.Label(self.root, text = "Please Populate your Goal Tags in the Tags Tab", font=('MS Sans Serif', 20))
            self.pleasePopulateTagsList.place(relx=.5, rely=.19, anchor = "center")
        else:
            print("TimeTags have been populated.  List is NOT empty.")
            self.instructions = tk.Label(self.root, text = "Select a category + time goal below:", font=('MS Sans Serif', 20))
            self.instructions.place(relx=.5, rely=.19, anchor = "center")


### GOALSFRAMESETGOAL CLASS ###
class GoalsFrameSetGoal(tk.Frame):
    def __init__(self, root, timeTagOptions):
        self.root = root
        self.timeTagOptions = timeTagOptions
        self.currentlySettingGoal = False
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

        self.setGoalButton = ttk.Button(root, text="Set Goal", command=self.didUserSelectARadioButton)
        #self.setGoalButton = ttk.Button(root, text="Confirm Goal", command=self.setGoal)
        self.setGoalButton.place(relx=0.5, rely=0.37, anchor = "center")

        ### CHECK IF LIST IS EMPTY ###
        listIsEmpty = True
        listIsEmpty = checkIfGoalsListIsEmpty(timeTagOptions)
        if listIsEmpty: 
            print("No TimeTags Exist.  Please populate the database first.")
            self.setGoalButton.config(text="Please populate Tags in Tags Menu", state="disabled")
            self.goalDropdownMenu.config(state="disabled")
            self.fifteenMins.config(state="disabled")
            self.thirtyMins.config(state="disabled")
            self.fortyFiveMins.config(state="disabled")
            self.sixtyMins.config(state="disabled")
        else:
            print("TimeTags have been populated.  List is NOT empty.")


    ## CHECK IF USER SELECTED A RADIO BUTTON FUNCTION ###
    def didUserSelectARadioButton(self):
        if self.selectedTimeGoal.get() == "":
            print("User did not select time Goal")
            if self.didUserSelectARadioButton == True:
                self.setGoalButton = ttk.Button(self.root, text="Confirm Goal", command=self.setGoal)
                self.setGoalButton.place(relx=0.5, rely=0.37, anchor = "center")
        else: # User did set a goal, call setGoal function
            self.setGoal()
            #self.setGoalButton = ttk.Button(self.root, text="Confirm Goal", command=self.setGoal)
            #self.setGoalButton.place(relx=0.5, rely=0.37, anchor = "center")


    ### SET GOAL FUNCTION ###
    def setGoal(self):
        self.currentlySettingGoal = not self.currentlySettingGoal
        rowNumber = 9999
        goalSetFlag = 0

        if(self.currentlySettingGoal):
            self.goalToTrack = self.selectedGoal.get()
            self.goalTimeDuration = self.selectedTimeGoal.get()

            print("Setting goal for:", self.goalToTrack)
            print("Time goal:", self.goalTimeDuration)
            # TODO: Check if the line below is correct... ?  I feel like I possibly need to change text and add
            # a call to setgoal()??
            self.setGoalButton.config(text = "Refresh and Set a New Goal") #change button label

            goalExistsInDatabase = doesTimeTagExist(self.goalToTrack)
            if goalExistsInDatabase:
                rowNumber = findRow(self.goalToTrack) # Call the next function
                if rowNumber != 9999:
                    print("We found the rownumber: " + str(rowNumber))
                    #hasAGoalAlreadyBeenSet = self.doesThisTimeTagAlreadyHaveAGoal(self, rowNumber)
                else:
                    print("We did not find the row nubmer.")
            else:
                self.setGoal() # Might not be the right move to call this again here?

            hasAGoalAlreadyBeenSet = doesThisTimeTagAlreadyHaveAGoal(rowNumber)
            if hasAGoalAlreadyBeenSet == False:
                print("Goal has not already been set.  We need to set this goal.")
            else:
                goalSetFlag = 1
                print("Goal already set, go back to set a new goal.")
                self.setGoal()

            if goalSetFlag == 0: # ONLY DO THE STUFF BELOW IF GOAL HAS NOT BEEN SET YET

                goalStatusSet = self.changeGoalStatusToSet(rowNumber)
                if goalStatusSet:
                    print("Confirmed, goal status set in database.")

                hasMyGoalBeenReached = checkIfGoalHasBeenReached(rowNumber)
                if (hasMyGoalBeenReached):
                    print("You've reached your goal.")

            # TODO: ADD ANOTHER CALL TO setGoal() HERE ? 

            else:
                self.setGoalButton.config(text = "Confirm Goal") #change button label


    ### CHANGE GOAL STATUS FROM UNSET TO SET ###
    def changeGoalStatusToSet(self, rowNumber):
        columnNumber = 4
        rows = []
        print("Changing goal set Boolean within Database")
        with open('timeDatabase.csv', mode='r+') as timeDatabase:
            csvReader = csv.reader(timeDatabase)
            print("Opened timeDatabase.csv")
            for index, row in enumerate(csvReader):
                if (index == rowNumber and row[columnNumber] == "0"):
                    row[columnNumber] = "1"
                    print("Goal set at row number " + str(rowNumber) + " and column number " + str(columnNumber))
                    #return True
                rows.append(row)

            timeDatabase.seek(0)
            csvWriter = csv.writer(timeDatabase)
            csvWriter.writerows(rows)
        return True


    ### CHANGE GOAL REACHED STATUS FROM UNREACHED TO GOAL REACHED ###
    def changeGoalReachedStatus(self, rowNumber):
        columnNumber = 7
        rows = []
        print("Changing goal set Boolean within Database")
        with open('timeDatabase.csv', mode='r+') as timeDatabase:
            csvReader = csv.reader(timeDatabase)
            print("Opened timeDatabase.csv")
            for index, row in enumerate(csvReader):
                if index == rowNumber:
                    row[columnNumber] = "1"
                    print("Goal reached at row number " + str(rowNumber) + " and column number " + str(columnNumber))
                    #return True
                rows.append(row)

            timeDatabase.seek(0)
            csvWriter = csv.writer(timeDatabase)
            csvWriter.writerows(rows)       
        return True


    ### PRINT GOAL IN TERMINAL (for debugging purposes) ###
    def printSelectedGoal(self):
        self.printThis = self.selectedGoal.get()
        print("You're setting a goal for:", self.printThis)


    ### PRINT GOAL ON GUI (for debugging purposes ###)
    def printSelectedGoalOnGUI(self):
        self.printThisOnScreen = self.selectedGoal.get()
        if self.printThisOnScreen != '':
            self.goalConfirmed = tk.Label(self.root, text=self.printThisOnScreen, font=('MS Sans Serif', 20), bg = backgroundColor)
            self.goalConfirmed.place(relx=.5, rely=.45, anchor = "center")

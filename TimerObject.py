import tkinter as tk
from tkinter import ttk
import time
import threading
from tkinter import Canvas
from tkinter import PhotoImage
import csv

import GoalsTabObjects

#IDEA: Open associated application with menu button

def doesTimeTagExist(selectedGoal):
    # print("Checking if the timeTag exists in the database")
    with open('csvFiles/timeDatabase.csv', mode='r') as timeDatabase:
        csvReader = csv.reader(timeDatabase)
        # print("Opened timeDatabase.csv")
        for row in csvReader:
            if row[0] == selectedGoal:
                print("Goal found in database")
                return True
        print("Goal not found in database") # All rows searched, goal not found.
        return False
    
#---------------------------------------------------------------------------

def currentStoredTime(goalToTrack):
    with open('csvFiles/timeDatabase.csv', mode='r') as timeDatabase:
        csvReader = csv.reader(timeDatabase)
        for row in csvReader:
            if row[0] == goalToTrack:
                currentStoredTime = row[3]
                print("Current stored time: " + currentStoredTime)
                return float(currentStoredTime)   


backgroundColor = "#87ccab"
IMAGE = 'ClockResized.gif'

class TimerFrame(tk.Frame):
    #Tutorial referenced: https://www.youtube.com/watch?v=iP7CaRg9OPA
    def __init__(self, root, timeTagOptions):
        self.root = root

        self.canvas = Canvas(self.root, width =350, height=350, bg=backgroundColor, borderwidth=0)
        self.canvas.place(relx=.5, rely=.4, anchor="center")

        self.photo1 = PhotoImage(file='DynamicImageDrafts/ImageSet1/Stage1.png') #TODO: Figure out how to make corners transparent
        self.photo2 = PhotoImage(file='DynamicImageDrafts/ImageSet1/Stage2.png')
        self.photo3 = PhotoImage(file='DynamicImageDrafts/ImageSet1/Stage3.png')
        self.photo4 = PhotoImage(file='DynamicImageDrafts/ImageSet1/Stage4.png')
        self.ImageSet = [self.photo1, self.photo2, self.photo3, self.photo4]
        self.imageIndex = 0

        self.imageNum = self.canvas.create_image((0, 0), anchor='nw',image=self.ImageSet[self.imageIndex])

        self.timeTagOptions = timeTagOptions
        self.currentlyRunning = False

        self.selectedGoal = tk.StringVar(root)

        self.timerLabel = tk.Label(self.root, text="00:00:00", font=('MS Sans Serif', 20), bg=backgroundColor)
        self.timerLabel.place(relx= 0.5, rely=0.7, anchor='center')

        self.goalDropdownMenu = tk.OptionMenu(root, self.selectedGoal, *timeTagOptions)
        self.selectedGoal.set(timeTagOptions[0])
        self.goalDropdownMenu.config(bg='#FFD9B7')
        self.goalDropdownMenu.place(relx=0.5, rely=0.8, anchor = "center")

        self.currentGoal = -1.00
        self.accumulatedTime = -1.00

        self.button = tk.Button(self.root, text = "Start", width=15, command=self.startStop)
        self.button.place(relx= 0.5, rely = 0.9, anchor='n')

        self.label = tk.Label(self.root, text = "Click start to begin", font=('MS Sans Serif', 16), bg= backgroundColor)
        self.label.place(relx=.5, rely=.1, anchor="center")

#--------------------------------------------------------------------------------------------------  

    def startStop(self):
        
        self.currentlyRunning = not self.currentlyRunning

        if(self.currentlyRunning):
            self.goalToTrack = self.selectedGoal.get()

            self.currentGoal = currentStoredTime(self.goalToTrack)

            if(doesTimeTagExist(self.goalToTrack) == False):
                self.currentlyRunning = not self.currentlyRunning
                self.currentGoal = 0.0
                return
    

            print(f"Goal selected: {self.goalToTrack}")
            self.button.config(text = "Stop") #change button label
            self.removeWidgets()
            threading.Thread(target=self.countUp).start() #start new thread to count
        else:
            self.button.config(text = "Start") #change button label
            # threading.Thread(target=self.countUp).join() #wait for thread to kill
            self.replaceWidgets()
            print(self.label.winfo_ismapped())

#------------------------------------------------------------------------------------------

    def removeWidgets(self):
        self.goalDropdownMenu.place_forget()
        self.label.place_forget() 
        self.button.place(relx= 0.5, rely = 0.8, anchor='center')

#---------------------------------------------------------------------------------------------------

    def replaceWidgets(self):
        self.goalDropdownMenu.place(relx=0.5, rely=0.8, anchor = "center") 
        self.label.place(relx=.5, rely=.1, anchor="center")
        self.button.place(relx= 0.5, rely = 0.9, anchor='n')

#-------------------------------------------------------------------------------------------
            
    def changeImage(self, timePassed):
        if(timePassed/self.currentGoal >= 0.75):
            self.imageIndex = 3
        elif(timePassed/self.currentGoal >= 0.50):
            self.imageIndex = 2
        elif(timePassed/self.currentGoal >= 0.25):
            self.imageIndex = 1
        else:
            self.imageIndex = 0

        self.canvas.itemconfig(self.imageNum, image=self.ImageSet[self.imageIndex])
        

    def generateString(self, newCurrentTime):
        currentSecond = newCurrentTime % 60
        currentMinute = newCurrentTime // 60 #// = "floor divide"
        currentHour = currentMinute // 60
        return f"{int(currentHour):02d}:{int(currentMinute):02d}:{int(currentSecond):02d}"
    
#--------------------------------------------------------------------------------------------------------

    def countUp(self):
        startTime = time.time() #grabs the current time in seconds
        timePassed = 0

        while self.currentlyRunning:
            timePassed = time.time() - startTime #grabs the new current time, finds the difference since starting
            self.timerLabel.config(text = self.generateString(timePassed))
            self.changeImage(timePassed + self.accumulatedTime)

            time.sleep(0.001)

        self.timerLabel.config(text = self.generateString(0.0))
        self.changeImage(0)
        self.updateTimes(timePassed)


    def updateTimes(self, timePassed):
        row = GoalsTabObjects.findRow(self.selectedGoal)
        oldTime = GoalsTabObjects.returnCurrentStoredTime(row)
        self.accumulatedTime = GoalsTabObjects.calculateUpdatedStoredTime(oldTime, timePassed)
        GoalsTabObjects.updateStoredTimeInDatabase(row, self.accumulatedTime)
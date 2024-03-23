import tkinter as tk
from tkinter import ttk
import time
import threading
from tkinter import Canvas
from tkinter import PhotoImage
import csv
import pandas as pd

import GoalsTabObjects

#IDEA: Open associated application with menu button  

backgroundColor = "#87ccab"
IMAGE = 'ClockResized.gif'


#uses pandas package to check if a goal has been set or not
def isGoalSet(selectedGoal):
    data = pd.read_csv('timeDatabase.csv') #read in csv file into dataframe
    notSet = data[data['goalSetBool'] == 0] #grab all rows where values is 0

    if((notSet['timeTag'] == selectedGoal).any()):
        print("false")
        return False
    
    print("true")
    return True




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
        self.currentAccumulatedTime = -1.00

        self.button = tk.Button(self.root, text = "Start", width=15, command=self.startStop)
        self.button.place(relx= 0.5, rely = 0.9, anchor='n')

        self.label = tk.Label(self.root, text = "Click start to begin", font=('MS Sans Serif', 16), bg= backgroundColor)
        self.label.place(relx=.5, rely=.1, anchor="center")

#---------------------------------------------------------------------------

    def changeStates(self):
        self.currentlyRunning = not self.currentlyRunning


#-------------------------------------------------------------------------
        
    def isValid(self):
        self.goalToTrack = self.selectedGoal.get() #convert the current goal label selected to a string
        print(self.currentGoal)

        if(GoalsTabObjects.doesTimeTagExist(self.goalToTrack) == False or isGoalSet(self.goalToTrack) == False):
            self.changeStates()
            self.currentGoal = -1.0
            print("Tag doesnt exist")
            return False
        
        rowNumber = GoalsTabObjects.findRow(self.goalToTrack)
        self.currentGoal = GoalsTabObjects.returnCurrentStoredTime(rowNumber) #get the current goal value in csv
        self.currentAccumulatedTime = GoalsTabObjects.returnCurrentStoredTime(rowNumber)
        
        return True

#-----------------------------------------------------------------------------------
    
    def startTimer(self):
        print(f"Goal selected: {self.goalToTrack}")
        self.button.config(text = "Stop") #change button label
        self.removeWidgets() #clean up the screen
        thread = threading.Thread(target=self.countUp) #start new thread to count
        thread.start()


#--------------------------------------------------------------------------------------------------  

    def startStop(self):

        self.changeStates() #i know this is weird but for some reason its the only way to get the states to change correctly
        
        if self.currentlyRunning:
            if(self.isValid()):
                self.startTimer()
        else:
            self.timerLabel.config(text = self.generateString(0.0))
            self.changeImage(0.01)

            self.button.config(text = "Start") #change button label
            self.replaceWidgets()

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
        
#----------------------------------------------------------------

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
            self.changeImage(timePassed + self.currentAccumulatedTime)
            time.sleep(1)
        
        GoalsTabObjects.calculateUpdatedStoredTime(self.currentAccumulatedTime,timePassed) #update times in database
        return
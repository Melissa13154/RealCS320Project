import TimerObject
import GoalsTabObjects
import tkinter as tk

timer = TimerObject.TimerFrame(tk.Tk(), ["walk"])

#Acceptance test
def test_generateStr_positive():
    # timer = TimerObject.TimerFrame(tk.Tk(), ["walk"])
    print(timer.generateString(1000))

#Acceptance test
def test_generateStr_negative():
    # timer2 = TimerObject.TimerFrame(tk.Tk(), ["walk"])
    print(timer.generateString(-10))

#Acceptance test
def test_generateStr_large():
    # timer3 = TimerObject.TimerFrame(tk.Tk(), ["walk"])
    print(timer.generateString(10000000))


#-----------------------------------------------------------------------------------------
    
# def returnCurrentStoredTime(rowNumber):
#     columnNumber = 1
#     with open('csvFiles/timeDatabase.csv', mode='r') as timeDatabase:
#         csvReader = csv.reader(timeDatabase)
#         for index, row in enumerate(csvReader):
#             if index == rowNumber:
#                 currentStoredTime = row[columnNumber]
#                 print("Current stored time: " + currentStoredTime)
#                 print("rownumber: " + str(rowNumber))
#                 print("colnumber: " + str(columnNumber))
#                 return float(currentStoredTime)

#Checks if the returnCurrentStoredTime() returns the correct number 
def test_storedTime():
    rowNumber = GoalsTabObjects.findRow("walk")
    assert GoalsTabObjects.returnCurrentStoredTime(rowNumber) == 90

#Checks to see if function is actually grabbing different values
def test_storedTime_not():
    rowNumber = GoalsTabObjects.findRow("read for fun")
    assert not GoalsTabObjects.returnCurrentStoredTime(rowNumber) == 90


#-------------------------------------------------------------------------------------
    
# def updateTimes(self, timePassed):
#         row = GoalsTabObjects.findRow(self.selectedGoal)
#         oldTime = GoalsTabObjects.returnCurrentStoredTime(row)
#         self.accumulatedTime = GoalsTabObjects.calculateUpdatedStoredTime(oldTime, timePassed)

#checks if updateTimes() is storing the correct value in the accumulatedTime attribute
def test_countUp():
    # timer = TimerObject.TimerFrame(tk.Tk(), ["walk"])
    timer.selectedGoal = "walk"
    timer.updateTimes(5)
    assert timer.accumulatedTime == 25

#checks if the function is returning different things
def test_countUp_not():
    # timer = TimerObject.TimerFrame(tk.Tk(), ["walk"])
    timer.selectedGoal = "walk"
    timer.updateTimes(10)
    assert not timer.accumulatedTime == 25

#---------------------------------------------------------------------------------------

#Integration testing w/ functions from GoalsTabObjects and interacts with timeDatabase.csv
#Bottom Up approach
    
#checks if the correct value at the correct place is being written to the csv file by using the
#attributes specified in timer.

def test_pushValuetoCsv():
    # timer = TimerObject.TimerFrame(tk.Tk(), ["walk"])
    timer.selectedGoal = "walk"
    row = GoalsTabObjects.findRow(timer.selectedGoal)
    GoalsTabObjects.updateStoredTimeInDatabase(row, 17)
    assert GoalsTabObjects.returnCurrentStoredTime(row) == 17

def test_pushValuetoCsv_not():
    # timer = TimerObject.TimerFrame(tk.Tk(), ["walk"])
    timer.selectedGoal = "walk"
    row = GoalsTabObjects.findRow(timer.selectedGoal)
    GoalsTabObjects.updateStoredTimeInDatabase(row, 20)
    assert not GoalsTabObjects.returnCurrentStoredTime(row) == 17


#------------------------------------------------------------------------------

# def changeImage(self, timePassed):
#         if(timePassed/self.currentGoal >= 0.75):
#             self.imageIndex = 3
#         elif(timePassed/self.currentGoal >= 0.50):
#             self.imageIndex = 2
#         elif(timePassed/self.currentGoal >= 0.25):
#             self.imageIndex = 1
#         else:
#             self.imageIndex = 0

#         self.canvas.itemconfig(self.imageNum, image=self.ImageSet[self.imageIndex])


#Check if stage 1 of changeImage works
def test_changeImage_Stage1():
    # timer = TimerObject.TimerFrame(tk.Tk(), ["read for fun"])
    timer.currentGoal = 100
    timer.changeImage(0)
    assert timer.imageIndex == 0

#Check if stage 2 of changeImage works
def test_changeImage_Stage2():
    # timer = TimerObject.TimerFrame(tk.Tk(), ["read for fun"])
    timer.currentGoal = 100
    timer.changeImage(25)
    assert timer.imageIndex == 1

#check if stage 3 of changeImage works
def test_changeImage_Stage3():
    # timer = TimerObject.TimerFrame(tk.Tk(), ["read for fun"])
    timer.currentGoal = 100
    timer.changeImage(50)
    assert timer.imageIndex == 2

#check if stage 4 of changeImage works
def test_changeImage_Stage4():
    # timer = TimerObject.TimerFrame(tk.Tk(), ["read for fun"])
    timer.currentGoal = 100
    timer.changeImage(75)
    assert timer.imageIndex == 3
 

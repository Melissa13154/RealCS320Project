
import tkinter as tk
from tkinter import ttk
import pandas as pd
# import pymysql
import csv

myColor = "#c7d0b4"
DEBUG = 1

def displayAllTags(root, timerDB):
    timeLeftUntilGoalMet()
    height = countTags()
    displayAllTags = tk.Text(root, height=height, width='30')
    allTags = retrieveAllTags()
    for item in allTags:
        displayAllTags.insert(tk.END, item + "\n")
    displayAllTags.place(anchor='n', x='250', y='150')

def taginit(root, timerDB):
    ### BUILD TAG BUTTON ###
    displayAllTags(root, timerDB)
    tagBtn = tk.Button(root, text = "Create a New Tag", bg=myColor, state='active', command=lambda: input(root, tagBtn, timerDB))
    tagBtn.place(anchor='center', x='200', y='15')

def input(root, tagBtn, timerDB):
    tagBtn.place_forget()
    input = tk.Entry(root, width=20)
    input.place(anchor='center', x='200', y='15')

    okBtn = tk.Button(root, text="OK", state='active', command=lambda: retrieveUserIn(root, okBtn, input, timerDB))
    okBtn.place(anchor='center', x='75', y='15',)

def retrieveUserIn(root, okBtn, input, timerDB):
        okBtn.place_forget()
        newtag = input.get()
        print(input.get())
        if not (newtag == "") and not (dupTags(newtag)):
            enterNewTag(newtag)
            print(countTags())
        input.destroy()
        taginit(root, timerDB)

### COUNT TIMETAGS BEING TRACKED IN DATABASE ###
def countTags():
    rowCount = 0
    with open('timeDatabase.csv', mode='r') as timerDB:
        csvReader = csv.reader(timerDB)
        for row in enumerate(csvReader):
            rowCount+=1
    rowCount-=1 # To subtract column headers off database
    return rowCount

### REMOVE AN ENTRY FROM DB ###
def rmTag(tag):
    isInDB, rownum = inDB(tag)
    if not (isInDB):
        return False
    timerDB = pd.read_csv("timeDatabase.csv")
    timerDB = timerDB.drop(timerDB.index[rownum])
    timerDB.to_csv("timeDatabase.csv", index=False)

### ENTER NEW TUPLE IN DATABASE ###
def enterNewTag(timeTag):
    newEntry = [timeTag,0,0,0,0]
    try:
        with open('timeDatabase.csv', mode='a') as timerDB:
            csvWriter = csv.writer(timerDB)
            # csvWriter.writerow('\n')
            csvWriter.writerow(newEntry)
        return True
    except Exception as e:
            print(f"Error writing tuple to Database:{e}")
            return False

### CHECK FOR DUPLICATE TIMETAG ENTRY ###
def dupTags(timeTag):
    timerTagCol = 0
    with open('timeDatabase.csv', mode='r') as timerDB:
        csvReader = csv.reader(timerDB)
        for row in csvReader:
            if row[timerTagCol] == timeTag:
                print("timetag already exists.")
                return True
    print("This timetag is unique and new.")
    return False

def retrieveAllTags():
    timerTagCol = 0
    allTags = []
    with open('timeDatabase.csv', mode='r') as timerDB:
        csvread = csv.reader(timerDB)
        for row in csvread:
            allTags.append(row[timerTagCol])
    allTags.pop(0)  # removes first item sense it is only a headername
    print("the retrieveAllTags function:")
    print(allTags)
    return allTags

def inDB(tag):
    with open('timeDatabase.csv', mode='r') as timerDB:
        csvread = csv.reader(timerDB)
        for row in csvread:
            if row[0] == tag:
                return True, row
        return False, -1
    
def countGoalsSet():
    i = 0
    with open('timeDatabase.csv', mode='r') as timerDB:
        csvread = csv.reader(timerDB)
        for row in csvread:
            if (row[3] == 1):
                i += 1
    return i

def countGoalsMet():
    i = 0
    with open('timeDatabase.csv', mode='r') as timerDB:
        csvread = csv.reader(timerDB)
        for row in csvread:
            if (row[4] == 1):
                i =+ 1
    return i

def timeLeftUntilGoalMet():
    timeRemaining = 0
    timeLeft = {}
    with open('timeDatabase.csv', mode='r') as timerDB:
        csvread = csv.reader(timerDB)
        for row in csvread:
            if not (row == 0):
                timeRemaining = int(row[3]) - int(row[1])
            if (timeRemaining > 0):
                timeLeft[row[0]] = timeRemaining
    print(timeLeft)
    return timeLeft

def prioritize():
    i = 0
    with open('timeDatabase.csv', mode='r') as timerDB:
        csvread = csv.reader(timerDB)
        for row in csvread:
            if not (row[3] == 'goalTime'):
                if (int(row[3]) > i):
                    tag, i = row[0], int(row[3])
    return tag

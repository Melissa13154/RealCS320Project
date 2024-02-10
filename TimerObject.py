import tkinter as tk
import time
import threading

backgroundColor = "#c7d0b4"


#Tutorial referenced: https://www.youtube.com/watch?v=iP7CaRg9OPA
class Timer:
    def __init__(self, root):
        self.root = root
        self.currentlyRunning = False
        self.timePassed = 0

        self.button = tk.Button(self.root, text = "Start", width=15, command=self.startStop)
        self.button.place(relx= 0.5, rely = 0.8, anchor='n')
        
        self.label = tk.Label(self.root, text="00:00:00", font=('MS Sans Serif', 20), bg=backgroundColor)
        self.label.place(relx= 0.5, rely=0.75, anchor='center')


    def generateString(self, newCurrentTime):
        #newCurrentTime type = float
        currentSecond = newCurrentTime % 60
        currentMinute = newCurrentTime // 60 #// = "floor divide"
        currentHour = currentMinute // 60
        return f"{int(currentHour):02d}:{int(currentMinute):02d}:{int(currentSecond):02d}"

    def startStop(self):
        self.currentlyRunning = not self.currentlyRunning

        if(self.currentlyRunning):
            self.button.config(text = "Stop") #change button label
            threading.Thread(target=self.countUp).start() #start new thread to count

            #Sorry linnea i dont think we need this any more :(
            # stopTimeAsString = 0
            # stopTimeAsString = now.strftime("%H%M") # Attempting to capture stop time when "stop" is clicked - LPC
            # stopTime = int(stopTimeAsString)

            # if stopTime != 0:
            #     timeElapsed = (stopTime - startTime) # Might actually need to convert these from strings to ints? - LPC
            #     # timer.label = timeElapsed TODO: Change label to show time elapsed rather than 00:00

        else:
            self.button.config(text = "Start") #change button label


    def countUp(self):
        startTime = time.time() #grabs the current time in seconds

        while self.currentlyRunning:
            self.timePassed = time.time() - startTime #grabs the new current time, finds the difference since starting
            self.label.config(text = self.generateString(self.timePassed))
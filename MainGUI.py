import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage

import MainPageObjects
import TimerObject

backgroundColor = "#D1FFB0"

TK_SILENCE_DEPRECATION=1 #suppress warnings

class MainFrame:
    def __init__(self):
        self.root = tk.Tk() #creates main root
        self.root.config(bg= backgroundColor)
        self.root.title("Track Timer 1.0.0") #title display at the top
        self.root.geometry('500x700') #inital dimensions of window

        #image of clock    
        #TODO: figure out how to get fill image to show
        self.image1 = Canvas(self.root, width =350, height=350)
        self.image1.place(relx=.5, rely=.4, anchor="center")
        self.photo1 = PhotoImage(file='Images/Clock2-resized.gif')
        self.image1.create_image((1, 1), anchor='nw',image= self.photo1)

main = MainFrame()
mainLabel = MainPageObjects.StartingLabel(main.root)
timer = TimerObject.Timer(main.root)

main.root.mainloop() 
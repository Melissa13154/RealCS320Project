import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage

import MainPageObjects
import TimerObject
import TimerTags

backgroundColor = "#c7d0b4"
IMAGE = 'ClockResized.gif'

TK_SILENCE_DEPRECATION=1 #suppress warnings

class MainFrame:
    root = tk.Tk() #creates main root
    root.config(bg= backgroundColor)
    root.title("Track Timer 1.0.0") #title display at the top
    root.geometry('500x700') #inital dimensions of window

    #image of clock    
    image1 = Canvas(root, width =350, height=350)
    image1.place(relx=.5, rely=.4, anchor="center")
    photo1 = PhotoImage(file=IMAGE) #TODO: Figure out how to make corners transparent
    image1.create_image((1, 1), anchor='nw',image= photo1)

main = MainFrame()
mainLabel = MainPageObjects.StartingLabel(main.root)
timer = TimerObject.Timer(main.root)
goalDashboardButton = MainPageObjects.GoalDashboardButton(main.root)
tags = TimerTags.Tags(main.root)
tags.createTags()

main.root.mainloop() 
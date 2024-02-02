import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage

backgroundColor = "#D1FFB0"

TK_SILENCE_DEPRECATION=1

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
        self.photo1 = PhotoImage(file='Images/Clock2.gif')
        self.image1.create_image((1, 1), anchor='nw',image= self.photo1)


class StartingLabel:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(self.root, text = "Click button below to start timer", font=('MS Sans Serif', 20), bg= backgroundColor)
        self.label.place(relx=.5, rely=.1, anchor="center")


class StartButton:
    def __init__(self, root):
        self.root = root
        self.button = tk.Button(self.root, text = "Start", width=15, command=self.handleMouseClick)
        self.button.place(relx= 0.5, rely = 0.8, anchor='n')
        self.clicks = 0

    #changes text back and forth each click (kind of scuffed but it works)
    def handleMouseClick(self):
        self.clicks = self.clicks+1

        if((self.clicks)%2 != 0):
            self.button.config(text = "Stop")
        else:
            self.button.config(text = "Start")


class Timer:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(self.root, text="00:00", font=('MS Sans Serif', 20), bg=backgroundColor)
        self.label.place(relx= 0.5, rely=0.75, anchor='center')



main = MainFrame()
mainLabel = StartingLabel(main.root)
timer = Timer(main.root)
startButton = StartButton(main.root)


main.root.mainloop() 




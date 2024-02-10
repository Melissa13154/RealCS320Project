import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage

backgroundColor = "#3A7069"

class TimerFrame(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.config(bg=backgroundColor)
        self.root.title("Track Timer 1.0.0") #title display at the top
        self.root.geometry('500x700') #inital dimensions of window

        #image of clock    
        self.image1 = Canvas(self.root, width =350, height=350, bg=backgroundColor, borderwidth=0)
        self.image1.place(relx=.5, rely=.4, anchor="center")
        self.photo1 = PhotoImage(file='Images/Clock2-resized.gif') #TODO: Figure out how to make corners transparent
        self.image1.create_image((1, 1), anchor='nw',image= self.photo1)

        self.label = tk.Label(self.root, text = "Click start to begin", font=('MS Sans Serif', 20), bg= backgroundColor)
        self.label.place(relx=.5, rely=.1, anchor="center")
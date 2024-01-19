import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage

class MainFrame:

    def __init__(self):
        self.root = tk.Tk() #creates main root
        self.root.title("Track Timer 1.0.0")
        self.root.geometry('500x700') #inital dimensions of window

        self.label = tk.Label(self.root, text = "Click button below to start timer", font=('MS Sans Serif', 20))
        self.label.place(relx=.5, rely=.1, anchor="center")

        self.image1 = Canvas(self.root, width =350, height=350)
        self.image1.place(relx=.5, rely=.4, anchor="center")
        self.photo1 = PhotoImage(file='Images/Clock2.png')
        self.image1.create_image((1, 1), anchor='nw',image= self.photo1) #cant figure out how to show whole photo???

        self.button = tk.Button(self.root, text = 'Start', width=15)
        self.button.place(relx= 0.5, rely = 0.8, anchor='n')


class Timer:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(self.root, text="00:00", font=('MS Sans Serif', 20))
        self.label.place(relx= 0.5, rely=0.75, anchor='center')

        # def startTimer:



main = MainFrame()
timer = Timer(main.root)
main.root.mainloop()

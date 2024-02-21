import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image, ImageTk

backgroundColor = "#3A7069"

class GoalsFrameSetup(tk.Frame):
    def __init__(self, root):
        self.root = root

        self.image = Image.open("graphPaper.jpg")
        self.photo_image = ImageTk.PhotoImage(self.image)

        background_label = ttk.Label(root, image=self.photo_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)       
        
        self.header = tk.Label(self.root, text = "Set a Goal!", font=('MS Sans Serif', 40))
        self.header.place(relx=.5, rely=.10, anchor = "center")
        #self.header.pack()

        self.instructions = tk.Label(self.root, text = "Select a category + time goal below:", font=('MS Sans Serif', 20))
        self.instructions.place(relx=.5, rely=.19, anchor = "center")
        #self.instructions.pack()


class GoalsFrameSetGoal(tk.Frame):
    def __init__(self, root):
        self.root = root

        self.selectedGoal = tk.StringVar(root)
        self.timeTagOptions = ["Study databases", "Workout", "Read a book", "Work on CS 320 Project"]

        self.selectedTimeGoal = tk.StringVar(root)

        style = ttk.Style()
        style.configure('Custom.TMenubutton', background='red') # I can change width here, but color not appearing on my computer
        #self.goalDropdownMenu = ttk.OptionMenu(root, self.selectedGoal, "option 1", "option 2", "option 3", style='Custom.TMenubutton')
        self.goalDropdownMenu = ttk.OptionMenu(root, self.selectedGoal, *self.timeTagOptions, style='Custom.TMenubutton')
        self.goalDropdownMenu.place(relx=0.5, rely=0.25, anchor = "center")

        self.fifteenMins = ttk.Radiobutton(root, text="15 mins", variable=self.selectedTimeGoal, value="15")
        self.fifteenMins.place(relx=.1, rely=.30)

        self.thirtyMins = ttk.Radiobutton(root, text="30 mins", variable=self.selectedTimeGoal, value="30")
        self.thirtyMins.place(relx=.3, rely=.30)

        self.fortyFiveMins = ttk.Radiobutton(root, text="45 mins", variable=self.selectedTimeGoal, value="45")
        self.fortyFiveMins.place(relx=.5, rely=.30)

        self.sixtyMins = ttk.Radiobutton(root, text="60 mins", variable=self.selectedTimeGoal, value="60")
        self.sixtyMins.place(relx=.7, rely=.30)

        self.printButton = ttk.Button(root, text="Confirm Goal", command=self.setGoal)
        self.printButton.place(relx=0.5, rely=0.37, anchor = "center")

    def setGoal(self):
        self.selectedGoal = self.selectedGoal.get()
        self.selectedTimeGoal = self.selectedTimeGoal.get()
        print("Setting goal for:", self.selectedGoal)
        print("Time goal:", self.selectedTimeGoal)

    def printSelectedGoal(self):
        self.printThis = self.selectedGoal.get()
        print("You're setting a goal for:", self.printThis)

    def printSelectedGoalOnGUI(self):
        self.printThisOnScreen = self.selectedGoal.get()
        if self.printThisOnScreen != '':
            self.goalConfirmed = tk.Label(self.root, text=self.printThisOnScreen, font=('MS Sans Serif', 20), bg = backgroundColor)
            self.goalConfirmed.place(relx=.5, rely=.45, anchor = "center")
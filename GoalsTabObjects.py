import tkinter as tk
from tkinter import ttk

backgroundColor = "#3A7069"

class GoalsFrameIntro(tk.Frame):
    def __init__(self, root):
        self.root = root
        
        self.header = tk.Label(self.root, text = "Set a Goal!", font=('MS Sans Serif', 40), bg= backgroundColor)
        self.header.place(relx=.5, rely=.05, anchor = "center")
        #self.header.pack()

        self.instructions = tk.Label(self.root, text = "Select a category below:", font=('MS Sans Serif', 20), bg= backgroundColor)
        self.instructions.place(relx=.5, rely=.15, anchor = "center")
        #self.instructions.pack()


class GoalsFrameDropdown(tk.Frame):
    def __init__(self, root):
        self.root = root

        self.selectedGoal = tk.StringVar(root)
        self.timeTagOptions = ["Study databases", "Workout", "Read a book", "Work on CS 320 Project"]

        style = ttk.Style()
        style.configure('Custom.TMenubutton', background='red') # I can change width here, but color not appearing on my computer
        #self.goalDropdownMenu = ttk.OptionMenu(root, self.selectedGoal, "option 1", "option 2", "option 3", style='Custom.TMenubutton')
        self.goalDropdownMenu = ttk.OptionMenu(root, self.selectedGoal, *self.timeTagOptions, style='Custom.TMenubutton')
        self.goalDropdownMenu.place(relx=0.5, rely=0.3, anchor = "center")

        self.printButton = ttk.Button(root, text="Print Selected Option", command=self.printSelectedGoal)
        self.printButton.place(relx=0.5, rely=0.4, anchor = "center")

    def printSelectedGoal(self):
        self.printThis = self.selectedGoal.get()
        print("You're setting a goal for:", self.printThis)

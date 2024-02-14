import tkinter as tk

backgroundColor = "#3A7069"

class GoalsFrame(tk.Frame):
    def __init__(self, root):
        self.root = root
        
        self.header = tk.Label(self.root, text = "Set a Goal!", font=('MS Sans Serif', 40), bg= backgroundColor)
        self.header.place(relx=.5, rely=.05, anchor = "center")
        #self.header.pack()

        self.instructions = tk.Label(self.root, text = "Select a category below:", font=('MS Sans Serif', 20), bg= backgroundColor)
        self.instructions.place(relx=.5, rely=.15, anchor = "center")
        #self.instructions.pack()

        self.selectedGoal = tk.StringVar()
        self.goalDropdownMenu = tk.OptionMenu(root, self.selectedGoal, "option 1", "option 2", "option 3")
        self.goalDropdownMenu.place(relx=0.5, rely=0.4, anchor = "center")
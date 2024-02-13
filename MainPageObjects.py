import tkinter as tk

backgroundColor = "#3A7069" #background color global for main theme

class GoalDashboardButton:
    def __init__(self, root):
        self.root = root
        self.goaldashbutton = tk.Button(self.root, text = "Goal Dashboard", width=30)
        self.goaldashbutton.place(relx= 0.5, rely = 0.9, anchor='center')

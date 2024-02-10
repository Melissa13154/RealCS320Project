import tkinter as tk

backgroundColor = "#3A7069" #background color global for main theme

class TimeTags:
    def __init__(self, root):
        self.root = root
        def userin():
            canvas = tk.Canvas(self.root, width=100, height=50, bg = 'white')
            usr = tk.Entry(self.root, relief='flat', bg = backgroundColor)   # store user input into a database
            canvas.create_window(200, 250, window=usr)
            
        tagBtn = tk.Button(self.root, text = "Create a Tag", bg =backgroundColor, state = 'active', command = userin)
        tagBtn.place(x = 250, y = 100)


class GoalDashboardButton:
    def __init__(self, root):
        self.root = root
        self.goaldashbutton = tk.Button(self.root, text = "Goal Dashboard", width=30)
        self.goaldashbutton.place(relx= 0.5, rely = 0.9, anchor='center')

import tkinter as tk

backgroundColor = "#D1FFB0" #background color global for main theme

class StartingLabel:
    def __init__(self, root):
        self.root = root
        self.label = tk.Label(self.root, text = "Click start to begin", font=('MS Sans Serif', 20), bg= backgroundColor)
        self.label.place(relx=.5, rely=.1, anchor="center")


class TimeTags:
    def __init__(self, root):
        self.root = root
        def userin():
            canvas = tk.Canvas(self.root, width=100, height=50, bg = 'white')
            usr = tk.Entry(self.root, relief='flat', bg = backgroundColor)   # store user input into a database
            canvas.create_window(200, 250, window=usr)

        tagBtn = tk.Button(self.root, text = "Create a Tag", bg = backgroundColor, state = 'active', command = userin)
        tagBtn.place(x = 250, y = 100)
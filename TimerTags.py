import tkinter as tk

myColor = "#c7d0b4"
DEBUG = 1


class Tags:
    def __init__(self, root):
        self.root = root
        
    def close(self):
        print(input.get())
        input.destroy()

    def tags(self):
        # create pop up window displaying list of existing tags
        # have a cancel option and a create new option

        # upon selecting to create a new tag
        input = tk.Entry(self.root, width=20)
        input.pack()
        ok = tk.Button(self.root, text="OK", state='active', command=self.close())
        ok.pack(side='right')

    def createTags(self):
        tagBtn = tk.Button(self.root, text = "Create a Tag", bg=myColor, state='active', command=self.tags())
        tagBtn.pack()
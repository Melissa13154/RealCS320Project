import tkinter as tk
# import mypysql

myColor = "#c7d0b4"
DEBUG = 1

class Tags:
    def __init__(self, root):
        self.root = root
        clicked = False

    def click(self):
        clicked = True

    def close(self, object):
        self.object = object 
        self.object.destroy()

    def userIn(self, input):
        self.input = input
        print(self.input.get())

    def tagInput(self):
        if DEBUG: print("I am here")
        # create pop up window displaying list of existing tags
        # have a cancel option and a create new option

        # upon selecting to create a new tag
        input = tk.Entry(self.root, width=20)
        input.pack()
        input.config(command=lambda: self.close(input))

        ok = tk.Button(self.root, text="OK", state='active', command=lambda: self.userIn(input))
        ok.pack(side='right')
        ok.config(command=lambda: self.close(input))
        # sql = "INSERT INTO test(pk, info, num) VALUES ("+input+", )"

    def createTags(self):
        tagBtn = tk.Button(self.root, text = "Create a Tag", bg=myColor, state='active', command=self.click, self.tagInput)
        tagBtn.pack()
        # if tagBtn['state'] == 
        tagBtn.config(command=lambda: self.close(tagBtn))
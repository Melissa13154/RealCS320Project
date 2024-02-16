import tkinter as tk
# import mypysql

myColor = "#c7d0b4"
DEBUG = 1

class Tags:
    clicked = False

    def __init__(self, root):
        self.root = root
        self.createTags(self.root)

    def click(self):
        if DEBUG: print("saw a click")
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

        input = tk.Entry(self.root, width=20)
        input.pack()
        # input.config(command=lambda: self.close(input))

        ok = tk.Button(self.root, text="OK", state='active', command=lambda: self.userIn(input))
        ok.pack(side='right')
        # ok.config(command=lambda: self.close(input))
        # sql = "INSERT INTO test(pk, info, num) VALUES ("+input+", )"

    def createTags(self, root):
        self.root = root
        clicked = False
        tagBtn = tk.Button(self.root, text = "Create a Tag", bg=myColor, state='active', command=self.tagInput)
        tagBtn.pack()
        # self.close(tagBtn)
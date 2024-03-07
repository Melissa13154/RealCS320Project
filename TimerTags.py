import tkinter as tk
import pymysql

myColor = "#c7d0b4"
DEBUG = 1

def taginit(root):
    ### BUILD TAG BUTTON ###
    tagBtn = tk.Button(root, text = "Create a Tag", bg=myColor, state='active', command=createTextBox())
    tagBtn.pack()



class CreateTags:
    @staticmethod
    def __init__(self, root, timerDB):
        self.timerDB = timerDB
        self.root = root
        self.createTags(self.root)

    def click(self):
        if DEBUG: print("saw a click")
        clicked = True

    @staticmethod
    def close(object):
        object.destroy()

    def retrieveUserIn(self, input):
        self.input = input
        print(self.input.get())

    def createTextBox(self):
        if DEBUG: print("I am here")
        # create pop up window displaying list of existing tags
        # have a cancel option and a create new option

        input = tk.Entry(self.root, width=20)
        input.pack()
        # input.config(command=lambda: self.close(input))

        okBtn = tk.Button(self.root, text="OK", state='active', command=lambda: self.retrieveUserIn(input))
        okBtn.pack(side='right')
        # ok.config(command=lambda: self.close(input))
        # sql = "INSERT INTO test(pk, info, num) VALUES ("+input+", )"
import tkinter as tk

DEBUG = 1


class Tags:
    def __init__(self, root):
        self.root = root
        def tags():
            # create pop up window displaying list of existing tags
            # have a cancel option and a create new option
            if DEBUG: print("Hello world\n")

            # upon selecting to create a new tag
            def close():
                print(input.get())
                input.destroy()


            # usersTag = tk.StringVar()
            input = tk.Entry(root, width=20)
            input.pack()
            ok = tk.Button(root, text="OK", state='active', command=close)
            ok.pack(side='right')

        tagBtn = tk.Button(root, text = "Create a Tag", background='white', state='active', command=tags)

        tagBtn.pack()
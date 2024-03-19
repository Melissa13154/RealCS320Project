from MainGUI import main
from MainGUI import OuterFrame
from GoalsTabObjects import GoalsFrameSetGoal
from MainGUI import initialize
from tkinter import Tk

@pytest.fixture
def app():
    root = Tk()
    outerFrame = OuterFrame()
    timeTagOptions = initialize()
    #setGoal = GoalsFrameSetGoal(outerFrame.goalsTab, timeTagOptions)
    yield root
    #root.destroy()
    root.after(0, root.destroy)

def test_app(app):
    root = app
    assert (1 == 1)
    print("1 == 1")
    #print(GoalsFrameSetGoal.goalDropdownMenu.get())

    #print(setGoal.goalDropdownMenu.get())

# def print_options():
#     menu = setGoal.goalDropdownMenu["menu"]
#     for entry in menu["entries"]():
#         print(entry)

# assert (print_options)

# outerFrame = OuterFrame()
# timeTagOptions = initialize()

# main()
# main.destroy()


# setGoal = GoalsFrameSetGoal(outerFrame.goalsTab, timeTagOptions)

# from MainGUI import OuterFrame
# from MainGUI import initialize
# from GoalsTabObjects import GoalsFrameSetup
# from GoalsTabObjects import GoalsFrameSetGoal
# from TimerObject import TimerFrame
# from TimerTags import CreateTags
# from tkinter import Canvas


# timeTagOptions = initialize()

# outerFrame = OuterFrame()

# mainFrame = TimerFrame(outerFrame.mainTab, timeTagOptions)
# tagBtn = CreateTags(outerFrame.tagsTab)
# goalFrame = GoalsFrameSetup(outerFrame.goalsTab ,timeTagOptions)
# setGoal = GoalsFrameSetGoal(outerFrame.goalsTab, timeTagOptions)

# outerFrame.root.mainloop()

# #print(setGoal.goalDropdownMenu.get())

# def print_options():
#     menu = setGoal.goalDropdownMenu["menu"]
#     for entry in menu["entries"]():
#         print(entry)

# assert (print_options)
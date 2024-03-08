from GoalsTabObjects import findRow

def test_does_timetag_exist_exists():
    goalToTrack1 = "walk"
    assert (findRow(goalToTrack1) == 3) # Because the goal "walk" exists on row 3

def test_does_timetag_exist_doesnotexist():
    goalToTrack2 = "work on testing suite"
    assert (findRow(goalToTrack2) == 9999) # Because function will return 9999 for a goal that doesn't exist
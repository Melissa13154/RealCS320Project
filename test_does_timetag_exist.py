from GoalsTabObjects import doesTimeTagExist

def test_does_timetag_exist_exists():
    goalToTrack1 = "walk"
    assert doesTimeTagExist(goalToTrack1)

def test_does_timetag_exist_doesnotexist():
    goalToTrack2 = "work on testing suite"
    assert not doesTimeTagExist(goalToTrack2)
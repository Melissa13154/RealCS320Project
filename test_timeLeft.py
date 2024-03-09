from TimerTags import timeLeftUntilGoalMet

# WHITE BOX
def test_timeLeftUntilGoalMet():
    test = {"study haskell":30, "work on rpn assignment":30, "Workout":10}
    print (timeLeftUntilGoalMet)
    assert (test == timeLeftUntilGoalMet())

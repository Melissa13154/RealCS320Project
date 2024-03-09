from GoalsTabObjects import changeGoalStatusToSet

def test_change_goal_status_not_already_set():
    rowNumber = 1
    assert (changeGoalStatusToSet(rowNumber) == 1)
    # Function returns 1 when goal was not already set, and value was changed from 0 to 1

def test_change_goal_status_already_set():
    rowNumber = 5
    # Testing that a boolean will only change from unsest to set
    # And not the other way around. 
    assert not (changeGoalStatusToSet(rowNumber) == 1)

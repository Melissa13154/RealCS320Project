from GoalsTabObjects import checkIfGoalHasBeenReached

def test_has_goal_been_reached_allzeroes():
    rowNumber = 1
    assert not checkIfGoalHasBeenReached(rowNumber)

def test_has_goal_been_reached_yes():
    rowNumber = 2
    assert checkIfGoalHasBeenReached(rowNumber)

def test_has_goal_been_reached_notyet():
    rowNumber = 6
    assert not checkIfGoalHasBeenReached(rowNumber)


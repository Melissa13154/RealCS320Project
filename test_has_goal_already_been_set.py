from GoalsTabObjects import doesThisTimeTagAlreadyHaveAGoal

def test_timetag_already_has_a_goal_set():
    rowNumber = 6
    assert doesThisTimeTagAlreadyHaveAGoal(rowNumber)


def test_timetag_does_not_have_a_goal_set():
    rowNumber = 7
    assert not doesThisTimeTagAlreadyHaveAGoal(rowNumber)


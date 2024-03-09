from GoalsTabObjects import setGoalTimeInDatabase
from GoalsTabObjects import printRow

def test_set_goal_time_in_database():
    rowNumber = 4
    goalTimeDuration = 10

    printRow(rowNumber)
    assert setGoalTimeInDatabase(rowNumber, goalTimeDuration)
    printRow(rowNumber)

def test_set_goal_time_in_database_already_set():
    rowNumber = 5
    goalTimeDuration = 10

    printRow(rowNumber)
    assert not setGoalTimeInDatabase(rowNumber, goalTimeDuration)
    printRow(rowNumber)
    


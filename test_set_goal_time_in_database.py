from GoalsTabObjects import setGoalTimeInDatabase
from GoalsTabObjects import printRow

def test_set_goal_time_in_database():
    rowNumber = 4
    goalTimeDuration = 10

    printRow(rowNumber)
    setGoalTimeInDatabase(rowNumber, goalTimeDuration)
    printRow(rowNumber)


from GoalsTabObjects import doesTimeTagExist
from GoalsTabObjects import findRow
from GoalsTabObjects import doesThisTimeTagAlreadyHaveAGoal
from GoalsTabObjects import setGoalTimeInDatabase
from GoalsTabObjects import changeGoalStatusToSet
from GoalsTabObjects import checkIfGoalHasBeenReached
from GoalsTabObjects import printRow

def test_integration_of_goal_functions_flow():
    timeTag = "journal"
    goalTimeDuration = 30

    assert doesTimeTagExist(timeTag)
    print ("Timetag exists within database: " + timeTag)

    rowNumber = findRow(timeTag)
    assert rowNumber == 9
    print ("Row number found: " + str(rowNumber))
    printRow(rowNumber)

    assert not doesThisTimeTagAlreadyHaveAGoal(rowNumber)
    print("TimeTag does not already have a goal associated with it.")

    assert changeGoalStatusToSet(rowNumber) == 1

    assert setGoalTimeInDatabase(rowNumber, goalTimeDuration)

    printRow(rowNumber)

    assert not checkIfGoalHasBeenReached(rowNumber)
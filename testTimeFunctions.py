from GoalsTabObjects import findRow
from GoalsTabObjects import returnCurrentStoredTime
from GoalsTabObjects import calculateUpdatedStoredTime
from GoalsTabObjects import updateStoredTimeInDatabase
from GoalsTabObjects import countTimeTagsInDatabase
from GoalsTabObjects import enterNewTupleInDatabase

### VARIABLES ###
goal = "walk"
newlyTrackedTimeBlock = 35.0

### FIND WHAT ROW WALK IS IN ###
rowNumber = findRow(goal)

### RETURN CURRENT STORED TIME FROM DATABASE ###
storedTime = returnCurrentStoredTime(rowNumber)
print("Time returned from database: " + str(storedTime))

### CALCULATE UPDATED STORED TIME ###
updatedTime = calculateUpdatedStoredTime(storedTime, newlyTrackedTimeBlock)
print("Updated time value: " + str(updatedTime))

### UPDATE THE DATABASE (ADD OLD TIME WITH NEW TIME) ###
updateStatus = updateStoredTimeInDatabase(rowNumber, updatedTime)
if updateStatus:
    print("Update successful.")

### COUNT TIMETAGS IN DATABASE
numberOfGoals = countTimeTagsInDatabase()
print("Number of goals in database: " + str(numberOfGoals))

### ENTER NEW TUPLE IN DATABASE
timeTag = "rock this week"
entryStatus = enterNewTupleInDatabase(timeTag)
if entryStatus:
    print("Database entry successful.")







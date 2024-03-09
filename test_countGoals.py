from TimerTags import countGoalsSet
from TimerTags import countGoalsMet

# WHITE BOX
def test_countGoalsSet():
    currNumGoals = 4
    assert (currNumGoals == countGoalsSet())

# WHITE BOX
def test_countGoalsMet():
    currNumGoalsMet = 2
    assert (currNumGoalsMet == countGoalsMet())
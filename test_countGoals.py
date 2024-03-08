from TimerTags import countGoalsSet
from TimerTags import countGoalsMet


def test_countGoalsSet():
    currNumGoals = 4
    assert (currNumGoals == countGoalsSet())

def test_countGoalsMet():
    currNumGoalsMet = 2
    assert (currNumGoalsMet == countGoalsMet())
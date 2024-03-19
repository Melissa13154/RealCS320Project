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

from TimerTags import countTags

# WHITE BOX
def test_countTags():
    currTagCount = 7
    assert (countTags() == currTagCount)

from TimerTags import dupTags
from TimerTags import enterNewTag

# INTEGRATION
def test_dup_insert():
    newtag = "helloWorld!"
    assert not (dupTags(newtag))
    assert (enterNewTag(newtag))

from TimerTags import prioritize

# WHITE BOX
def test_prioritize():
    highestPrior = "study haskell"
    assert (prioritize() == highestPrior)

from TimerTags import retrieveAllTags
from TimerTags import countTags

# BLACK BOX
def test_retrieveAll():
    currTagCount = countTags()
    assert (currTagCount == len(retrieveAllTags()))

from TimerTags import countTags
from TimerTags import rmTag 

# BLACK BOX
def test_rmTag():
    deleteTagInCSV = "Hello World!"
    currTagCount = countTags()
    rmTag(deleteTagInCSV)
    assert (currTagCount - 1 == countTags())

# BLACK BOX
def test_rmTag():
    deleteTagNotInCSV = "hiiiy"
    currTagCount = countTags()
    rmTag(deleteTagNotInCSV)
    assert not (currTagCount - 1 == countTags())

from TimerTags import dupTags
from TimerTags import countTags

# returns true if duplicates found #
# WHITE BOX
def test_tag_dup():
    newtag = "Hello World!"
    currTagCount = countTags()
    assert dupTags(newtag)

# returns false if no duplicates #
# WHITE BOX
def test_tag_dup():
    newtag = "Hi!"
    currTagCount = countTags()
    assert not dupTags(newtag)

from TimerTags import enterNewTag
from TimerTags import countTags

### Tag doesn't yet exist in csv file so it should be inserted ###
# BLACK BOX
def test_tag_insertion():
    newtag = "welcome!"
    currTagCount = countTags()
    enterNewTag(newtag)
    assert (currTagCount + 1 == countTags())

from TimerTags import timeLeftUntilGoalMet

# WHITE BOX
def test_timeLeftUntilGoalMet():
    test = {"study haskell":30, "work on rpn assignment":30, "Workout":10}
    print (timeLeftUntilGoalMet)
    assert (test == timeLeftUntilGoalMet())
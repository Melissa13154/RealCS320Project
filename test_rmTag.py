from TimerTags import countTags
from TimerTags import rmTag 

def test_rmTag():
    deleteTagInCSV = "Hello World!"
    currTagCount = countTags()
    rmTag(deleteTagInCSV)
    assert (currTagCount - 1 == countTags())

def test_rmTag():
    deleteTagNotInCSV = "hiiiy"
    currTagCount = countTags()
    rmTag(deleteTagNotInCSV)
    assert not (currTagCount - 1 == countTags())
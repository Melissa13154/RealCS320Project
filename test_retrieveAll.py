from TimerTags import retrieveAllTags
from TimerTags import countTags

def test_retrieveAll():
    currTagCount = countTags()
    assert (currTagCount == len(retrieveAllTags()))
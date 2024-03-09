from TimerTags import retrieveAllTags
from TimerTags import countTags

# BLACK BOX
def test_retrieveAll():
    currTagCount = countTags()
    assert (currTagCount == len(retrieveAllTags()))
from TimerTags import enterNewTag
from TimerTags import countTags

### Tag doesn't yet exist in csv file so it should be inserted ###
def test_tag_insertion():
    newtag = "Hello word!"
    currTagCount = countTags()
    enterNewTag(newtag)
    assert (currTagCount + 1 == countTags())
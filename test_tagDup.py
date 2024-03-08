from TimerTags import dupTags
from TimerTags import countTags

# returns true if duplicates found #
def test_tag_dup():
    newtag = "Hello World!"
    currTagCount = countTags()
    assert dupTags(newtag)

# returns false if no duplicates #
def test_tag_dup():
    newtag = "Hi!"
    currTagCount = countTags()
    assert not dupTags(newtag)
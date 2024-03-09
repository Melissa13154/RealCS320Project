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
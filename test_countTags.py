from TimerTags import countTags

# WHITE BOX
def test_countTags():
    currTagCount = 10
    assert (countTags() == currTagCount)
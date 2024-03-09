from TimerTags import dupTags
from TimerTags import enterNewTag

# INTEGRATION
def test_dup_insert():
    newtag = "helloWorld!"
    assert not (dupTags(newtag))
    assert (enterNewTag(newtag))
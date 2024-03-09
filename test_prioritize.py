from TimerTags import prioritize

# BLACK BOX
def test_prioritize():
    highestPrior = "study haskell"
    assert (prioritize() == highestPrior)
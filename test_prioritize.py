from TimerTags import prioritize

def test_prioritize():
    highestPrior = "study haskell"
    assert (prioritize() == highestPrior)
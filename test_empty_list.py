from GoalsTabObjects import checkIfGoalsListIsEmpty

def test_is_goaltag_list_empty_empty():
    timeTagOptions1 = ['', '', '', '']
    assert checkIfGoalsListIsEmpty(timeTagOptions1)

def test_is_goaltag_list_empty_notempty():
    timeTagOptions2 = ['read', 'study', 'run', 'buy groceries']
    assert not checkIfGoalsListIsEmpty(timeTagOptions2)

def test_is_goaltag_list_empty_mixed():
    timeTagOptions3 = ['read', '', 'run', '']
    assert not checkIfGoalsListIsEmpty(timeTagOptions3)

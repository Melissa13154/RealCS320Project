import TimerObject
import tkinter as tk

def test_generateStr_negative():
    assert TimerObject.generateString(-1) == "00:00:00"

def test_generateStr_positive():
    assert TimerObject.generateString(1000) == "00:16:40"

#redundant
def test_currentStoredTime_large():
    assert TimerObject.currentStoredTime(10000000) == None

def test_currentStoredTime():
    assert TimerObject.currentStoredTime(1) == 7



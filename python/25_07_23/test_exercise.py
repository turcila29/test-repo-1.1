import pytest
from exercise import maxlen

def test_one():
    assert maxlen("hi","hello") == "hello"
    assert maxlen("three", "two") == "three"
    assert maxlen("three", "hello") == "three hello"
    assert maxlen("echo", "print") == "print"
    assert maxlen("fire","rib") == "fire"
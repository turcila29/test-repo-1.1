import pytest
from exercise import maxlen

def test_one():
    assert maxlen.one("hi","hello") == "hello"
    assert maxlen.one("three", "two") == "three"
    assert maxlen.one("three", "hello") == "three hello"
    assert maxlen.one("echo", "print") == "print"
    assert maxlen.one("fire","rib") == "fire"
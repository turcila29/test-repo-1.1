import pytest
from exercise import maxlen


def test_one():
    assert maxlen.one("white", "orange") == "orange"
    assert maxlen.one("tiger", "computer") == "computer"
    assert maxlen.one("egg", "building") == "building"

import pytest
from exercise import maxlen


def test_one():
    assert maxlen("tiger", "computer") == "computer"
    assert maxlen("egg", "building") == "building"

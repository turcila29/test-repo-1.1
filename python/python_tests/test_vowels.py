import vowels
def test_vowels():
    assert vowels.vowels('many') == 1
    assert vowels.vowels('dvsjdnfsf') == 0
    assert vowels.vowels('this line has 100000000000000 vowels ahahaahhahahahahaha') == 16


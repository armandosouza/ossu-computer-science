from um import count


def test_um():
    assert count("I like pizza and um") == 1
    assert count("I like chocolate um and banana um") == 2
    assert count("bananaum") == 0
    assert count("Um... maybe") == 1
from twttr import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("ARMANDO") == "RMND"
    assert shorten("armando123") == "rmnd123"
    assert shorten("car,.") == "cr,."
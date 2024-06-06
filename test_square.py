from square import get_square


def test_get_square():
    a = 7
    res = get_square(a)

    assert res == 49
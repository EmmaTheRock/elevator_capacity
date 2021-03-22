
def adder(lhs, rhs):
    return lhs + rhs


def test_adder_int():
    assert adder(4, 5) == 9


def test_adder_str():
    assert adder("a", "b") == "ab"

def multer(lhs, rhs):
    return lhs * rhs

def test_multer():
    assert multer(3, 5) == 15
    assert multer(7, 8) == 56

def divver(lhs, rhs):
    return lhs / rhs

def test_divver():
    assert divver(6, 2) == 3
    assert divver(9, 3) == 3
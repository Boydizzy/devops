from calculator import add, subtract, multiply, divide

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(1, 5) == -4


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0
    assert multiply(-2, 8) == -16


def test_divide():
    assert divide(10, 2) == 5
    assert divide(8, 4) == 2

    # Assuming your divide function handles division by zero gracefully
    assert divide(5, 0) is None

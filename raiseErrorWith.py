from pytest import raises
def raisesValueException():
    raise ValueError
def test_exception():
    with raises (ValueError):
        raisesValueException()


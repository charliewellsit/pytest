from pytest import raises

# Function that deliberately raises a ValueError
def raisesValueException():
    raise ValueError

# Test function that checks if raisesValueException() raises ValueError
def test_exception():
    # "with raises(ValueError)" tells pytest: this block must raise ValueError
    with raises(ValueError):
        raisesValueException()

"""
raises(ValueError) is a context manager provided by pytest.

It expects the code inside the block to raise ValueError.

If it does, the test passes. If not, the test fails.
"""
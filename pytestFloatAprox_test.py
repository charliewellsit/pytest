from pytest import approx

def test_float():
    assert 0.1 + 0.2 == 0.3
# it doesn't pass.

# As shown below. You need approx for float.
def test_float_approx():
    assert approx(0.1+0.2) == 0.3
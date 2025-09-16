"""
Fixtures can return data for tests.
With params=[...], pytest runs the test once for each value.
"""
import pytest

@pytest.fixture(params=[1,2,3])
def setup (request):
    retVal = request.param
    print ("\nSetup! retVal = {}".format(retVal))
    return retVal

def test2(setup):
    print("\nsetup ={}".format (setup))
    assert True

"""
============================= test session starts =============================
collected 3 items

test_example.py::test2[1] 
Setup! retVal = 1
In test2, setup = 1
PASSED

test_example.py::test2[2] 
Setup! retVal = 2
In test2, setup = 2
PASSED

test_example.py::test2[3] 
Setup! retVal = 3
In test2, setup = 3
PASSED

============================== 3 passed in 0.01s ==============================
"""
import pytest

@pytest.fixture()
def setup():
    print('\nsetup')

def test1(setup):
    print('test1')
    assert True

@pytest.mark.usefixtures('setup')
def test2():
    print('test2')
    assert True

# You can do '@pytest.fixture(autouse=True)' to have setup run at all tests.

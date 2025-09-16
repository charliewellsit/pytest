"""
Test Fixtures can have the following four different scopes which specify how often the fixture will be called:

• Function - Run the fixture once for each test
• Class - Run the fixture once for each class of tests
• Module - Run once when the module goes in scope
• Session - The fixture is run when pytest starts.
"""
import pytest

# Session-level fixture (runs once per whole test run)
@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session")

# Module-level fixture (runs once per module)
@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup Module")

# Function-level fixture (runs before each function)
@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")

def test1():
    print("Executing test1!")
    assert True

def test2():
    print("Executing test2!")
    assert True

# Another module-level fixture (just for demonstration)
@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nSetup Module2")

# Class-level fixture (runs once per class)
@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\nSetup Class2")

# Another function-level fixture
@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\nSetup Function2")

class TestClass:
    def test_it(self):
        print("TestIt")
        assert True

    def test_it2(self):
        print("TestIt2")
        assert True

"""
What Are Test Doubles?

• Almost all code depends (i.e. collaborates) with other parts of the system.

• Those other parts of the system are not always easy to
  replicate in the unit test environment or would make tests slow if used directly.

• Test doubles are objects that are used in unit tests as replacements
  to the real production system collaborators.

=============================

types of lest Doubles

• Dummy - Objects that can be passed around as necessary but
  do not have any type of test implementation and should never be used.

• Fake - These object generally have a simplified functional
  implementation of a particular interface that is adequate for
  testing but not for production.

• Stub - These objects provide implementations with
  canned answers that are suitable for the test.

• Spies - These objects provide implementations that
  record the values that were passed in so they can be used by the test.

• Mocks - These objects are pre-programmed to expect specific
  calls and parameters and can throw exceptions when necessary.
"""

"""
Mock frameworks
    1.unittest.mock
        it provides Mock Class, MagicMock Class.
    2.PyTest Monkeypatch Test Fixture
        it allow a test to dynamically replace:
        • module and class attributes
        • Dictionary entries
        • Environment Variables
    
"""

# tests/read_file_test.py

# 1) Imports
from pytest import raises            # context manager to assert exceptions in tests
from unittest.mock import MagicMock  # create fake objects for testing
import os                            # to check file existence
import pytest                        # pytest itself (not strictly required here but common)

# 2) Code under test
def readFromFile(filename):
    # Check if the file exists first; if not, raise an error.
    if not os.path.exists(filename):
        raise Exception("Bad File")

    # Open the file for reading and read one line.
    infile = open(filename, "r")
    line = infile.readline()
    infile.close()   # close the file (good practice)
    return line

# 3) Fixture to mock built-in open() so tests don't touch the real filesystem
@pytest.fixture()
def mock_open(monkeypatch):
    # Create a fake file-like object
    mock_file = MagicMock()
    # When someone calls mock_file.readline(), return this string
    mock_file.readline = MagicMock(return_value="test line")

    # Create a fake open() that returns our fake file object
    mock_open = MagicMock(return_value=mock_file)

    # Replace builtins.open with our fake open for the duration of the test
    monkeypatch.setattr("builtins.open", mock_open)

    # Return the fake open so tests can make assertions on how it was called
    return mock_open

# 4) Test: file exists -> read one line and return it
def test_returnsCorrectString(mock_open, monkeypatch):
    # Make os.path.exists(...) return True (pretend the file exists)
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)

    # Call the function under test
    result = readFromFile("blah")

    # Verify open() was called with the expected args
    mock_open.assert_called_once_with("blah", "r")

    # And verify the function returned the mocked line
    assert result == "test line"

# 5) Test: file does not exist -> function should raise Exception
def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    # Make os.path.exists(...) return False (pretend the file is missing)
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)

    # Expect Exception to be raised when calling the function
    with raises(Exception):
        readFromFile("blah")


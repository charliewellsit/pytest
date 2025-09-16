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

"""
1. "blah" and "r"

"blah" is just the filename string passed into readFromFile.
In a real program, it would be something like "data.txt" or "users.csv".
In the test, the exact string doesn’t matter because we’ve patched open and os.path.exists. The test just needs some filename input.
"r" is the mode used when opening a file in Python:
"r" → read (file must already exist, read-only).
"w" → write (creates file if missing, truncates if exists).
"a" → append (add new data at the end).
"rb", "wb", "ab" → same as above but binary mode.
"r+", "w+" → read + write.
So in the test, "blah" is the test filename, and "r" is making sure we opened it for reading.

2. mock_open.assert_called_once_with("blah", "r")
This is a MagicMock assertion.
mock_open is a fake replacement for open.
When readFromFile("blah") is called, it internally does open("blah", "r").
Since open has been monkeypatched → it’s actually calling mock_open("blah", "r").
assert_called_once_with(...) verifies two things:
mock_open was called exactly once
It was called with the exact arguments "blah" and "r"
If mock_open was called:
with wrong arguments → test fails
multiple times → test fails
never → test fails

3. Other common MagicMock assertions
Here are some you’ll often use:
mock.assert_called()
✅ Asserts the mock was called at least once.
mock.assert_not_called()
✅ Asserts the mock was never called.
mock.assert_called_once()
✅ Asserts the mock was called exactly once (arguments don’t matter).
mock.assert_called_with(arg1, arg2, …)
✅ Asserts the last call to the mock was with these arguments.
mock.assert_any_call(arg1, arg2, …)
✅ Asserts that the mock was called with these arguments at least once (good for when it’s called multiple times).
mock.call_args / mock.call_args_list
✅ Introspect the exact arguments the mock was called with (useful in more complex tests).
"""
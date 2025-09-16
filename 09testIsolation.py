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

from pytest import raises
from unittest.mock import MagicMock
import os
import pytest


# Function we want to test
def readFromFile(filename):
    # Check if file exists
    if not os.path.exists(filename):
        raise Exception("Bad File")  # Raise exception if file not found

    # If file exists, open it and read one line
    infile = open(filename, "r")
    line = infile.readline()
    return line


# -------- Fixtures (for mocking) --------

# This fixture replaces the built-in open() with a mock object
@pytest.fixture()
def mock_open(monkeypatch):
    # Create a fake file object
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")  # Fake file will return "test line"

    # Replace open() with this fake file
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)

    return mock_open


# -------- Tests --------

# Test: if the file exists, we should read "test line"
def test_returnsCorrectString(mock_open, monkeypatch):
    # Mock os.path.exists to always return True
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)

    # Call function under test
    result = readFromFile("blah")

    # Verify open() was called with correct arguments
    mock_open.assert_called_once_with("blah", "r")

    # Verify the return value is as expected
    assert result == "test line"


# Test: if the file does not exist, an Exception should be raised
def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    # Mock os.path.exists to always return False
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)

    # Check that our function raises an Exception
    with raises(Exception):
        readFromFile("blah")

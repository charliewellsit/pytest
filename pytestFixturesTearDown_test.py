import pytest
"""
Teardown code is called after a fixture goes out of scope

There are 2 methods.
'yield'
'addfinalizer' (request-context's method)
"""

# 1. 'yield'
@pytest.fixture()
def fixture():
    print('Setup')
    yield
    print('tear down')
# 'yield' replaces 'return'

# 2. addfinalizer
@pytest.fixture()
def fixture2(request):
    print('Setup')
    def tear_down():
        print('tear down')
    request.addfinalizer(tear_down)

@pytest.fixture()
def setup1():
    print('\nSetup1')
    yield
    print('\nTeardown1')

@pytest.fixture()
def setup2(request):
    print('\nSetup2')
    def teardown_a():
        print('\nTeardown A')
    def teardown_b():
        print('\nTeardown B')

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print('test1')
    assert True
def test2(setup2):
    print('test2')

"""
output: 
===================
collected 2 items

Setup1
test1
Teardown1
.
Setup2
test2
Teardown B
Teardown A
.
====================
"""

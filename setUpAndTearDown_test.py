def setup_module(module):
    print('setup module')

def teardown_module(module):
    print('teardown module')

def setup_function(function):
    if function == test1:
        print('\nsetup function test1')
    elif function == test2:
        print('\nsetup function test2')
    else:
        print('\nsetup unknown function')

def teardown_function(function):
    if function == test1:
        print('\nteardown function test1')
    elif function == test2:
        print('\nteardown function test2')
    else:
        print('\nteardown unknown function')

def test1():
    print('executing test1')
    assert True
def test2():
    print('executing test2')
    assert True
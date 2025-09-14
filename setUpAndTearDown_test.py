# Purpose of setup/teardown
# Setup → Prepare environment
# Teardown → Clean environment


# module-level setup/teardown
def setup_module(module):
    print('setup module')

def teardown_module(module):
    print('teardown module')

# function-level setup/teardown
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

# plain test functions
def test1():
    print('executing test1')
    assert True

def test2():
    print('executing test2')
    assert True

# class-level setup/teardown
class TestClassExample:

    @classmethod
    def setup_class(cls):
        print('\nsetup class TestClassExample')

    @classmethod
    def teardown_class(cls):
        print('teardown class TestClassExample')

    def setup_method(self, method):
        print(f'\nsetup method {method.__name__}')

    def teardown_method(self, method):
        print(f'teardown method {method.__name__}')

    def test3(self):
        print('executing test3')
        assert True

    def test4(self):
        print('executing test4')
        assert True

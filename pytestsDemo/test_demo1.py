#any pytest file should start with test_ or ends with _test
#pytest method name should start with test
#any code should be wrapped in a method only
#method name should have sense
# -k stands for methods name execution, -s for logs in output, -v for more info like metadata
#you can run specific file with pytest <filename> command
#to run particular test cases such as smoke or sanity we will use the mark concept which run the test cases which marked as smoke or sanity
#you can mark(tag) tests @pytest.mark.smoke and run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail - this will execute the method but cannot harm the execution
#fixtures are used as set up and tear down methods for test cases to generalize and make it available to each and every test case methods


import pytest


@pytest.mark.smoke
def test_firstprogram():
    print("hello world")


@pytest.mark.xfail
def test_greet():
    print("Good morning")

def test_second_demo():
    print("hello everyone")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)

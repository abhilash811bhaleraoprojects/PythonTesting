#fixtures are basically functions attached to the test methods which runs before/after test function is executed
#these are the set of resources that have to be set-up before & cleaned up once the test execution is completed
#yield : all line of code after yield keyword will get executed after test case complete execution
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I am execute steps in fixtureDemo method ")


    def test_fixtureDemo1(self):
        print("I am execute steps in fixtureDemo1 method ")


    def test_fixtureDemo2(self):
        print("I am execute steps in fixtureDemo2 method ")


    def test_fixtureDemo3(self):
        print("I am execute steps in fixtureDemo3 method ")



#any pytest file should start with test_ or ends with _test
#pytest method name should start with test
#any code should be wrapped in a method only
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_greet_2():
    msg = "Hello"
    assert  msg == "Good morning", "Test failed as strings does not match"


def test_second_program():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"
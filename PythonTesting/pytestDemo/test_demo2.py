# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello" #operations
    assert msg == "Hi", "Test Failed because strings do not match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == b, "Addition does not match"


@pytest.fixture()
def setup():
    print("I will be executing first")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")
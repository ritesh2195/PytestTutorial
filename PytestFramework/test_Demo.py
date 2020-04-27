import pytest


def test_first():
    print("Hello World")

@pytest.mark.smoke
def test_Second():
    print("Good Morning")
    msg = "Good Morning"
    # assert (msg == "good")

@pytest.mark.skip
def test_SecondDemo():
    print(3*4)

@pytest.mark.xfail
def test_fourth():
    print("Good Afternoon")


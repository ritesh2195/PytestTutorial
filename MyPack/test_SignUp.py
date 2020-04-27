import pytest


@pytest.fixture()
def setUp():
    print(" Opening URL to login")
    yield
    print(" Closing browser after login")


def test_SignUpByemail(setUp):
    print(" This is SignUp by email")


def test_SignUpByfacebook(setUp):
    print(" This is SignUp by facebook")

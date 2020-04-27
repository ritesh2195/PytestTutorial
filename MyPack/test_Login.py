import pytest


@pytest.fixture()
def setUp():
    print(" Opening URL to login")
    yield
    print(" Closing browser after login")


def test_loginByemail(setUp):
    print(" This is Login by email")


def test_loginByfacebook(setUp):
    print(" This is Login by facebook")

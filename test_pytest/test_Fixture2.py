import pytest

@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once after every method")

def testMethod1(setup):
    print("this is test method1")

def testMethod2(setup):
    print("this is test method2")
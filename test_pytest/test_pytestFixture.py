import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    print("Once before every method")

def testMethod1(setup):
    print("this is test method1")

def testMethod2(setup):
    print("this is test method2")
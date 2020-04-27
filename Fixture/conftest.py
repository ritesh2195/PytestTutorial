import pytest


@pytest.fixture(scope="class")
def setUp():
    print("Before Method")
    yield
    print("..After Method")


@pytest.fixture()
def dataLoad():
    print("Data is  being created")
    return ["Ritesh", "Ranjan", "Mishra"]


@pytest.fixture(params=[("ritesh", "chrome"), ("ranjan", "firefox"), ("mishra", "IE")])
def dataDriven(request):
    return request.param

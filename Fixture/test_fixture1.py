import pytest


@pytest.mark.usefixtures("setUp")
class TestExample:

    def test_Second2(self):
        print("Good Morning")
        msg = "Good Morning"
        # assert (msg == "good")

    def test_SecondDemo22(self):
        print("Multiplication is " + str(3 * 4))

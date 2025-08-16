import pytest
# def test_fixture():
#     a=4
#     b=6
#     assert a+2 == b , "addition do not match"

# @pytest.fixture()
# def setup():
#         print("setup")
#         yield
#         print("i will be  executed last")
import pytest

@pytest.mark.usefixtures("setup")
class Testexample:

    def test_fixdemo(self):
        print("stupid")

    def test_fixdemo(self):
        print("stupid")

    def test_fixdemo(self):
        print("stupid")
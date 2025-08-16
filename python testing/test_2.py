import pytest


@pytest.mark.smoke
def test_first():
    msg = "Hello"
    assert msg == "hi" , "test case failed"

def test_creditcard():
    a=4
    b=5
    assert a+2 == 6, "addition do not match"



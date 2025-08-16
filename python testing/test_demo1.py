import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_firstp():
    print("hello world")
@pytest.mark.xfail
def test_firstcreditcard():
    print("Good morning")


def test_crossbrowser(crossbrowser):
    print(crossbrowser)
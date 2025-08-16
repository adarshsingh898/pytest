import pytest
@pytest.fixture(scope="class")
def dataload():
        print("user profile is being created")
        return ["Rahul","Shetty","rahuladarsg.com"]



@pytest.fixture(params=["chrome","firefox","safari","opera"])
def crossbrowser(request):

    return request.param

# def dataload():
#     print("user profile is being created")
#     return ["Rahul", "Shetty", "rahuladarsg.com"]


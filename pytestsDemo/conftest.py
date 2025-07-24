import pytest
@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Abhilash", "Bhalerao", "abhilasbb@gmail.com"]

@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return request.param
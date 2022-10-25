import pytest


@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("User Profile data is being created")
    return["Stefan", "Nguyen", "mein-mmo.de"]

@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def crossBrowser(request):
    return request.param
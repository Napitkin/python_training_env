import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture
def app_1(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

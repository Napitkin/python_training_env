import pytest
from fixture.application import Application


@pytest.fixture #(scope="session") Так все тесты не запускаются, спотыкаются и крашатся...
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

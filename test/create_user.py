# -*- coding: utf-8 -*-
from env.model.user import User
from env.fixture.application_create_user import Application_create_user
import pytest


@pytest.fixture
def app(request):
    fixture = Application_create_user()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_user(app):
    app.login("admin", "secret")
    app.create_user(User("Kirill", "Napitkin", "Napitkin2", "Da", "Rus_Company", "Moscow Kremlin str.",
              "7777777", "2222222222", "55555555", "kirill@kirill.ru", "22", "August", "1986",
              "10", "August", "2000"))
    app.logout()

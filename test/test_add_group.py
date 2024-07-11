# -*- coding: utf-8 -*-
import pytest
from env.model.group import Group
from env.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login("admin", "secret")
    app.open_groups_page()
    app.create_group(Group("Keks", "Keks1", "KeksGroup"))
    app.logout()


def test_add_empty_group(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()

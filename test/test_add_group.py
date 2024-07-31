# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group("Keks", "Keks1", "KeksGroup"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))

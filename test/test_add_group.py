# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("Keks", "Keks1", "KeksGroup"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret") #- При не закомментированной данной строки, тест зависает на странице после создания заполннеой группы.
    app.group.create(Group("", "", ""))
    app.session.logout()

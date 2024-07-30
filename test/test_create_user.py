# -*- coding: utf-8 -*-
from model.user import User


def test_create_user(app):
    # app.session.login("admin", "secret")
    app.user.create(User("Kirill", "Napitkin", "Napitkin2", "Da", "Rus_Company", "Moscow Kremlin str.",
                         "7777777", "2222222222", "55555555", "kirill@kirill.ru", "22", "August", "1986",
                         "10", "August", "2000"))
    # app.session.logout()

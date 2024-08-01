# -*- coding: utf-8 -*-
from model.user import User


def test_create_user(app):
    old_users = app.user.get_user_list()
    user = User("Kirill", "Napitkin", "Napitkin2", "Da", "Rus_Company", "Moscow Kremlin str.",
                "7777777", "2222222222", "55555555", "kirill@kirill.ru", "22", "August", "1986",
                "10", "August", "2000")
    app.user.create(user)
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

# -*- coding: utf-8 -*-
from model.user import User


def test_create_user(app, db, json_users, check_ui):
    user = json_users
    # Загружаем список пользователей
    old_users = db.get_user_list()
    # Создаем нового пользователя
    app.user.create(user)
    # Снова загружаем список пользователей
    new_users = db.get_user_list()
    old_users.append(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)

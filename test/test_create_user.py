# -*- coding: utf-8 -*-
from model.user import User


def test_create_user(app, json_users):
    user = json_users
    # Загружаем список пользователей
    old_users = app.user.get_user_list()
    # Создаем нового пользователя
    app.user.create(user)
    # Снова загружаем список пользователей
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

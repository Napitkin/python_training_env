# -*- coding: utf-8 -*-
from model.user import User


def test_create_user(app):
    # Загружаем список пользователей
    old_users = app.user.get_user_list()
    user = User("Kirill", "Napitkin", "7777777", "2222222222", "55555555", "99900009")
    # Создаем новую группу
    app.user.create(user)
    # Снова загружаем список групп
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

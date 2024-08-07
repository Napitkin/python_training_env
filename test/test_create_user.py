# -*- coding: utf-8 -*-
from model.user import User
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    symbol = string.digits + "" * 3
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


test_data = [
    User(first_name=random_string("firstname", 10), last_name=random_string("lastname", 10), address=random_string("address", 30),
         tel_home=random_string("home", 20), tel_mobile=random_number("mobile", 20), tel_work=random_number("work", 20),
         email=random_string("email", 20), email_2=random_string("email2", 20), email_3=random_string("email3", 20))
    for i in range(2)
]


@pytest.mark.parametrize("user", test_data, ids=[repr(x) for x in test_data])
def test_create_user(app, user):
    # Загружаем список пользователей
    old_users = app.user.get_user_list()
    # Создаем нового пользователя
    app.user.create(user)
    # Снова загружаем список пользователей
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

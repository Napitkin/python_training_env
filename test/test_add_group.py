# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


# Случайно сгенерированная строка
def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


test_data = [Group("", "", "")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    # Загрузка списка групп
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # Проверка длинны списков
    assert len(old_groups) + 1 == app.group.count()
    # Загрузка изменённого списка групп
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

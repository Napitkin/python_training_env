# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    # Загрузка списка групп
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # Проверка длинны списков
    assert len(old_groups) + 1 == app.group.count()
    # Загрузка изменённого списка групп
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

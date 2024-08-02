# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Загрузка списка групп
    old_groups = app.group.get_group_list()
    # Создание новой группы
    group = Group("Keks", "Keks1", "KeksGroup")
    app.group.create(group)
    # Проверка длинны списков
    assert len(old_groups) + 1 == app.group.count()
    # Загрузка изменённого списка групп
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_empty_group(app):
#     # Загрузка списка групп №2
#     old_groups = app.group.get_group_list()
#     # Создание новой группы
#     group = Group("", "", "")
#     app.group.create(group)
#     # Загрузка изменённого списка групп
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

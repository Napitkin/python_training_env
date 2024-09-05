from pytest_bdd import given, when, then
from model.group import Group
import random


@given ('a group list', target_fixture="group_list")
def group_list(db):
    return db.get_group_list()

@given('I am on the group page')
def on_group_page(app):
    app.group.open_groups_page()

@given ('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list', target_fixture="new_group_list")
def add_new_group(app, new_group):
    app.group.create(new_group)
    return app.group.get_group_list()

@then('the new group list is equal to the old list with the added group', target_fixture="new_group_list")
def verify_group_added(app, group_list, new_group):
    old_groups = group_list
    new_groups = app.group.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list', target_fixture="non_empty_group_list")
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    return db.get_group_list()

@given ('a random group from the list', target_fixture="random_group")
def random_group(group_list):
    return random.choice(group_list)

@when('I delete the group from the list', target_fixture="new_group_list")
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then ('The new group list is equal to the old list without the deleted group', target_fixture="new_group_list")
def verify_group_deleted(db, non_empty_group_list, random_group, check_ui, app):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) -1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

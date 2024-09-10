import random
from model.group import Group
from model.user import User

def test_add_user_to_group(app, db, orm):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    if len(app.user.get_user_list()) == 0:
        app.user.create(User("test", "123", "123", "4444", "6666666", "45446464",
                             "nmail22222@mail.ru", "nmail_444444@mail.ru", "nmail_888888@mail.ru"))
    all_groups = app.group.get_group_list()
    random_group = random.choice(all_groups)
    if len(orm.get_users_not_in_group(random_group)) == 0:
        app.user.create(User("test", "123", "123", "4444", "6666666", "45446464",
                             "nmail22222@mail.ru", "nmail_444444@mail.ru", "nmail_888888@mail.ru"))
    old_users_not_in_group = orm.get_users_not_in_group(random_group)
    random_user = random.choice(old_users_not_in_group)
    app.user.add_user_to_group(random_user.id, random_group.id)
    old_users_not_in_group.remove(random_user)
    new_users_not_in_group = orm.get_users_not_in_group(random_group)
    assert sorted(old_users_not_in_group, key=User.id_or_max) == sorted(new_users_not_in_group, key=User.id_or_max)

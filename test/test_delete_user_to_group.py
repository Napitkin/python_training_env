import random
from model.group import Group
from model.user import User


def test_delete_user_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_user_list()) == 0:
        app.user.create(User("test", "123", "123", "4444", "6666666", "45446464",
                             "nmail22222@mail.ru", "nmail_444444@mail.ru", "nmail_888888@mail.ru"))
    old_groups = orm.get_group_list()
    old_users = orm.get_user_list()
    group = random.choice(old_groups)
    user = random.choice(old_users)
    app.user.delete_user_from_group(user, group)
    new_groups = orm.get_group_list()
    assert len(old_groups) == len(new_groups)
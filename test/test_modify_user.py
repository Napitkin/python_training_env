from model.user import User
from random import randrange


def test_modify_first_user(app):
    if app.user.count() == 0:
        app.user.create(
            User(first_name="test", last_name="123", tel_home="123", tel_mobile="123", tel_work="123", tel_fax="232399988774"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user = User("Kirill2", "Napitkin2", "77447773", "22224422", "55522555", "99900009")
    user.id = old_users[index].id
    app.user.modify_user_by_index(index, user)
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

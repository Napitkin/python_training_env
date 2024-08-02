from model.user import User
from random import randrange


def test_modify_first_user(app):
    if app.user.count() == 0:
        app.user.create(
            User(first_name="test", last_name="123", nick_name="123", title="123", company="123", address="123", tel_home="123", tel_mobile="123", tel_work="123", email="123", b_day="123",
                 b_month="123", b_year="123", anniversary_day="123", anniversary_month="123",
                 anniversary_year="123"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user = User("Kirill2", "Napitkin2", "Napitkin4", "Da", "Rus_Company", "Minissota Winter str.",
                "77447773", "22224422", "55522555", "kirill@kirill.com", "23", "April", "1988",
                "12", "August", "2004")
    user.id = old_users[index].id
    app.user.modify_user_by_index(index, user)
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

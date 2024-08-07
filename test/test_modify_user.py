from model.user import User
from random import randrange


def test_modify_first_user(app):
    if app.user.count() == 0:
        app.user.create(
            User("test", "123", "123", "123", "123", "123",
                 "kmail@mail.ru", "kmail_2@mail.ru", "kmail_3@mail.ru"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user = User("Kirill2", "Napitkin2", "Berlin Turtle str.", "77447773", "22224422", "55522555",
                "kmail1111@mail.ru", "kmail_22222@mail.ru", "kmail_33333@mail.ru")
    user.id = old_users[index].id
    app.user.modify_user_by_index(index, user)
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

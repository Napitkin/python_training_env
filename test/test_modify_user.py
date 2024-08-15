from model.user import User
import random


def test_modify_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create(
            User("test","123", "123", "4444", "6666666", "45446464",
                 "nmail22222@mail.ru", "nmail_444444@mail.ru", "nmail_888888@mail.ru"))
    old_users = db.get_user_list()
    modify_user = random.choice(old_users)
    modify_user.name = User("Kirill2", "Napitkin2", "Berlin Turtle str.", "77447773", "22224422", "55522555",
                            "kmail1111@mail.ru", "kmail_22222@mail.ru", "kmail_33333@mail.ru")
    app.user.modify_user_by_id(modify_user, modify_user.id)
    new_users = db.get_user_list()
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)


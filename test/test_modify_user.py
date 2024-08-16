from model.user import User
import random


def test_modify_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create(
            User("test","123", "123", "4444", "6666666", "45446464",
                 "nmail22222@mail.ru", "nmail_444444@mail.ru", "nmail_888888@mail.ru"))
    old_users = db.get_user_list()
    modify_user = random.choice(old_users)
    user = User("Kirill2", "Napitkin2", "Berlin Turtle str.", "77447773", "22224422", "55522555",
                            "kmail11111@mail.ru", "kmail_222222@mail.ru", "kmail_333333@mail.ru")
    app.user.modify_user_by_id(user, modify_user.id)
    # Прямо заменяем объект в списке
    old_users[old_users.index(modify_user)] = user
    new_users = db.get_user_list()
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)

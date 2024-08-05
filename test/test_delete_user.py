from model.user import User
from random import randrange


def test_delete_some_user(app):
    if app.user.count() == 0:
        app.user.create(
            User(first_name="test", last_name="123", tel_home="123", tel_mobile="123", tel_work="123", tel_fax="232399988774"))
    old_users = app.user.get_user_list()
    # Выбор пользователя случаным образом
    index = randrange(len(old_users))
    # Вспомогательный метод с передачей случайного порядкового номера пользователя
    app.user.delete_user_by_index(index)
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[index:index+1] = []
    assert old_users == new_users

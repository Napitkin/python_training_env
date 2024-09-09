import random
from model.group import Group
from model.user import User

def test_add_user_to_group(app, db, orm, max_attempts=8):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_user_list()) == 0:
        app.user.create(User("test", "123", "123", "4444", "6666666", "45446464",
                             "nmail22222@mail.ru", "nmail_444444@mail.ru", "nmail_888888@mail.ru"))
    old_groups = orm.get_group_list()
    old_users = orm.get_user_list()
    attempts = 0
    user = None
    group = None
    while attempts < max_attempts:
        group = random.choice(old_groups)
        # Выбираем пользователей, которые еще не состоят в выбранной группе
        available_users = [user for user in old_users if user not in orm.get_users_in_group(group)]
        if len(available_users) > 0:
            user = random.choice(available_users)
            break
        attempts = attempts + 1
        print(f"Попытка {attempts}: нет доступных пользователей для группы {group.id}")
    if user is None:
        raise Exception(f"Не удалось найти подходящего пользователя после {max_attempts} попыток.")
    # Добавляем найденного пользователя в выбранную группу
    app.user.add_user_to_group(user, group)
    # Обновляем данные пользователей в группе после добавления
    users_in_group = orm.get_users_in_group(group)
    # Проверяем, что пользователь действительно добавлен в группу
    assert user in users_in_group, f"Пользователь {user.id} не был добавлен в группу {group.id}"

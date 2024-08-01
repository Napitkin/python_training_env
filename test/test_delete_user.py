from model.user import User


def test_delete_first_user(app):
    if app.user.count() == 0:
        app.user.create(
            User(first_name="test", last_name="123", nick_name="123", title="123", company="123", address="123", tel_home="123", tel_mobile="123", tel_work="123", email="123", b_day="123",
                 b_month="123", b_year="123", anniversary_day="123", anniversary_month="123",
                 anniversary_year="123"))
    old_users = app.user.get_user_list()
    app.user.delete_first_user()
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)

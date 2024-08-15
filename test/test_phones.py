import re
from model.user import User


def test_names_emails_phones_and_address_on_home_page(app):
    user_from_home_page = app.user.get_user_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.last_name == user_from_edit_page.last_name
    assert user_from_home_page.first_name == user_from_edit_page.first_name
    assert user_from_home_page.address == user_from_edit_page.address


def test_phones_on_user_view_page(app):
    user_from_view_page = app.user.get_user_from_view_page(0)
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_view_page.tel_home == user_from_edit_page.tel_home
    assert user_from_view_page.tel_mobile == user_from_edit_page.tel_mobile
    assert user_from_view_page.tel_work == user_from_edit_page.tel_work


def test_all_user_data_on_home_page(app, db):
    if app.user.count() == 0:
        app.user.create(
            User("test", "123", "Moscow Dmt.", "4444", "6666666", "45446464",
                 "nmail22222@mail.ru", "nmail_444444@mail.ru", "nmail_888888@mail.ru"))
    users_from_db = db.get_user_list()
    users_from_home_page = app.user.get_user_list()
    assert sorted(users_from_db, key=User.id_or_max) == sorted(users_from_home_page, key=User.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.tel_home, user.tel_mobile, user.tel_work]))))


def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [user.email, user.email_2, user.email_3])))

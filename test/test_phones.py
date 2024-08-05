import re


def test_phones_on_home_page(app):
    user_from_home_page = app.user.get_user_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.tel_home == clear(user_from_edit_page.tel_home)
    assert user_from_home_page.tel_mobile == clear(user_from_edit_page.tel_mobile)
    assert user_from_home_page.tel_work == clear(user_from_edit_page.tel_work)
    # assert user_from_view_page.tel_fax == user_from_edit_page.tel_fax


def test_phones_on_user_view_page(app):
    user_from_view_page = app.user.get_user_from_view_page(0)
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_view_page.tel_home == user_from_edit_page.tel_home
    assert user_from_view_page.tel_mobile == user_from_edit_page.tel_mobile
    assert user_from_view_page.tel_work == user_from_edit_page.tel_work
    assert user_from_view_page.tel_fax == user_from_edit_page.tel_fax


def clear(s):
    return re.sub("[()  -]", "", s)

import re


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
    # assert user_from_view_page.tel_secondary == user_from_edit_page.tel_secondary


def clear(s):
    return re.sub("[()  -]", "", s)


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.tel_home, user.tel_mobile, user.tel_work])))) #user.tel_secondary


def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.email, user.email_2, user.email_3]))))

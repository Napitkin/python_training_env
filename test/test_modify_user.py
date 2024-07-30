from model.user import User


def test_modify_first_user(app):
    # app.session.login(username="admin", password="secret")
    app.user.modify_first_user(User("Kirill2", "Napitkin2", "Napitkin4", "Da", "Rus_Company", "Minissota Winter str.",
                                    "77447773", "22224422", "55522555", "kirill@kirill.com", "23", "April", "1988",
                                    "12", "August", "2004"))
    # app.session.logout()

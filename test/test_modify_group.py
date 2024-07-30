from model.group import Group


def test_modify_group_name(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group(header="New_header"))
    app.session.logout()

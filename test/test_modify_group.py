from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="Name group modify"))
    app.group.open_groups_page()
    app.session.log_out()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(header="Header group modify"))
    app.group.open_groups_page()
    app.session.log_out()

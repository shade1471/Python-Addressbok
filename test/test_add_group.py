from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name='The best group!', header='My new header', footer='My new footer'))
    app.group.open_groups_page()
    app.session.log_out()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name='', header='', footer=''))
    app.group.open_groups_page()
    app.session.log_out()

def test_delete_all_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_all_groups()
    app.group.open_groups_page()
    app.session.log_out()


def test_delete_first_group(app):
    app.session.login("admin", "secret")
    app.group.delete_first_group()
    app.group.open_groups_page()
    app.session.log_out()

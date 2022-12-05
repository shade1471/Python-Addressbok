from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="Name group modify"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="Header group modify"))

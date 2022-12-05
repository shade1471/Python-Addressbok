from model.group import Group


def test_delete_all_group(app):
    app.group.delete_all_groups()


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New best Group!"))
    app.group.delete_first_group()

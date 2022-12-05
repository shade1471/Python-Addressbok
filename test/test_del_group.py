from model.group import Group


def test_delete_all_group(app):

    if app.group.count() == 0:
        app.group.create(Group(name="New best Group!"))
    app.group.delete_all_groups()


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New best Group!"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # Удаление первого элемента
    old_groups[0:1] = []
    assert old_groups == new_groups
    # old_groups[0:1] = []
    # assert old_groups == new_groups

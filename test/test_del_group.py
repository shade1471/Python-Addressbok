from random import randrange

from model.group import Group


def test_delete_all_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New best Group!"))
    app.group.delete_all_groups()


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New best Group!"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # Удаление элемента по индексу
    old_groups[index:index + 1] = []
    assert old_groups == new_groups
    # old_groups[0:1] = []
    # assert old_groups == new_groups

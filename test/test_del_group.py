import random
from random import randrange

from model.group import Group


def test_delete_all_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New best Group!"))
    app.group.delete_all_groups()


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New best Group!"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # Удаление элемента по индексу
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    # old_groups[0:1] = []
    # assert old_groups == new_groups

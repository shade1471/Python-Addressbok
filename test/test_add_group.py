from model.group import Group


# @pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    # group = Group(name='The best group!', header='My new header', footer='My new footer')
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


## Новые комменты для ветки

#ветка 3
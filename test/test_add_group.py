from model.group import Group


def test_add_group(app):
    app.group.create(Group(name='The best group!', header='My new header', footer='My new footer'))


def test_add_empty_group(app):
    app.group.create(Group(name='', header='', footer=''))


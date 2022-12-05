from model.contact import Contact

contact_one = Contact('Петр', 'Иванов', 'p.ivanov', 'staffcop', '89991118899')
contact_two = Contact('Иван', '', 'i.ivanov', 'staffcop', '89991112233')


def test_add_contact(app):
    app.contact.add(contact_one)


def test_add_contact_without_family(app):
    app.open_home_page()
    app.contact.add(contact_two)

# def test_edit_first_name_contact_one(app):
#     app.open_home_page()
#     app.session.login(username="admin", password="secret")
#     app.contact.edit_contact_first_name(contact_one.first_name, 'newFamily')
#     app.session.log_out()

def test_delete_all_contacts(app):
    app.session.login('admin', 'secret')
    app.contact.delete_all()
    app.session.log_out()

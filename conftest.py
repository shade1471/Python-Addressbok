import pytest
from model.contact import Contact
from fixture.application import Application

contact_one = Contact('Petr', 'Petrov', 'a.petrov', 'staffcop', '89991118899')
contact_two = Contact('Ivan', '', 'a.ivanov', 'staffcop', '89991112233')

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.log_out()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

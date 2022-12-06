import pytest
from model.contact import Contact
from fixture.application import Application

contact_one = Contact('Petr', 'Petrov', 'a.petrov', 'staffcop', '89991118899')
contact_two = Contact('Ivan', '', 'a.ivanov', 'staffcop', '89991112233')

fixture = None


@pytest.fixture(scope='session')
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.log_out()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='firefox')
    parser.addoption("--baseUrl", action="store", default='http://10.10.12.212/addressbook/')

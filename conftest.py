import json
import os.path

import pytest
from model.contact import Contact
from fixture.application import Application

contact_one = Contact('Petr', 'Petrov', 'a.petrov', 'staffcop', '89991118899')
contact_two = Contact('Ivan', '', 'a.ivanov', 'staffcop', '89991112233')

fixture = None
target = None


@pytest.fixture(scope='session')
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    # Путь к текущему файлу
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.login(username=target['username'], password=target['password'])
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
    parser.addoption("--target", action="store", default='target.json')

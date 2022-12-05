import pytest
from model.contact import Contact
from fixture.application import Application

contact_one = Contact('Petr', 'Petrov', 'a.petrov', 'staffcop', '89991118899')
contact_two = Contact('Ivan', '', 'a.ivanov', 'staffcop', '89991112233')


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


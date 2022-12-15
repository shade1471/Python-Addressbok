from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.drv = webdriver.Firefox()
        elif browser == 'chrome':
            self.drv = webdriver.Chrome()
        elif browser == 'ie':
            self.drv = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.drv.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        drv = self.drv
        drv.get(self.base_url)

    def destroy(self):
        self.drv.quit()

    def is_valid(self):
        try:
            self.drv.current_url
            return True
        except:
            return False


###fvgsdf
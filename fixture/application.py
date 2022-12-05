from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.drv = WebDriver()
        self.drv.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        drv = self.drv
        drv.get('http://10.10.12.212/addressbook/')

    def destroy(self):
        self.drv.quit()

    def is_valid(self):
        try:
            self.drv.current_url
            return True
        except:
            return False

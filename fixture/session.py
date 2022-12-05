from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        drv = self.app.drv
        self.app.open_home_page()
        drv.find_element(By.NAME, 'user').send_keys(username)
        drv.find_element(By.NAME, 'pass').send_keys(password)
        drv.find_element(By.CSS_SELECTOR, '[type=submit]').click()

    def log_out(self):
        drv = self.app.drv
        drv.find_element(By.LINK_TEXT, 'Logout').click()

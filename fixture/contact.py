from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        ### Add contact to address book ##
        drv = self.app.drv
        drv.find_element(By.LINK_TEXT, 'add new').click()
        drv.find_element(By.CSS_SELECTOR, '[name=firstname]').send_keys(contact.first_name)
        drv.find_element(By.CSS_SELECTOR, '[name=lastname]').send_keys(contact.last_name)
        drv.find_element(By.CSS_SELECTOR, '[name=nickname]').send_keys(contact.nickname)
        drv.find_element(By.CSS_SELECTOR, '[name=company]').send_keys(contact.company)
        drv.find_element(By.CSS_SELECTOR, '[name=mobile]').send_keys(contact.mobile_phone)
        drv.find_element(By.CSS_SELECTOR, '[name=submit]').click()

    def delete_all(self):
        drv = self.app.drv
        drv.find_element(By.ID, 'MassCB').click()
        drv.find_element(By.CSS_SELECTOR, '[value=Delete]').click()
        Alert(drv).accept()

    def edit_contact_first_name(self, name_before, name_after):
        drv = self.app.drv
        drv.find_element(By.XPATH, f'//td[contains(text(), {name_before})]/following-sibling::td/a/img').click()
        drv.find_element(By.NAME, 'modifiy').click()
        drv.find_element(By.CSS_SELECTOR, '[name=firstname]').clear()
        drv.find_element(By.CSS_SELECTOR, '[name=firstname]').send_keys(name_after)
        drv.find_element(By.CSS_SELECTOR, '[name=update]').click()

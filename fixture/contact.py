from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import re

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        drv = self.app.drv
        if text is not None:
            drv.find_element(By.NAME, field_name).clear()
            drv.find_element(By.NAME, field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            drv = self.app.drv
            self.app.open_home_page()
            self.contact_cache = []
            for row in drv.find_elements(By.NAME, 'entry'):
                cells = row.find_elements(By.TAG_NAME, 'td')
                first_name = cells[1].text
                last_name = cells[2].text
                id = cells[0].find_element(By.TAG_NAME, 'input').get_attribute('value')
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(first_name=first_name, last_name=last_name, all_phones_from_home_page=all_phones, id=id))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        drv = self.app.drv
        self.app.open_home_page()
        row = drv.find_elements(By.NAME, 'entry')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[7]
        cell.find_element(By.TAG_NAME, 'a').click()

    def open_contact_view_by_index(self, index):
        drv = self.app.drv
        self.app.open_home_page()
        row = drv.find_elements(By.NAME, 'entry')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[6]
        cell.find_element(By.TAG_NAME, 'a').click()

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

    # def edit_contact_first_name(self, name_before, name_after):
    #     drv = self.app.drv
    #     drv.find_element(By.XPATH, f'//td[contains(text(), {name_before})]/following-sibling::td/a/img').click()
    #     drv.find_element(By.NAME, 'modify').click()
    #     drv.find_element(By.CSS_SELECTOR, '[name=firstname]').clear()
    #     drv.find_element(By.CSS_SELECTOR, '[name=firstname]').send_keys(name_after)
    #     drv.find_element(By.CSS_SELECTOR, '[name=update]').click()

    def get_contact_info_from_edit_page(self, index):
        drv = self.app.drv
        self.open_contact_to_edit_by_index(index)
        first_name = drv.find_element(By.NAME, 'firstname').get_attribute('value')
        last_name = drv.find_element(By.NAME, 'lastname').get_attribute('value')
        id = drv.find_element(By.NAME, 'id').get_attribute('value')
        home_phone = drv.find_element(By.NAME, 'home').get_attribute('value')
        mobile_phone = drv.find_element(By.NAME, 'mobile').get_attribute('value')
        work_phone = drv.find_element(By.NAME, 'work').get_attribute('value')
        return Contact(first_name=first_name, last_name=last_name, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, id=id)

    def get_contact_from_view_page(self, index):
        drv = self.app.drv
        self.open_contact_view_by_index(index)
        text = drv.find_element(By.ID, 'content').text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)

from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        drv = self.app.drv
        self.open_groups_page()
        drv.find_elements(By.CSS_SELECTOR, '[name=new]')[0].click()
        self.fill_group_form(group)
        drv.find_element(By.CSS_SELECTOR, '[name=submit]').click()
        self.open_groups_page()
        self.group_cache = None

    def change_field_value(self, field_name, text):
        drv = self.app.drv
        if text is not None:
            drv.find_element(By.CSS_SELECTOR, field_name).clear()
            drv.find_element(By.CSS_SELECTOR, field_name).send_keys(text)

    def fill_group_form(self, group):
        drv = self.app.drv
        self.change_field_value('[name=group_name]', group.name)
        self.change_field_value('[name=group_header]', group.header)
        self.change_field_value('[name=group_footer]', group.footer)

    def open_groups_page(self):
        drv = self.app.drv
        if not (drv.current_url.endswith("/group/php") and len(drv.find_elements_by_name("new")) > 0):
            drv.find_element(By.LINK_TEXT, 'groups').click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        drv = self.app.drv
        self.open_groups_page()
        self.select_group_by_index(index)
        drv.find_element(By.CSS_SELECTOR, '[name=delete]').click()
        self.open_groups_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        drv = self.app.drv
        drv.find_elements(By.NAME, 'selected[]')[index].click()

    def delete_all_groups(self):
        drv = self.app.drv
        self.open_groups_page()
        list_groups = drv.find_elements(By.CSS_SELECTOR, '[method=post] .group input')
        for i in range(0, len(list_groups)):
            drv.find_elements(By.CSS_SELECTOR, '[method=post] .group input')[i].click()
        drv.find_elements(By.CSS_SELECTOR, '[name=delete]')[0].click()
        self.open_groups_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        drv = self.app.drv
        self.open_groups_page()
        self.select_group_by_index(index)
        drv.find_element(By.NAME, 'edit').click()
        self.fill_group_form(new_group_data)
        drv.find_element(By.NAME, 'update').click()
        self.open_groups_page()
        self.group_cache = None

    def count(self):
        drv = self.app.drv
        self.open_groups_page()
        return len(drv.find_elements(By.NAME, 'selected[]'))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            drv = self.app.drv
            self.open_groups_page()
            self.group_cache = []
            for element in drv.find_elements(By.CSS_SELECTOR, 'span.group'):
                text = element.text
                id = element.find_element(By.NAME, 'selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

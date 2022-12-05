from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        drv = self.app.drv
        self.open_groups_page()
        drv.find_elements(By.CSS_SELECTOR, '[name=new]')[0].click()
        self.fill_group_form(drv, group)
        drv.find_element(By.CSS_SELECTOR, '[name=submit]').click()

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
        drv.find_element(By.LINK_TEXT, 'groups').click()

    def delete_first_group(self):
        drv = self.app.drv
        self.open_groups_page()
        self.select_first_group()
        drv.find_element(By.CSS_SELECTOR, '[name=delete]').click()

    def select_first_group(self):
        drv = self.app.drv
        drv.find_element(By.NAME, 'selected[]').click()

    def delete_all_groups(self):
        drv = self.app.drv
        self.open_groups_page()
        list_groups = drv.find_elements(By.CSS_SELECTOR, '[method=post] .group input')
        for i in range(0, len(list_groups)):
            drv.find_elements(By.CSS_SELECTOR, '[method=post] .group input')[i].click()
        drv.find_elements(By.CSS_SELECTOR, '[name=delete]')[0].click()

    def modify_first_group(self, new_group_data):
        drv = self.app.drv
        self.open_groups_page()
        self.select_first_group()
        drv.find_element(By.NAME, 'edit').click()
        self.fill_group_form(new_group_data)
        drv.find_element(By.NAME, 'update').click()
        self.open_groups_page()
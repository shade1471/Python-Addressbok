from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        drv = self.app.drv
        self.open_groups_page()
        drv.find_elements(By.CSS_SELECTOR, '[name=new]')[0].click()
        drv.find_element(By.CSS_SELECTOR, '[name=group_name]').send_keys(group.name)
        drv.find_element(By.CSS_SELECTOR, '[name=group_header]').send_keys(group.header)
        drv.find_element(By.CSS_SELECTOR, '[name=group_footer]').send_keys(group.footer)
        drv.find_element(By.CSS_SELECTOR, '[name=submit]').click()

    def open_groups_page(self):
        drv = self.app.drv
        drv.find_element(By.LINK_TEXT, 'groups').click()

    def delete_first_group(self):
        drv = self.app.drv
        self.open_groups_page()
        drv.find_element(By.NAME, 'selected[]').click()
        drv.find_element(By.CSS_SELECTOR, '[name=delete]').click()

    def delete_all_groups(self):
        drv = self.app.drv
        self.open_groups_page()
        list_groups = drv.find_elements(By.CSS_SELECTOR, '[method=post] .group input')
        for i in range(0, len(list_groups)):
            drv.find_elements(By.CSS_SELECTOR, '[method=post] .group input')[i].click()
        drv.find_elements(By.CSS_SELECTOR, '[name=delete]')[0].click()

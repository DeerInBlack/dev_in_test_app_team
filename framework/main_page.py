from .page import Page


class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.navbar_button = driver.find_element_by_id('com.ajaxsystems:id/menuDrawer')

    def get_navbar_elements(self):
        self.navbar_button.click()
        menu_view = self.driver.find_element_by_id('com.ajaxsystems:id/compose_menu')
        menu_elements = menu_view.find_elements_by_id('com.ajaxsystems:id/title')
        base_layout = self.driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@resource-id="com.ajaxsystems:id/noHubs"]/android.view.ViewGroup')
        base_layout.click()
        return [el.text for el in menu_elements]

    def log_out(self):
        self.navbar_button.click()
        settings_button = self.driver.find_element_by_id('com.ajaxsystems:id/settings')
        settings_button.click()
        sign_out_field = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Sign Out"]')
        sign_out_field.click()

from .page import Page
from .login_page import LoginPage


class StartPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_button, self.create_account_button = driver.find_elements_by_class_name('android.widget.Button')

    def log_in(self):
        self.login_button.click()
        return LoginPage(self.driver)

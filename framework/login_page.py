from contextlib import suppress
import logging

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utils.appium_extensions import AnyExpectedConditionsWithOrder

from .page import Page
from .main_page import MainPage

LOGGER = logging.getLogger()


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field, self.password_field = driver.find_elements_by_class_name('android.widget.EditText')
        self.log_in_button = driver.find_elements_by_class_name('android.widget.Button')[-1]

    def fill_credentials_fields(self, email, password):
        self.clear_credentials_fields()
        self.email_field.send_keys(email)
        self.password_field.send_keys(password)

    def clear_credentials_fields(self):
        self.email_field.clear()
        self.password_field.clear()

    def attempt_log_in(self):
        # after click wait until we get to next page (Main page) or get error in snackbar element
        snackbar_cond = expected_conditions.presence_of_element_located(
            (By.ID, 'com.ajaxsystems:id/snackbar_text'))
        hub_add_cond = expected_conditions.presence_of_element_located(
            (By.ID, 'com.ajaxsystems:id/hubAdd'))
        wait = WebDriverWait(self.driver, 20)
        condition = AnyExpectedConditionsWithOrder(snackbar_cond, hub_add_cond)

        self.log_in_button.click()
        with suppress(TimeoutException):
            i, el = wait.until(condition)
            return (None, el.text) if i == 0 else (MainPage(self.driver), el.text)

        return None, ''

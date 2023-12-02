import pytest
import logging

from framework.start_page import StartPage
from framework.login_page import LoginPage
from framework.main_page import MainPage

LOGGER = logging.getLogger()


@pytest.fixture(scope='function')
def main_page_fixture(driver, valid_login_credentials):
    page = StartPage(driver).log_in()
    page.fill_credentials_fields(*valid_login_credentials)
    main_page, _ = page.attempt_log_in()
    if main_page is None:
        LOGGER.exception(f"Can't authorize to prepare Main page")
        raise RuntimeError()
    yield main_page
    if isinstance(main_page, MainPage):
        main_page.log_out()
    elif isinstance(page, LoginPage):
        page.go_back()

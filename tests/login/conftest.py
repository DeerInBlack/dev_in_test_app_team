import pytest
import logging

from framework.start_page import StartPage
from framework.login_page import LoginPage
from framework.main_page import MainPage

LOGGER = logging.getLogger()


@pytest.fixture(scope='function')
def login_page_fixture(driver):
    page = StartPage(driver).log_in()

    # just crutch to make possible resetting to Start page
    # can be changed by PageManager to get track of current page
    # and easier reset
    p_cont = [page]

    yield p_cont

    page = p_cont[0]
    if type(page) == LoginPage:
        page.go_back()
    elif type(page) == MainPage:
        page.log_out()

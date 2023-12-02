import subprocess
import logging
from dotenv import dotenv_values

import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities
from utils.appium_utils import get_appium_version

LOGGER = logging.getLogger()

config = dotenv_values()

APPIUM_HOST = config.get('APPIUM_HOST', 'localhost')
APPIUM_PORT = config.get('APPIUM_PORT', '4725')


@pytest.fixture(scope='session')
def run_appium_server():
    appium_service_args = ['--address', APPIUM_HOST,
                           '--port', APPIUM_PORT,
                           '--allow-insecure', 'adb_shell']

    appium_version = get_appium_version()

    # Add this arg for compatability with appium v1.x
    # optionally '/wd/hub' can be add to appium url when setting driver
    if appium_version and appium_version.split('.')[0] == 1:
        appium_service_args.extend(['--base-path', '/wd/hub'])
    # !Be careful if calling bellow Appium executable distinct from default,
    # as it's version may differ

    # Use subprocess instead of AppiumService().run() due to AppiumService is bugged
    appium_service = subprocess.Popen(['appium'] + appium_service_args,
                                      stdout=subprocess.DEVNULL,
                                      stderr=subprocess.DEVNULL,
                                      stdin=subprocess.DEVNULL,
                                      shell=True)

    # TODO: check if Appium process is already running on the same address and port and reopen it
    LOGGER.info(f"Appium server is running on `http://{APPIUM_HOST}:{APPIUM_PORT}")

    yield appium_service
    if appium_service.poll() is None:
        appium_service.terminate()


@pytest.fixture(scope='session')
def driver(run_appium_server):
    driver = webdriver.Remote(f"http://{APPIUM_HOST}:{APPIUM_PORT}",
                              android_get_desired_capabilities())
    yield driver
    if driver:
        driver.quit()


@pytest.fixture(scope='session')
def valid_login_credentials():
    valid_email = config.get('VALID_LOGIN_EMAIL', None)
    valid_password = config.get('VALID_LOGIN_PASSWORD', None)
    assert valid_email is not None and valid_password is not None
    return valid_email, valid_password

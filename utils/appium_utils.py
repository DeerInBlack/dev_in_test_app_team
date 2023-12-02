import subprocess
import logging
from typing import Optional

LOGGER = logging.getLogger()


def get_appium_version() -> Optional[str]:
    """
    :return: full appium server version
    """
    exec_result = subprocess.run(['appium', '--version'],
                                 shell=True, text=True, capture_output=True)
    if exec_result.returncode != 0:
        LOGGER.info("Can't get Appium server version")
        return None
    appium_version = exec_result.stdout.strip()
    LOGGER.info(f"Current default Appium version {appium_version}")
    return appium_version

import os
import subprocess
import logging

from typing import Optional

LOGGER = logging.getLogger()


def android_get_desired_capabilities() -> dict:
    desired_caps = {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        'ignoreHiddenApiPolicyError': True
    }
    if device_id := get_device_id():
        desired_caps['udid'] = device_id
        LOGGER.info(f"Selected device (udid:{device_id}) is added to desired capabilities")
    return desired_caps


def get_device_id() -> Optional[str]:
    """
    Checks available devices in ADB (https://developer.android.com/tools/adb).
    :return: first connected device in list
    """
    adb_path = os.path.join(os.environ['ANDROID_HOME'], 'platform-tools')

    exec_result = subprocess.run(['adb', 'devices', '-l'], cwd=adb_path, shell=True,
                                 capture_output=True, text=True)
    if exec_result.returncode != 0:
        LOGGER.warning("Can't get devices from ADB!")
        return None

    connections = exec_result.stdout.strip().split('\n')[1:]

    connected_devices = []
    for c in connections:
        device_id, state, *decs = c.split()
        if state == 'device':
            connected_devices.append({'udid': device_id,
                                      'description': dict((p.split(':')) for p in decs)})

    if not connected_devices:
        LOGGER.warning("ADB: no connected device's found! Check your connection")
        return None
    devices_short_info = '\\n'.join([d['udid'] + ':' + d['description']['model']
                                     for d in connected_devices])
    LOGGER.info(f"Available devices:\n {devices_short_info}")
    chosen_device = connected_devices[0]
    return chosen_device['udid']

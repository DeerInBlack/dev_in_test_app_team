import logging

import pytest
from pytest_lazyfixture import lazy_fixture

LOGGER = logging.getLogger()

test_data = [
    (('email', 'password'), False),
    (lazy_fixture('valid_login_credentials'), True),
    (('email@gmail.com', 'password'), False),
]
test_data_ids = [
    'Incorrect email format',
    'Valid credentials',
    'Incorrect email or password',
]


@pytest.mark.parametrize(['credentials', 'expected_result'],
                         test_data, ids=test_data_ids)
def test_user_login(login_page_fixture, credentials, expected_result):
    login_page_fixture[0].fill_credentials_fields(*credentials)
    result, massage = login_page_fixture[0].attempt_log_in()

    LOGGER.info(
        f"{'Can' if result else 'Can`t'} log with credentials {credentials} (message:{massage})")

    assert bool(result) == expected_result
    if result:
        login_page_fixture[0] = result

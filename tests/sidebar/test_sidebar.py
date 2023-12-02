import logging

import pytest

LOGGER = logging.getLogger()


def test_sidebar_elements(main_page_fixture):
    expected_elements = ['App Settings', 'Help', 'Report a Problem', 'Video Surveillance']
    elements_present = main_page_fixture.get_navbar_elements()
    assert expected_elements == elements_present

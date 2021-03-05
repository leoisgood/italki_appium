import pytest
import time
from appium import webdriver

driver = None


@pytest.fixture()
def set_up(android_setting_dict):
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',android_setting_dict)
    return driver


@pytest.fixture()
def tear_down():
    yield driver
    time.sleep(2)
    driver.close_app()

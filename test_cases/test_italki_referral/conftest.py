import pytest
import time
from appium import webdriver

driver = None


# @pytest.fixture(params=[('18217116148@126.com', 'lz123456')])
# def params_setting_list(request):
#     return request.param


@pytest.fixture()
def set_up(android_setting_dict):  # 使用到了外层的fixture
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', android_setting_dict)
    return driver


@pytest.fixture()
def tear_down():
    yield driver
    time.sleep(2)
    # driver.close()
    driver.close_app()

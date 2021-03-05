import pytest
import allure
@allure.epic('计算器项目')
@allure.feature('计算器项目V1.0')
class TestAdd:
    @allure.story('基本运算')
    @allure.title('[case01] 验证计算器能否正常完成加法功能')
    def test_add_case01(self,set_up,tear_down):
        with allure.step('1、启动app中的计算器'):
            driver = set_up
        with allure.step('2、依次按下按键 9、+、8、='):
            driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.sky.jisuanji:id/btn9"]').click()
            driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.sky.jisuanji:id/jia"]').click()
            driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.sky.jisuanji:id/btn8"]').click()
            driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.sky.jisuanji:id/denyu"]').click()
            actual_result = driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.sky.jisuanji:id/text"]').text
        with allure.step('3、验证实际结果是否正确'):
            assert  actual_result == '17.0'
        with allure.step('4、关闭italki'):
            driver = tear_down
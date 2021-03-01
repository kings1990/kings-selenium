from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver as webdriver_phone
from selenium import webdriver as webdriver_web
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import os
import kings_selenium.constants as constants


class SeleniumCommon:
    def __init__(self):
        constants.init()

    def _init__phone(self, app_path):
        """
        初始化app端driver(Appium)
        :param app_path:
        :return:
        """
        app = os.path.abspath(app_path)
        DESIRED_CAPABILITIES = constants.DESIRED_CAPABILITIES
        print(DESIRED_CAPABILITIES)
        DESIRED_CAPABILITIES["app"] = app

        self.driver = webdriver_phone.Remote(
            command_executor=constants.COMMAND_EXECUTOR,
            desired_capabilities=DESIRED_CAPABILITIES)
        return self.driver

    def _init_web(self, is_debug=False, arguments=None):
        """
        web端初始化
        :param is_debug: 是否是调试模式,默认False
        :param arguments: chrome参数
        :return:
        """
        if arguments is None:
            arguments = []
        options = webdriver_web.ChromeOptions()
        if is_debug:
            options.debugger_address = constants.CHROME_DEBUGGER_ADDRESS
        for argument in arguments:
            options.add_argument(argument)
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver_web.Chrome(constants.DRIVER_LOCATION, options=options)
        return self.driver

    def get_driver(self):
        """获取driver"""
        return self.driver

    def _click(self, by=MobileBy.ACCESSIBILITY_ID, by_value=None, timeout=constants.TIMEOUT,
               poll_frequency=constants.POLL_FREQUENCY):
        """
        异步click方法
        :param driver: driver驱动
        :param by: 查询策略
        :param by_value: 查询策略值
        :return:
        """
        try:
            self._wait(timeout, by, by_value=by_value, poll_frequency=poll_frequency)
            ele = self.driver.find_element(by, by_value)
            ele.click()
        except NoSuchElementException:
            print(by, '异常', by_value)
            self.driver.quit()

    def _wait(self, timeout, by, by_value=None, poll_frequency=constants.POLL_FREQUENCY):
        """
        异步等待
        :param timeout: 超时时间
        :param by: 查询策略
        :param by_value: 查询策略值
        :param poll_frequency: 寻轮时间
        :return:
        """
        loc = (by, by_value)
        ec.presence_of_element_located(loc)
        WebDriverWait(self.driver, timeout, poll_frequency, None).until(ec.presence_of_element_located(loc))

    def _send_keys(self, by=MobileBy.ACCESSIBILITY_ID, by_value=None, keys=None):
        """
        根据by输入值
        :param by: 查询策略
        :param by_value: 查询策略值
        :param keys: 输入的值
        :return:
        """
        try:
            self._wait(constants.TIMEOUT, by, by_value=by_value, poll_frequency=constants.POLL_FREQUENCY)
            self.driver.find_element(by, by_value).send_keys(keys)
        except NoSuchElementException:
            print(by, '异常', by_value)
            self.driver.quit()

    def click_by_xpath(self, xpath):
        """
        根据xpath点击
        :param xpath: 目标节点xpath
        :return:
        """
        self._click(By.XPATH, xpath)

    def send_keys_by_xpath(self, xpath, keys):
        """
        根据xpath输入值
        :param xpath: 目标节点xpath
        :param keys: 输入的值
        :return:
        """
        self._send_keys(By.XPATH, by_value=xpath, keys=keys)

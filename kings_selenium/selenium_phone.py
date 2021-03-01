from appium.webdriver.common.mobileby import MobileBy
from .selenium_common import SeleniumCommon


class SeleniumPhone(SeleniumCommon):
    def __init__(self, app_path):
        """
        初始化driver
        :param app_path: app路径
        :return:
        """
        super().__init__()
        super()._init__phone(app_path)

    def set_app(self, app_path):
        """
        初始化driver
        :param app_path: app路径
        :return:
        """
        super()._init__phone(app_path)

    def click(self, by=MobileBy.ACCESSIBILITY_ID, by_value=None):
        """
        点击,默认按照ACCESSIBILITY_ID点击
        :param by: 查询策略
        :param by_value: 查询策略值
        :return:
        """
        super()._click(by, by_value)

    def wait(self, timeout, by=MobileBy.ACCESSIBILITY_ID, by_value=None, poll_frequency=0.5):
        """
        等待直到某个组件可以访问到(异步)
        :param timeout: 超时时间
        :param by: 查询策略
        :param by_value: 查询策略值
        :param poll_frequency: 轮训间隔时间
        :return:
        """
        super()._wait(self.driver, timeout, by, by_value, poll_frequency)

    def click_by_accessibility_id(self, id_):
        """
        根据ACCESSIBILITY_ID点击
        :param id_: ACCESSIBILITY_ID值
        :return:
        """
        self.click(MobileBy.ACCESSIBILITY_ID, id_)

    def send_keys(self, by=MobileBy.ACCESSIBILITY_ID, by_value=None, keys=None):
        """
        根据by输入值(默认根据ACCESSIBILITY_ID)
        :param by: 查询策略
        :param by_value: 查询策略值
        :param keys: 输入的值
        :return:
        """
        super()._send_keys(by, by_value, keys)

    def send_keys_by_accessibility_id(self, id_, keys):
        """
        根据ACCESSIBILITY_ID输入值
        :param id_: 目标节点的ACCESSIBILITY_ID
        :param keys: 输入的值
        :return:
        """
        self.send_keys(MobileBy.ACCESSIBILITY_ID, by_value=id_, keys=keys)

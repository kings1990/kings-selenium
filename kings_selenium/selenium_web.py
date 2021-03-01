from selenium.webdriver.common.by import By
from .selenium_common import SeleniumCommon


class SeleniumWeb(SeleniumCommon):
    def __init__(self, is_debug=False, arguments=None):
        """
        初始化
        :param is_debug: 是否是调试模式
        :param arguments: chrome option参数
        """
        super().__init__()
        super()._init_web(is_debug, arguments)

    def get(self, url):
        """打开url"""
        self.driver.get(url)

    def open_url_debug(self, url):
        """新建tab打开url(调试模式下)"""
        self.driver.execute_script("window.open('" + url + "');")
        self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles) - 1])

    def click(self, by=By.ID, by_value=None):
        """点击,默认按照id点击"""
        super()._click(by, by_value)

    def wait(self, timeout, by=By.ID, by_value=None, poll_frequency=0.5):
        """
        等待直到某个组件可以访问到(异步)
        :param timeout: 超时时间
        :param by: 查询策略
        :param by_value: 查询策略值
        :param poll_frequency: 轮训间隔时间
        :return:
        """
        super()._wait(self.driver, timeout, by, by_value, poll_frequency)

    def click_by_id(self, id_):
        """根据id点击"""
        self.click(By.ID, id_)

    def send_keys(self, by=By.ID, by_value=None, keys=None):
        """
        根据by输入值(默认根据ID)
        :param by: 查询策略
        :param by_value: 查询策略值
        :param keys: 输入的值
        :return:
        """
        super()._send_keys(by, by_value, keys)

    def send_keys_by_id(self, id_, keys):
        """
        根据ID输入值
        :param id_: 根据id输入值,默认根据ID
        :param keys: 输入的值
        :return:
        """
        self.send_keys(by_value=id_, keys=keys)

    def send_keys_by_css_selector(self, css, keys):
        """
        根据CSS选择器输入值
        :param css: 目标节点的css
        :param keys: 输入的值
        :return:
        """
        self.send_keys(By.CSS_SELECTOR, by_value=css, keys=keys)

    def execute_script(self, js, *args):
        """
        执行js
        :param js: js函数
        :param args: 参数
        :return:
        """
        self.driver.execute_script(js, args)

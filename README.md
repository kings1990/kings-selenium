# kings_selenium
基于chrome的使用selenium将web端和appium常用方法封装集成成一个简单的类,其中节点查询和点击都是基于异步的,不需要再在程序中使用time.sleep(x)

# 安装
pip install kings_selenium

# 配置 config.json
配置文件,路径为当前项目的根目录创建一个config文件夹,里面再创建config.json

## 公共
> POLL_FREQUENCY  
异步查询节点轮循时间,单位秒,默认0.5

> TIMEOUT  
节点查询超时时间

## web端
> CHROME_DEBUGGER_ADDRESS  
谷歌浏览器调试地址，默认,使用此参数需要先启动谷歌浏览器调试模式
127.0.0.1:9222

> DRIVER_LOCATION  
chrome driver驱动路径,使用web时必填

## appium
> COMMAND_EXECUTOR
appium启动调试地址，默认
http://127.0.0.1:4723/wd/hub

> DESIRED_CAPABILITIES
```
appium启动联调参数,使用appium时必填,如
"DESIRED_CAPABILITIES": {
    "platformName": "iOS",
    "platformVersion": "14.0",
    "deviceName": "Kings",
    "udid": "xxx",
    "appPushTimeout": 300000,
    "noReset": "True",
    "webkitgtk:browserOptions": {
      "excludeSwitches": [
        "enable-automation"
      ],
      "args": [
        "--incognito",
        "--headless",
        "--disable-infobars",
        "--disable-javascript"
      ]
    }
  }
```

# 使用
```web端
from kings_selenium.selenium_web import SeleniumWeb

seleniumWeb = SeleniumWeb(True)
seleniumWeb.open_url_debug("https://www.baidu.com")
seleniumWeb.send_keys_by_id("kw", "hello")
seleniumWeb.click_by_id("su")

```

```
app端
from kings_selenium.selenium_phone import SeleniumPhone

"""模拟京东app点击我的"""
seleniumPhone = SeleniumPhone('/Users/wilson/Desktop/jd.ipa')
seleniumPhone.click_by_xpath('//XCUIElementTypeStaticText[@name="我的"]')
```
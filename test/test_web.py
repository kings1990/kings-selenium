from kings_selenium.selenium_web import SeleniumWeb

seleniumWeb = SeleniumWeb(True)
seleniumWeb.open_url_debug("https://www.baidu.com")
seleniumWeb.send_keys_by_id("kw", "hello")
seleniumWeb.click_by_id("su")

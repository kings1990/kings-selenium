from kings_selenium.selenium_phone import SeleniumPhone

"""模拟京东app点击我的"""
seleniumPhone = SeleniumPhone('/Users/wilson/Desktop/jd.ipa')
seleniumPhone.click_by_xpath('//XCUIElementTypeStaticText[@name="我的"]')

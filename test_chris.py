import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.amazon.com")
browser.find_element_by_id("twotabsearchtextbox").send_keys("Macbook")
# time.sleep(3)
# browser.find_element_by_id("twotabsearchtextbox").send_keys(Keys.ARROW_DOWN * 3 + Keys.ENTER)
dropdown = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath("//input[#'twotabsearchtextbox']"))
dropdown.send_keys(Keys.ARROW_DOWN * 3 + Keys.ENTER)
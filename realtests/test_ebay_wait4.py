from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.ebay.com")

browser.find_element_by_id("gh-ac").send_keys("Mustang")
my_element = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath("//a[@aria-label='mustang convertible']"))
my_element.click()


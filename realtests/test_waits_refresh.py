from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.ebay.com")
assert browser.title == expected_title

browser.find_element_by_id("gh-ac").send_keys("Dodge")
# name_of_your_element = WebDriverWait(browser,5).until(lambda x: x.find_element_by_xpath("xpath"))
# name_of_your_element.click()
name_of_your_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"xpath")))

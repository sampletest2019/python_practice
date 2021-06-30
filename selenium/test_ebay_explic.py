from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
expected_search_title = "dodge viper | eBay"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.ebay.com/")
assert browser.title == expected_title

browser.find_element_by_id("gh-ac").send_keys("Dodge")

# dropdown_option = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath("//li[3]/a[@role='option']"))
dropdown_option = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/a[@role='option']")))
dropdown_option.click()

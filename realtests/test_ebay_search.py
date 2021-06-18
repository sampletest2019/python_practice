from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
expected_search_title = "dodge viper | eBay"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.ebay.com/")
assert browser.title == expected_title

browser.find_element_by_id("gh-ac").send_keys("Dodge Viper" + Keys.ENTER)
assert browser.title == expected_search_title

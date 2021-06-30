from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(5)
browser.get("https://www.ebay.com")
assert browser.title == expected_title

browser.find_element_by_id("gh-ac").send_keys("Dodge")
browser.find_element_by_xpath("//a[@aria-label='dodge ram 2500']").click()

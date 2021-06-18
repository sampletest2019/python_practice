from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.ebay.com/")
assert browser.title == expected_title


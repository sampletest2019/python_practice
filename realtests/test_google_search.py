from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Google"
search_page_title = "Dodge Viper - Google Search"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com/")
assert browser.title == expected_title

browser.find_element_by_name("q").send_keys("Dodge Viper" + Keys.ENTER)
assert browser.title == search_page_title

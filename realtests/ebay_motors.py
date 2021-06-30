from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"
expected_search_title = "dodge viper | eBay"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.ebay.com/")
assert browser.title == expected_title

browser.find_element_by_link_text("Motors").click()

make_dropdown = WebDriverWait(browser, 5).until(lambda y: y.find_element_by_xpath("//select[@name='Make'][@aria-label='All Makes']"))
make_dropdown.click()

make_dropdown_value = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath("//select//option[@value='Aston Martin']"))
make_dropdown_value.click()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com")
browser.find_element_by_name("q").send_keys("learnix" + Keys.ENTER)

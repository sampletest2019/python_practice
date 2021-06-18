from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Google"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com/")
assert browser.title == expected_title

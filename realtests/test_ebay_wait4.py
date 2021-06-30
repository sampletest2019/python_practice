from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.ebay.com")

browser.find_element_by_id("gh-ac").send_keys("Mustang")


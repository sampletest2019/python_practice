from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.ebay.com")

browser.find_element_by_id("gh-ac").send_keys("Mustang")
your_element_will_be_here = WebDriverWait(browser, 4).until(
    EC.presence_of_element_located((By.XPATH, "//a[@aria-label='mustang cobra']")))
your_element_will_be_here.click()

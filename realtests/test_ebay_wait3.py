"""sometimes you don't need to write code over and over again.
you can write custom function to find, wait for and to click on specific element"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.ebay.com")


# you can create custom function to wait for specific amount of time and click on specific element by xpath
# and you can reuse it see below
def wait_for_element_and_click(browser, timeout, xpath):
    el = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
    el.click()


browser.find_element_by_id("gh-ac").send_keys("Mustang")
# here you can call you custom function passing browser, 10 seconds and xpath of your element
wait_for_element_and_click(browser, 10, "//a[@aria-label='mustang cobra']")

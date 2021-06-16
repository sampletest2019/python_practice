from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://the-internet.herokuapp.com/")
browser.get("https://formy-project.herokuapp.com/")
browser.back()
browser.refresh()
browser.forward()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://the-internet.herokuapp.com/windows")
browser.find_element_by_link_text("Click Here").click()
windows = browser.window_handles
print(browser.window_handles)
browser.switch_to.window(windows[0])



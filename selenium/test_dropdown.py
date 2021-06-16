from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://the-internet.herokuapp.com/")
browser.find_element_by_link_text("Dropdown").click()

#create a new object which is the instance of Select class
# specify how to find this element on the screen (by id)
dropdown = Select(browser.find_element_by_id("dropdown"))

# you can access all methods of this object
# you can select by text
dropdown.select_by_visible_text("Option 1")
# by index (number) from 0
dropdown.select_by_index(2)
# by value (if value attribute exists)
dropdown.select_by_value("1")


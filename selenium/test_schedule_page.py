from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://homepro.herokuapp.com/index.php")
assert browser.current_url == "https://homepro.herokuapp.com/index.php"
assert browser.title == "HomePro, Inc"
browser.find_element_by_link_text("Schedule an Appointment").click()

jobtype_dropdown = Select(browser.find_element_by_name("job_type"))
jobtype_dropdown.select_by_index(1)

browser.find_element_by_name("first_name").send_keys("Masuma")
browser.find_element_by_name("last_name").send_keys("Masuma")
browser.find_element_by_name("phone").send_keys("703-123-4455")
browser.find_element_by_name("email").send_keys("masuma.qa2021@gmail.com")

browser.find_element_by_xpath("//input[@value='Schedule My consultation']").click()
assert browser.current_url == "https://homepro.herokuapp.com/orderconfirm.php"


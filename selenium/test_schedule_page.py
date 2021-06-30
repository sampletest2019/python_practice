from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


# create variables for home pro home page url, confirmation page url and home page title
base_url = "https://homepro.herokuapp.com/index.php"
confirmation_page = "https://homepro.herokuapp.com/orderconfirm.php"
home_page_title = "HomePro, Inc"

# created customer dictionary to pass data like first name, email to my test below
customer = {
    "jop type index": 2,
    "first name": "Vila",
    "last name": "Vila",
    "phone": "202-554-3123",
    "email": "automation.vila.qa2021@gmail.com"
}

# create an instance of Chrome
browser = webdriver.Chrome(ChromeDriverManager().install())

# create function to find an element by name which we will provide
# and enter the text into this text field which we will provide
def find_element_enter_text(name, text):
    browser.find_element_by_name(name).send_keys(text)



# navigate to home pro base url (home page) see above
browser.get(base_url)
# validate that current url is matching with our expected url (home page url)
assert browser.current_url == base_url
#validate current page title is matching with our expected title (home page title)
assert browser.title == home_page_title
# find Schedule button by link text and click on it
browser.find_element_by_link_text("Schedule an Appointment").click()

# create a new instance of Select class and find an element by name (dropdown)
jobtype_dropdown = Select(browser.find_element_by_name("job_type"))
# now we will select job type from the dropdown by index (0, 1, 2 etc)
jobtype_dropdown.select_by_index(customer["jop type index"])

# we used our newly created function to find different elements
# by name and enter different text
find_element_enter_text("first_name", customer["first name"])
find_element_enter_text("last_name", customer["last name"])
find_element_enter_text("phone", customer["phone"])
find_element_enter_text("email", customer["email"])
# browser.find_element_by_name("first_name").send_keys(customer["first name"])
# browser.find_element_by_name("last_name").send_keys(customer["last name"])
# browser.find_element_by_name("phone").send_keys(customer["phone"])
# browser.find_element_by_name("email").send_keys(customer["email"])

# find a button by xpath and click on it
# browser.find_element_by_xpath("//input[@value='Schedule My consultation']").click()
# # validate that user landed on the confirmation page by checking that url matches expected url (confirmation page)
# assert browser.current_url == confirmation_page


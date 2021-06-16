from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://homepro.herokuapp.com/quote.php")
browser.find_element_by_xpath("//input[@value='Send']").click()

my_alert = browser.switch_to.alert
print(my_alert.text)
my_alert.accept()
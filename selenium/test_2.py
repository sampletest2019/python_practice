from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://homepro.herokuapp.com/quote.php")
browser.find_element_by_name("first_name").send_keys("Victoria")
browser.find_element_by_name("email").send_keys("victoria.qa2021@gmail.com")
browser.find_element_by_name("phone").send_keys("202-222-2222")
browser.find_element_by_name("comments").send_keys("I need a quote today!")
browser.find_element_by_name("subscription").click()

#it's impossible to use "" inside "". you need to use single ' ' inside double " "
browser.find_element_by_xpath("//input[@value='Send']").click()
assert browser.current_url == "https://homepro.herokuapp.com/quoteconfirm.php"
browser.quit()







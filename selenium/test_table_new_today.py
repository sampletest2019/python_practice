from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://the-internet.herokuapp.com/tables")
# create a variable, find your table by id and put it into your table_1 variable
table_1 = browser.find_element_by_id("table1")

# find ALL rows inside your table by tag "tr" (table row). you will get a LIST
all_rows = table_1.find_elements_by_tag_name("tr")

# find all COLUMNS (cells) from row with the index 1 by using tag "td" (table data)
cells_from_row1 = all_rows[1].find_elements_by_tag_name("td")
# print first (with index 0) column text
print(cells_from_row1[0].text)

# find all COLUMNS (cells) from row with index 3 by using tag "td" (table data)
cells_from_row3 = all_rows[3].find_elements_by_tag_name("td")
# print column 1 (index 0) text
print(cells_from_row3[0].text)
# print column 2 index 1 text
print(cells_from_row3[1].text)

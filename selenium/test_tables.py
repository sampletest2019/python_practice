from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://the-internet.herokuapp.com/tables")

table1 = browser.find_element_by_id("table1")
all_rows = table1.find_elements_by_tag_name("tr")
# for row in all_rows:
#     print(row.text)

# row_1 = all_rows[1]
# print(row_1.text)
#
# all_cells = row_1.find_elements_by_tag_name("td")
# print(all_cells[0].text)


# specific row using xpath

row_1 = browser.find_element_by_xpath("//table[@id='table1']/tbody/tr[1]")
print(row_1.text)
cells_all = row_1.find_elements_by_tag_name("td")
for cell in cells_all:
    print(cell.text)

cell_0 = row_1.find_element_by_xpath("//td[0]")
print(cell_0)
browser.quit()
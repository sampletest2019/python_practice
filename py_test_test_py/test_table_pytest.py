"""
Fixture scopes
Fixtures are created when first requested by a test, and are destroyed based on their scope:

function: the default scope, the fixture is destroyed at the end of the test.

class: the fixture is destroyed during teardown of the last test in the class.

module: the fixture is destroyed during teardown of the last test in the module.

package: the fixture is destroyed during teardown of the last test in the package.

session: the fixture is destroyed at the end of the test session.
"""


import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.mark.smoketest2
def test_navigate(browser):
    browser.get("https://the-internet.herokuapp.com")

@pytest.mark.smoketest2
def test_verify_table(browser):
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

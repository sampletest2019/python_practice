import pytest
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize("item", [
    "macbook pro",
    "microsoft surface",
    "razer gaming laptop"
])
@pytest.mark.regressiontest
def test_validate_search(browser, item):
    browser.get("https://www.amazon.com")
    assert browser.title == "Amazon.com. Spend less. Smile more."
    browser.find_element_by_id("twotabsearchtextbox").send_keys(item + Keys.ENTER)
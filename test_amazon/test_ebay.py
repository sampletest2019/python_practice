import pytest


@pytest.mark.smoketest2102
def test_validate_title(browser):
    browser.get("https://www.ebay.com")
    assert browser.title == "Electronics, Cars, Fashion, Collectibles & More | eBay"
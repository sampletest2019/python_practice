import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    yield browser

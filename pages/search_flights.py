from webbrowser import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
#@pytest.mark.usefixtures('browser')
@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = Chrome()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)
    # Return the driver object at the end of setup
    #cookie = {'name': 'foo', 'value': 'bar'}
    #driver.add_cookie(cookie)
    # And now output all the available cookies for the current URL
    #driver.get_cookies()
    yield driver
    # For cleanup, quit the driver
    driver.quit()
def test_duckduckgo_search(browser):
    # Set up some test case data

    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'
    # Navigate to the DuckDuckGo home page
    browser.get(URL)
    # Find the search input element
    # In the DOM, it has an 'id' attribute of 'search_form_input_homepage'
    search_input = browser.find_element(By.ID, "searchbox_input")
    # Send a search phrase to the input and hit the RETURN /ENTER key
    search_input.send_keys(PHRASE + Keys.RETURN)
    # Verify that results appear on the results page
    link_divs = browser.find_elements(By.CSS_SELECTOR, '#links > div')
    assert len(link_divs) > 0
    # Verify that at least one search result contains the search phrase
    xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
    phrase_results = browser.find_elements(By.XPATH, xpath)
    assert len(phrase_results) > 0
    # Verify that the search phrase is the same
    search_input = browser.find_element(By.ID, 'search_form_input')
    assert search_input.get_attribute('value') == PHRASE

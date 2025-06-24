import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose browser language")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name == 'chrome':
        options = Options()
        if language:
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        pytest.skip("Only Chrome is supported")

    yield browser
    browser.quit()

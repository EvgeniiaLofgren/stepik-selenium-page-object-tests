import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
        page.open()
        page.go_to_login_page()
        login = LoginPage(browser, browser.current_url)
        login.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
        page.open()
        page.should_be_login_link()

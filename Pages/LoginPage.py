from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.HomePage import HomePage


class LoginPage(BasePage):

    """By locators - OR"""
    EMAIl = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.ID, "Sign up")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions for Login Page"""

    """Used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """Used to check sign up link"""
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """Used to login to AUT"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIl, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

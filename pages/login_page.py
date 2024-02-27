from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'str "login" not in current url'

    def should_be_login_form(self):
        assert (self.is_element_present(*LoginPageLocators.LOGIN_INPUT) and
                self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD) and
                self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)) is True, 'Login form is not presented'

    def should_be_register_form(self):
        assert (self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON) and
                self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL) and
                self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD) and
                self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)) is True, 'Registration form is not presented'

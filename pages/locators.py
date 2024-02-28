from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form .btn')
    BASKET_SUMMARY = (By.CSS_SELECTOR, '.basket-mini')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] h1')
    BASKET_ADD_CONFIRM_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    PRODUCT_MAIN_PRICE = (By.CSS_SELECTOR, '.col-sm-6 [class="price_color"]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
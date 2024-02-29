import pytest
import time
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, url=link)
    page.open()
    page.should_be_product_promo_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_basket_confirm_message_equal_to_product_name()
    page.should_basket_summary_equal_to_product_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url=product_base_link)
    page.open()
    page.add_to_basket()
    page.should_basket_confirm_is_not_present()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url=product_base_link)
    page.open()
    page.should_basket_confirm_is_not_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url=product_base_link)
    page.open()
    page.add_to_basket()
    page.should_basket_confirm_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page (browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, product_base_link)
    page.basket_totals_is_disappeared()
    page.empty_basket_text_is_disappeared()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        self.page=LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user((str(time.time()) + "@fakemail.org"),'Password6EQUJ5')
        self.page=BasePage(browser, link)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, url=product_base_link)
        page.open()
        page.should_basket_confirm_is_not_present()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, url=product_base_link)
        page.open()
        page.add_to_basket()
        page.should_basket_confirm_message_equal_to_product_name()
        page.should_basket_summary_equal_to_product_price()


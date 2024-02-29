from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.locators import BasePageLocators
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators
import pytest
import time


link = 'http://selenium1py.pythonanywhere.com/'
@pytest.mark.skip
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.basket_totals_is_disappeared()
    page.empty_basket_text_is_disappeared()


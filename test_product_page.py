import pytest
from .pages.product_page import ProductPage
import time
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls)
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, url=link)
    page.open()
    page.should_be_product_promo_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_basket_confirm_message_equal_to_product_name()
    page.should_basket_summary_equal_to_product_price()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url=product_base_link)
    page.open()
    page.add_to_basket()
    page.should_basket_confirm_is_not_present()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url=product_base_link)
    page.open()
    page.should_basket_confirm_is_not_present()

@pytest.mark.skip
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

def test_guest_should_see_login_link_from_product_page(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_be_login_link()


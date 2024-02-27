from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, url='http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear')
    page.open()
    page.should_be_product_promo_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_basket_confirm_message_equal_to_product_name()
    page.should_basket_summary_equal_to_product_price()



from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_promo_page(self):
        self.should_be_promo()
        self.should_be_basket_button()
        self.should_be_basket_summary()
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON) is True , 'Basket button is not presented'

    def should_be_basket_summary(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_SUMMARY) is True , 'Basket_summary is not presented'

    def should_be_promo(self):
        assert 'promo' in self.browser.current_url, 'This link is not promo'

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def should_basket_confirm_message_equal_to_product_name(self):
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text ==
                self.browser.find_element(*ProductPageLocators.BASKET_ADD_CONFIRM_MESSAGE).text), \
                'The product name in the confirmation message does not match the actual one'

    def should_basket_summary_equal_to_product_price(self):
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT_MAIN_PRICE).text in
                self.browser.find_element(*ProductPageLocators.BASKET_SUMMARY).text), \
                'Basket summary does not equal to the product price'

    def should_basket_confirm_is_not_present(self):
        assert BasePage.is_not_element_present(self, *ProductPageLocators.BASKET_ADD_CONFIRM_MESSAGE), \
            'Success message is presented, but should not be'

    def should_basket_confirm_is_disappeared(self):
        assert BasePage.is_disappeared(self, *ProductPageLocators.BASKET_ADD_CONFIRM_MESSAGE), \
            'Success message is presented, but should not be'

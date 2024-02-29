from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_basket_text_is_disappeared(self):
        assert (self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT).get_attribute('href')
                in self.browser.current_url), 'Basket is not empty'

    def basket_totals_is_disappeared(self):
        assert BasePage.is_disappeared(self, *BasketPageLocators.BASKET_TOTALS), ('Basket totals is presented,'
                                                                            ' but should not be')



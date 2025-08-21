from selenium.webdriver.common.by import By

from pageObject.check_out_and_confirmation import Checkout_Confirmation


class ShopPage:

    def __init__(self,driver):
        self.driver = driver
        self.shop_link =(By.XPATH, "//a[@href='/angularpractice/shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.check_out_button = (By.CSS_SELECTOR, "a[class*='btn btn-primary']")


    def add_product_to_cart(self,productName):

        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == productName:
                product.find_element(By.XPATH, "div/button").click()

    def goToCart(self):
        self.driver.find_element(*self.check_out_button).click()
        checkout_confirmation = Checkout_Confirmation(self,driver)
        return checkout_confirmation

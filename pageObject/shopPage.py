from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self,driver):
        self.driver = driver
        self.shop_link =(By.XPATH, "//a[@href='/angularpractice/shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")


    def add_product_to_cart(self,productName):

        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == productName:
                product.find_element(By.XPATH, "div/button").click()

    def goToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn btn-primary']").click()

class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver


    def getTitle(self, driver):
        return self.driver.title




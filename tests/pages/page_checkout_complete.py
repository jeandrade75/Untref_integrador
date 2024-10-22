from selenium.webdriver.common.by import By


class Page_Checkout_Complete:
    def __init__(self, driver):
        self.driver = driver
        self.final_message = (By.CLASS_NAME,'complete-header')

    def get_final_message(self):
        return self.driver.find_element(*self.final_message).text
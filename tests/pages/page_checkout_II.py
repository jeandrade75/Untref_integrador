from selenium.webdriver.common.by import By

class Page_Checkout_II:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_item = (By.CLASS_NAME,'inventory_item_name')
        self.finish_button = (By.ID,'finish')
    
    def verify_element(self, i):
        return self.driver.find_elements(*self.inventory_item)[i].text
    
    def finish(self):
        self.driver.find_element(*self.finish_button).click()
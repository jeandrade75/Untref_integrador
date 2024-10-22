class Page_Checkout():
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID,'first-name')
        self.last_name = (By.ID,'last-name')
        self.postal_code = (By.ID,'postal-code')
        self.continue_button = (By.ID,'continue')
    
    def checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class SauceDemoTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login("standard_user", "secret_sauce")
    
    def login(self, username, password):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
    
    def test_case_1(self):
        """Caso 1: Ordenar los productos por precio (bajo a alto) y verificar el orden"""
        driver = self.driver
        select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("lohi")  # Ordenar de bajo a alto
        
        # Obtener los precios de los productos
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices_values = [float(price.text.replace("$", "")) for price in prices]
        
        # Verificar que estén en orden
        self.assertEqual(prices_values, sorted(prices_values), "Los productos no están ordenados correctamente por precio.")

    def test_case_2(self):
        """Caso 2: Agregar todos los productos al carrito y verificar errores en el checkout"""
        driver = self.driver
        add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        
        # Agregar todos los elementos al carrito
        for button in add_buttons:
            button.click()
        
        # Ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        # Verificar que todos los productos están en el carrito
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(cart_items), len(add_buttons), "No todos los productos están en el carrito.")

        # Ir al checkout
        driver.find_element(By.ID, "checkout").click()
        
        # Ingresar nombre y continuar
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "continue").click()
        
        # Verificar error de apellido requerido
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Error: Last Name is required", error_message)

        # Ingresar apellido y continuar
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "continue").click()

        # Verificar error de código postal requerido
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Error: Postal Code is required", error_message)

    def test_case_3(self):
        """Caso 3: Agregar y remover productos, luego completar la compra"""
        driver = self.driver
        # Agregar un producto al carrito
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # Remover el producto
        driver.find_element(By.CLASS_NAME, "cart_button").click()
        
        # Verificar que no hay productos en el carrito
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(cart_items), 0, "El carrito no está vacío.")

        # Continuar comprando y agregar dos productos
        driver.find_element(By.ID, "continue-shopping").click()
        add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        add_buttons[0].click()
        add_buttons[1].click()

        # Verificar que los productos están en el carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(cart_items), 2, "Los productos no están en el carrito.")
        
        # Completar el checkout
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()

        # Verificar que la compra se ha completado
        confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
        self.assertIn("thank you for your order".lower(), confirmation_message.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


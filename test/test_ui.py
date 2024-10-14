import unittest
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options

from pages.page_login import Page_Login
from pages.page_inventory import Page_Inventory
from pages.page_cart import Page_Cart
from pages.page_checkout import Page_Checkout
from pages.page_checkout_II import Page_Checkout_II
from pages.page_checkout_complete import Page_Checkout_Complete
class Compras(unittest.TestCase):
    pass
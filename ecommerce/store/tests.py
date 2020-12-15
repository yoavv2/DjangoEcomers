from selenium import webdriver

import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from ecommerce.store.models import *

def test_exemple_using_chrome():
    driver = webdriver.Chrome()

    driver.get('http://127.0.0.1:8000/checkout/')

    driver.find_element_by_id('name').send_keys('john smith')

    driver.quit()

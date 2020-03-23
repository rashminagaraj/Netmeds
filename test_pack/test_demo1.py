"""
This code explains mark usage

"""

from time import sleep

import pytest
from selenium.webdriver.common.keys import Keys

from generics.genmethods import read_json_val
from _pytest.nodes import Item
from pages.homepage import *
from pages.catalogsearch import add_items_to_cart


def test_launch_browser(driver):
    print ("launching app") 
    print (driver.title)
    search_products(driver) 
    sleep(4)
    validate_products_displayed(driver)
    initial_count=get_countof_items_added(driver)
    add_items_to_cart(driver)
    sleep(2)
    final_count=get_countof_items_added(driver)
    assert (initial_count+1)==final_count
    print("Successfully executed")
     

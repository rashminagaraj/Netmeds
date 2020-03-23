"""
Conftest file is like supermost class/module accessible to all modules in project.
Here we write fixtures,hooks.

It is similar to environment.py file in behave
"""
"""
This code explains fixtures.
Using request.config.option we can read command prompt inputs

"""

from time import sleep

import pytest
from selenium import webdriver


# @pytest.fixture(scope='session')
# def driver(request):
#     driver=webdriver.Chrome()
#     driver.get("https://www.netmeds.com/")
#     sleep(4)
#
#     def teardown():
#         driver.close()
#     request.addfinalizer(teardown)
#     yield driver
@pytest.yield_fixture(scope="session")
def driver(request):
    driver=webdriver.Chrome()
    driver.get("https://www.netmeds.com/")
    driver.maximize_window()
    yield driver
    sleep(4)
    driver.close()

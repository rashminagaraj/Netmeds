from selenium.webdriver.common.keys import Keys

from generics.genmethods import read_json_val

def search_products(driver):
    product=driver.find_element_by_id(read_json_val("homepage","id","searchbutton"))
    product.send_keys(read_json_val("testdata","product_name","med1"))
    product.send_keys(Keys.ENTER)
    
def validate_products_displayed(driver):
    items=driver.find_elements_by_xpath(read_json_val("homepage","xpath","product"))
    assert len(items) != 0
    
def get_countof_items_added(driver):
    val=driver.find_element_by_xpath(read_json_val("homepage","xpath","itemcount")).text
    return int(val)




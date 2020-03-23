from generics.genmethods import read_json_val


def add_items_to_cart(driver):
    driver.find_element_by_xpath(read_json_val("catalogsearch","xpath","addtocart")).click()
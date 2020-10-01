import os
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = os.path.join(dir_path, "chromedriver")
os.environ["webdriver.chrome.driver"] = chromedriver


def main():
    driver = webdriver.Chrome(chromedriver)
    wait = WebDriverWait(driver, 10)

    driver.get('http://localhost:9001')
    print('open landing page')
    start_button = driver.find_element_by_id('cta-button')
    time.sleep(3)
    start_button.click()
    print('clicked on cta-button button move to property search page')

    keyword = '1529 W TAYLOR ST, CHICAGO, IL'
    search_box = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))
    search_box.send_keys(keyword)
    time.sleep(3)
    print('search by keyword: %s' % keyword)
    search_box_value = search_box.get_attribute('value')

    li = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'li')))
    time.sleep(3)

    select_button = driver.find_element_by_id('select_button')
    select_button.click()
    time.sleep(3)
    print('clicked on select_button button')

    driver.get('http://localhost:9001/property-selected')
    print('open property-selected table')
    time.sleep(3)

    cells = driver.find_elements_by_class_name('cell')
    print('search: %s', search_box_value)
    # print([cell.text for cell in cells])
    assert any(cell.text == search_box_value for cell in cells)

    trash_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'el-button--danger')))
    trash_button.click()
    print('delete selected property from table')
    time.sleep(3)

    # print([cell.text for cell in cells])
    cells = driver.find_elements_by_class_name('cell')
    assert all(cell.text != search_box_value for cell in cells)

    driver.close()

    print('e2e Test Pass')


if __name__ == '__main__':
    main()

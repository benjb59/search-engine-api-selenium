from selenium import webdriver
from urllib.parse import unquote

def price(product):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(unquote(product))
    try:
        price = driver.find_element_by_id("priceblock_ourprice").text
    finally:
        driver.quit()
    return price
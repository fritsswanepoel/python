
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

url = 'https://groceries.aldi.co.uk/en-GB/chilled-food'

driver = webdriver.Chrome()



driver.get(url)

#Cookies
cookie_xpath = '/html/body/div[8]/div[3]/div/div/div[2]/div/button'
cookie = driver.find_element(By.XPATH, cookie_xpath)
cookie.click()

confirm_xpath = '/html/body/div[8]/div[2]/div[3]/div[1]/button'
confirm = driver.find_element(By.XPATH, confirm_xpath)
confirm.click()


product_list = []
next_product = True
while next_product:
    #Products
    page_products_xpath = '//*[@id="vueSearchResults"]/div/div'
    page_products = driver.find_elements(By.XPATH, page_products_xpath)
    for product in page_products:
        html = product.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        product_link = soup.find('a', attrs={'class':  "product-tile-media"})
        product_url = product_link['href']
        product_size = soup.find('div', attrs={'class': 'text-gray-small'})
        product_description = soup.find('div', attrs={'class': 'product-tile-text text-center px-3 mb-3'})
        product_price = soup.find('span', attrs={'class': "h4"})
        product_price_proportion = soup.find('small', attrs={'class': "mr-1 text-gray-small"})
        product_list.append({"size":product_size.text,
                            "description":product_description.text.strip(),
                            "price":product_price.text,
                            "proportion":product_price_proportion.text,
                            "url":product_url})
    #Next page
    next_page_xpath = '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div[3]/div/ul/li[4]'
    next_page = driver.find_element(By.XPATH, next_page_xpath)
    if next_page.get_attribute('class') != 'page-item next ml-2 disabled':
        next_page_xpath = '/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/div[3]/div/ul/li[4]/a'
        next_page = driver.find_element(By.XPATH, next_page_xpath)
        next_page.click()
        time.sleep(2)
    else:
        next_product = False




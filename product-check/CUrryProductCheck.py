from urllib.request import urlopen
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://store-locations.co.uk/currys/index.html'
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

#URL
product_url = "https://www.currys.co.uk/gbuk/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/samsung-galaxy-s10-sim-free-128-gb-prism-white-10190352-pdt.html"

#XPATHS
cookie_xpath = '//*[@id="onetrust-pc-btn-handler"]'
reject_xpath = '/html/body/div[8]/div[2]/div[2]/section/div[6]/button[1]'

#Function
#Get counter for input locations
def get_input_counter():
    counter = 0
    locations = driver.find_elements_by_tag_name('input')
    for l in locations:
        if l.get_attribute('placeholder') == 'Enter town or postcode' and l.is_displayed() and l.is_enabled(): 
            break
        counter += 1
    return counter

#Search for location
def search_location(location, counter):
    #Search
    locations = driver.find_elements_by_tag_name('input')
    locations[counter].send_keys(location, Keys.ENTER)
    time.sleep(2)
    #Menu
    menus = driver.find_elements_by_tag_name('menu')
    counter = 0
    for m in menus:
        if m.get_attribute('data-anonid') == 'suggestionlist' and m.is_displayed() and m.is_enabled(): 
            break
        counter+=1
    if counter < len(menus):
        menus[counter].find_element_by_tag_name('li').click()
        return True
    else:
        search_location('leeds',counter)
        return False

#Select a new location
def new_location():
    counter = 0
    changes = driver.find_elements_by_tag_name('a')
    for c in changes:
        if c.get_attribute('textContent') == 'Change location' and c.is_displayed() and c.is_enabled():
            break
        counter += 1
    changes[counter].click()

############
#Store list
store_list = []

for store in soup('a'):
    store_list.append(store.text)

store_list = store_list[1:-3]
store_list = list(set(store_list))
store_list.sort()

# Using Chrome to access web
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(product_url)
driver.implicitly_wait(1)
time.sleep(2)

#Cookies
cookie = driver.find_element(By.XPATH, cookie_xpath)
cookie.click()

driver.implicitly_wait(1)
time.sleep(2)

reject = driver.find_element_by_class_name('ot-pc-refuse-all-handler')
reject.click()

driver.implicitly_wait(1)
time.sleep(2)

#Start with a search
input_counter = get_input_counter()
search_location('Leeds', input_counter)

driver.implicitly_wait(1)
time.sleep(2)
results = []

place = 0

for l in store_list:
    print(l)
    if place > 0:
        new_location()
        driver.implicitly_wait(1)
        time.sleep(2)
        input_counter = get_input_counter()
        searched = search_location(l, input_counter)
        driver.implicitly_wait(1)
        time.sleep(2)
        if searched:
            available = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[2]/section/div[3]/div[2]/div[5]/div/div[2]/div[1]/div[1]/span')
            results.append(available.get_attribute('textContent') + ':'+ l)
    if l == "Staffordshire":
        place+=1





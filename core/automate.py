import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service

skip_count = 47

options = ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--disable-gpu')


# Set up the Selenium driver
driver = webdriver.Chrome(options=options)

connection_message = "Greetings {}, I am Suyash Singh, a final year student and I am interested in exploring full-time employment opportunities at {}. If there are no current openings, I would appreciate it if you could keep me in mind for future opportunities, could we connect so I can share my resume."


def login(address):
    driver.get('https://oxt.me/')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search-inp')))
    search_field = driver.find_element(By.ID, 'search-inp')
    for i in address:
        search_field.send_keys(i)
    search_field.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'title-icon')))
    tools_field = driver.find_element(By.CLASS_NAME, 'site-toolbox')
    node_link = tools_field.find_element(By.TAG_NAME, 'a').get_attribute('href')

address = 'aa8d7407f88dca9b1779880c3d2e3245e02217f7366972d617f812c8dd73a96a'
login(address)

# Close the browser
driver.quit()
'''
Created on 

@author: Chaaya

source:
   
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from webdriver_manager.chrome import ChromeDriverManager
import requests
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

# options.add_argument('--headless')

load_dotenv()

IMAGE_FOLDER    = os.getenv("IMAGE_FOLDER")

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

def startpy():

    celebrity = "jenna"

    driver.get("https://images.google.com/")
    search = driver.find_element(By.XPATH, "//input[@name='q']")
    search.send_keys(celebrity)
    search.send_keys(Keys.RETURN)

    img_tags = driver.find_elements(By.XPATH, '//*[@class=" bRMDJf islir"]/img')

    try:
        os.mkdir(os.path.join(IMAGE_FOLDER, celebrity))
    except Exception as e:
        print(e)

    for i in range(10):
        img_tags[i].click()
        time.sleep(6)
        # try:
        #     img = driver.find_element(By.XPATH, '//img[@class="n3VNCb KAlRDb"]')
        # except:
        img = driver.find_element(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
        img_link = img.get_attribute('src')
        print(img_link)

        with open(f'{IMAGE_FOLDER}/{celebrity}/{celebrity}_{i}.jpeg','wb') as img_file:
            im = requests.get(img_link)
            img_file.write(im.content)
            print('writing: ', f'{celebrity}_{i}.jpeg')


if __name__ == '__main__':
    startpy()

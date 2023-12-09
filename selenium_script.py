from selenium import webdriver
from selenium.webdriver.common.by import By
import time


service = webdriver.ChromeService(executable_path='C:\\CODES\\PYTHON\\Django\\flighty\\flighty\\_driver\\chromedriver-win64-120\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

url = 'https://www.alibaba.ir/'
driver.get(url)
time.sleep(2)
source_tag = driver.find_elements(By.CSS_SELECTOR, '.a-input__input input')
if source_tag:
    source_tag = source_tag[0]
    source_tag.click()
    source_tag.send_keys('اهواز')
    source_tag.submit()
    time.sleep(2)
    print('source tagged')
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=service, options=options)

#Atver saitu
url = "https://www.ss.lv/"
driver.get(url)
time.sleep(2)

#Nospiež pogu - Pieņemt un turpināt
find=driver.find_element(By.XPATH, '//button[text()="Pieņemt un turpināt"]')
find.click()
time.sleep(2)

#Nospiež pogu - viegli auto
find=driver.find_element(By.ID, "mtd_97")
find.click()
time.sleep(2)

#Nospiež pogu -BMW
find=driver.find_element(By.LINK_TEXT, "BMW")
find.click()
time.sleep(2)

#Ievada maksimālo auto cenu - 5000
find=driver.find_element(By.ID, "f_o_8_max")
find.send_keys("5000")

#Nospiež pogu - Meklēt
find = driver.find_element(By.XPATH, "//*[contains(@class, 'b s12')]")
find.click()


import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5)
username="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
password="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
login="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
paul="//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"
logout="//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
time.sleep(3)
driver.find_element_by_xpath(username).send_keys("Admin")
time.sleep(3)
driver.find_element_by_xpath(password).send_keys("admin123")
time.sleep(3)
driver.find_element_by_xpath(login).click()
time.sleep(3)
driver.find_element_by_xpath(paul).click()
time.sleep(3)
driver.find_element_by_xpath(logout).click()


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"(//input[@type='password'])[1]").send_keys("hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("hello@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()


time.sleep(5)
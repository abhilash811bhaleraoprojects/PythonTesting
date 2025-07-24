import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name = "Abhilash"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
#driver.find_element(By.ID, "alertbtn").click()
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
time.sleep(3)
alert_text = alert.text
assert name in alert_text
print(alert_text)
alert.accept()  #this will click on ok button
#alert.dismiss() #this will click on cancel button
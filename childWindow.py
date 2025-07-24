from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
#import time


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windows_Opened = driver.window_handles

driver.switch_to.window(windows_Opened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windows_Opened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
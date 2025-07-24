from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate iframes")
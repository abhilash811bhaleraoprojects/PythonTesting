import time

from selenium.webdriver.support.select import Select

print("hello world")

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element(By.NAME,"email").send_keys("hello@abhilash.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID,"exampleCheck1").click()

#static dropdown handling
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)


#to create a XPATH  and css selector we will use the syntax as follows
#Xpath-- //tagname[@attribute ='value']--> this is a general syntax used to create a XPATH
#CSS-- //tagname[attribute ='value']--> this is a general syntax used to create a CSS Selector
#//input[@type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Abhilash")
driver.find_element(By.XPATH, "//input[@type='submit']").click()


message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello again")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()


time.sleep(5)
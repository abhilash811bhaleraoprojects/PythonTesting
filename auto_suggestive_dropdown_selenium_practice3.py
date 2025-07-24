import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class=ui-menu-item] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

#print(driver.find_element(By.ID,"autosuggest").text)
#above method will not grab the text as we are dynamically providing the text to the script


print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
#above method will print the text that is present in the list

#this method will validate the grabbed text and provided text
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
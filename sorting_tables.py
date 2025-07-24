from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser_sortedList = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#click on columns header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
#collect all veggies list > browser_sortedList
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browser_sortedList.append(ele.text)

originalBrowserSortedList = browser_sortedList.copy()

#sort this browser_sortedList => newSortedList[] => (A, B, C)

browser_sortedList.sort()

assert browser_sortedList == originalBrowserSortedList




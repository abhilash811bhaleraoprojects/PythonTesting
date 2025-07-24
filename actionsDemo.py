from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
actions = ActionChains(driver)
#actions.context_click(driver.find_element(By.ID))  #right click
#actions.double_click(driver.find_element(By.XPATH)) #double click
#actions.click_and_hold() #long press
#actions.drag_and_drop() #drag and drop by providing the source and target webelements into the parenthesis

actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

chrome_options.add_argument("--ignore-certificate-error")

driver =  webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen2.png")
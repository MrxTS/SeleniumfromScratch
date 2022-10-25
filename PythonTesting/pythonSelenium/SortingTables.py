from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")

# chrome_options.add_argument("--ignore-certificate-errors")
browserSortedVeggies = []
service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)

# click on column header
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names -> BrowserSortedveggieList (A, B, C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# Sort this veggieList => newSortedList
browserSortedVeggies.sort()

# BrowserSortedveggieList == newSortedList

assert browserSortedVeggies == originalBrowserSortedList


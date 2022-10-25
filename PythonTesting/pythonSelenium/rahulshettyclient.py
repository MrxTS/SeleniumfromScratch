from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.XPATH, "//p[@class='login-wrapper-footer-text']").click()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Peter")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Pan")
driver.find_element(By.CSS_SELECTOR, "input[id='userEmail']").send_keys("hello@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[id='userMobile']").send_keys("3135693285")
driver.find_element(By.CSS_SELECTOR, "input[value='Male']").click()
driver.find_element(By.XPATH, "//input[@id='userPassword']").send_keys("Peterpan123.")
driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("Peterpan123.")
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
dropdown = Select(driver.find_element(By.XPATH, "//select[@formcontrolname='occupation']"))
dropdown.select_by_value("2: Student")
# driver.find_element(By.CSS_SELECTOR,"input[id='login']").click()

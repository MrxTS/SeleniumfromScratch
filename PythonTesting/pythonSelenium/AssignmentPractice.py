from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver
# --Chrome

service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
copiedEmail = driver.find_element(By.CSS_SELECTOR, ".red").text
print(copiedEmail)
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID, "username").send_keys("mentor@rahulshettyacademy.com")
driver.find_element(By.ID, "password").send_keys("mentor@rahulshettyacademy.com")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()

time = WebDriverWait(driver, 10)
time.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# chrome driver
# --Chrome

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
print(driver.title)
driver.get("https://mein-mmo.de/")
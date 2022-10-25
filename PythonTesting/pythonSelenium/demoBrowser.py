from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver
# --Chrome
service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# --Firefox
# service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)
# --Edge
# service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://mein-mmo.de")
print(driver.title)
print(driver.current_url)
driver.get("https://mein-mmo.de/multiplayer-game-zu-dragonball-release-breakers/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

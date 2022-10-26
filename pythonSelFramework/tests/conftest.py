import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "edge":
        service_obj = Service("/Users/Tuan/Downloads/Selenium Webdriver with Python/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

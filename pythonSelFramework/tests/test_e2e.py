import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        # a[href*='shop'] css version //a[contains(@href.'shop')] xpath version
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        self.driver.find_element(By.ID, "country").send_keys("ger")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Germany")))
        self.driver.find_element(By.LINK_TEXT, "Germany").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successText


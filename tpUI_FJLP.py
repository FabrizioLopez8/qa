import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures('class_setup')
class TestCoffee:

    @pytest.fixture
    def class_setup(self):
        self.driver = webdriver.Edge()
        self.driver.get('https://coffee-cart.app/')
        self.cart = self.driver.find_element(By.XPATH, "//li[contains(., 'cart')]")

    def test_webpage_shows_coffee_selection_and_empty_cart(self):
        coffeeSelection = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/ul[1]') #xpath copiado con click derecho.
        assert "(0)" in self.cart.text
        assert coffeeSelection.is_displayed
        self.driver.quit()

    def test_add_one_coffe_to_cart(self):
        coffee = self.driver.find_element(By.XPATH, "//li[contains(., 'Espresso')]")
        total = self.driver.find_element(By.XPATH, '//button[contains(text(), "Total")]')
        coffee.click()
        assert "(1)" in self.cart.text
        assert "10" in total.text
        self.driver.quit()

    def test_get_extra_coffe(self):
        coffee = self.driver.find_element(By.XPATH, "//li[contains(., 'Espresso')]")
        total = self.driver.find_element(By.XPATH, '//button[contains(text(), "Total")]')
        for i in range(0, 3):
            coffee.click()
        extra_cup = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Yes")]')))
        extra_cup.click()
        assert "(4)" in self.cart.text
        assert "34" in total.text
        self.driver.quit()
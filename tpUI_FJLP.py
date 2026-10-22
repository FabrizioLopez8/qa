import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('class_setup')
class TestCoffee:

    @pytest.fixture
    def class_setup(self):
        self.driver = webdriver.Edge()
        self.driver.get('https://coffee-cart.app/')

    def test_webpage_shows_coffee_selection_and_empty_cart(self):
        cart = self.driver.find_element(By.XPATH, "//*[@id='app']/ul/li[2]/a")
        coffeeSelection = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/ul[1]')
        assert "(0)" in cart.text
        assert coffeeSelection.is_displayed

    def test_add_one_coffe_to_cart(self):
        cart = self.driver.find_element(By.XPATH, "//*[@id='app']/ul/li[2]/a")
        coffee = self.driver.find_element(By.XPATH, "//li[contains(., 'Espresso')]")
        total = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/button')
        coffee.click()
        assert "(1)" in cart.text
        assert "10" in total.text 

    def test_get_extra_coffe(self):
        cart = self.driver.find_element(By.XPATH, "//*[@id='app']/ul/li[2]/a")
        coffee = self.driver.find_element(By.XPATH, "//li[contains(., 'Espresso')]")
        total = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/button')
        for i in range(0, 3):
            coffee.click()
        extra_cup = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/button[1]')
        extra_cup.click()
        assert "(4)" in cart.text
        assert "34" in total.text 
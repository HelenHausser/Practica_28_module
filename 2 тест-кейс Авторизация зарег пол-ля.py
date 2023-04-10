import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_authorization(driver):
    driver.get("https://b2c.passport.rt.ru/")
    login_button = driver.find_element_by_xpath("//a[@href='/login']")
    login_button.click()
    email_field = driver.find_element_by_name("email")
    password_field = driver.find_element_by_name("password")
    email_field.send_keys("user@example.com")
    password_field.send_keys("password123")
    password_field.send_keys(Keys.RETURN)
    assert driver.current_url == "https://b2c.passport.rt.ru/profile"
	
    # мы определяем функцию test_authorization, которая открывает сайт и выполняет авторизацию пользователя. Наконец, мы проверяем, что пользователь успешно авторизовался, сравнивая текущий URL с ожидаемым значением.


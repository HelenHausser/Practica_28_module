import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # здесь можно использовать любой другой драйвер
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_registration(driver):
    driver.get("https://b2c.passport.rt.ru/")
    assert "RT-Пасспорт" in driver.title

    # Нажать кнопку "Регистрация"
    driver.find_element_by_link_text("Регистрация").click()

    # Заполнить поля формы регистрации
    driver.find_element_by_name("lastname").send_keys("Иванов")
    driver.find_element_by_name("firstname").send_keys("Иван")
    driver.find_element_by_name("middlename").send_keys("Иванович")
    driver.find_element_by_name("birthdate").send_keys("01.01.1990")
    driver.find_element_by_name("email").send_keys("ivanov@example.com")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_name("password_confirmation").send_keys("password")

    # Нажать кнопку "Зарегистрироваться"
    driver.find_element_by_name("submit").click()

    # Проверить, что на странице появилось сообщение о том, что на указанный адрес электронной почты отправлено письмо с подтверждением регистрации
    assert "На указанный адрес электронной почты отправлено письмо с подтверждением регистрации." in driver.page_source
    # Тест test_registration открывает сайт, нажимает на кнопку "Регистрация", заполняет форму регистрации, нажимает кнопку "Зарегистрироваться" и проверяет, что на странице появилось сообщение о том, что на указанный адрес электронной почты отправлено письмо с подтверждением регистрации.
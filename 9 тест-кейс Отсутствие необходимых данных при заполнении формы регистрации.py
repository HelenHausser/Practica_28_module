def test_registration_missing_fields():
    # запускаем браузер
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/")

    # находим кнопку регистрации и нажимаем на нее
    register_button = driver.find_element_by_xpath("//a[contains(text(), 'Регистрация')]")
    register_button.click()

    # находим кнопку регистрации и нажимаем на нее
    submit_button = driver.find_element_by_xpath("//button[contains(text(), 'Зарегистрироваться')]")
    submit_button.click()

    # проверяем, что появилось сообщение об ошибке
    error_messages = driver.find_elements_by_xpath("//div[contains(@class, 'error-message')]")
    assert len(error_messages) > 0
    for message in error_messages:
        assert "обязательное поле" in message.text

    # закрываем браузер
    driver.quit()

    # Этот тест запускает браузер, переходит на страницу регистрации, нажимает кнопку "Зарегистрироваться" без заполнения обязательных полей и проверяет, что появляются сообщения об ошибках, указывающие на необходимость заполнения всех обязательных полей.
    
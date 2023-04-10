def test_invalid_login(driver):
    driver.get("https://b2c.passport.rt.ru/")
    login_button = driver.find_element_by_xpath("//button[contains(text(),'Вход')]")
    login_button.click()
    email_input = driver.find_element_by_name("email")
    email_input.send_keys("test@example.com")
    password_input = driver.find_element_by_name("password")
    password_input.send_keys("password")
    submit_button = driver.find_element_by_xpath("//button[contains(text(),'Войти')]")
    submit_button.click()
    error_message = driver.find_element_by_css_selector(".error-message")
    assert error_message.text == "Учетная запись не найдена или пароль неверен."

    # Мы создаем фикстуру driver(), которая создает экземпляр браузера Chrome, открывает сайт https://b2c.passport.rt.ru/ и после выполнения теста закрывает браузер.
    # 
    # Затем мы определяем функцию test_invalid_login(driver), которая использует созданную фикстуру driver() и выполняет следующие шаги:
    # 
    # Находим кнопку "Вход" и кликаем на нее
    # Находим поле для ввода email и вводим в него значение "test@example.com"
    # Находим поле для ввода пароля и вводим в него значение "password"
    # Находим кнопку "Войти" и кликаем на нее
    # Проверяем, что появилось сообщение об ошибке авторизации с текстом "Учетная запись не найдена или пароль неверен."
    # В конце мы используем функцию assert, чтобы убедиться, что текст сообщения об ошибке совпадает с ожидаемым значением. Если текст не совпадает, то тест завершится с ошибкой.
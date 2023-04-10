def test_login_with_incorrect_password():
        # Открыть страницу
    driver.get("https://b2c.passport.rt.ru/")

        # Ввести действительный логин и неверный пароль
    login_field = driver.find_element_by_id("login")
    login_field.send_keys("+79807033610")
    password_field = driver.find_element_by_id("password")
    password_field.send_keys("wrong_password")

        # Нажать кнопку "Войти"
    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

        # Проверить, что появилось сообщение об ошибке
    error_message = driver.find_element_by_css_selector(".error-message")
    assert "Неверный логин или пароль" in error_message.text

    # Вначале открываем страницу, затем вводим логин и неверный пароль, нажимаем кнопку "Войти" и проверяем, что появилось сообщение об ошибке. Если сообщение об ошибке содержит нужный текст, то тест проходит успешно.

def test_empty_login_password():
    # Переходим на страницу авторизации
    driver.get("https://b2c.passport.rt.ru/")

    # Нажимаем на кнопку "Войти" без введения логина и пароля
    login_button = driver.find_element_by_xpath("//a[contains(text(), 'Войти')]")
    login_button.click()

    # Проверяем наличие сообщения об ошибке
    error_message = driver.find_element_by_xpath("//span[@class='form__message-error'][contains(text(),'обязательно')]")
    assert error_message.is_displayed()

    # В данном тест-кейсе мы находим кнопку "Войти" и кликаем по ней без введения логина и пароля. Затем мы проверяем наличие сообщения об ошибке, связанной с отсутствием логина и пароля. Если данное сообщение не найдено, то тест завершится с ошибкой.
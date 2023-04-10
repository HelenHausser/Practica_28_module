def test_invalid_data_format(driver):
    # Ввод некорректных данных в форму
    driver.find_element_by_name("surname").send_keys("Иванов")
    driver.find_element_by_name("name").send_keys("Иван")
    driver.find_element_by_name("patronymic").send_keys("Иванович")
    driver.find_element_by_name("email").send_keys("invalid_email")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_name("password_confirmation").send_keys("password")
    # Отправка формы
    driver.find_element_by_css_selector("button[type='submit']").click()
    # Проверка, что появилось сообщение об ошибке с указанием некорректного поля
    assert "Введите корректный адрес эл.почты" in driver.page_source

    # В тесте test_invalid_data_format производится ввод некорректных данных в форму, после чего производится отправка формы и проверка наличия сообщения об ошибке с указанием некорректного поля.
    
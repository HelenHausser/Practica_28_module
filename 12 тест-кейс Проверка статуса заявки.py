def test_check_application_status():
    # Войти на сайт
    login_url = "https://b2c.passport.rt.ru/"
    driver.get(login_url)

    # Нажать на кнопку "Проверить статус заявки"
    check_status_btn = driver.find_element_by_xpath("//a[@href='/status/']")
    check_status_btn.click()

    # Ввести номер заявки и контактную информацию
    app_num_input = driver.find_element_by_id("application_number")
    app_num_input.send_keys("123456789")
    contact_info_input = driver.find_element_by_id("contact_info")
    contact_info_input.send_keys("example@example.com")

    # Нажать на кнопку "Проверить"
    check_btn = driver.find_element_by_xpath("//button[@type='submit']")
    check_btn.click()

    # Проверить, что на странице отображается статус заявки
    status_msg = driver.find_element_by_xpath("//div[@class='alert alert-info']")
    assert "Статус заявки: " in status_msg.text

    #Здесь мы находим и кликаем на кнопку "Проверить статус заявки", вводим номер заявки и контактную информацию в соответствующие поля, нажимаем кнопку "Проверить" и проверяем, что на странице отображается сообщение о статусе заявки.
    
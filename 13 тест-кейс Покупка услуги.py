def test_purchase_service():
    # Войти на сайт
    login_url = "https://b2c.passport.rt.ru/"
    driver.get(login_url)

    # Выбрать услугу, которую нужно купить
    service_name = "service_name"
    service_btn = driver.find_element_by_xpath(f"//div[contains(text(),'{service_name}')]/../..//button[contains(text(),'Купить')]")
    service_btn.click()

    # Ввести необходимую информацию в поля формы
    fio_input = driver.find_element_by_id("fio")
    fio_input.send_keys("Иванов Иван Иванович")
    contact_info_input = driver.find_element_by_id("contact_info")
    contact_info_input.send_keys("example@example.com")
    birthdate_input = driver.find_element_by_id("birthdate")
    birthdate_input.send_keys("01.01.1980")

    # Нажать на кнопку "Оплатить"
    pay_btn = driver.find_element_by_xpath("//button[contains(text(),'Оплатить')]")
    pay_btn.click()

    # Проверить, что платеж прошел успешно
    success_msg = driver.find_element_by_xpath("//div[contains(text(),'спешно')]")
    assert success_msg.is_displayed()
    assert "перенаправлены на страницу с подтверждением заказа" in success_msg.text

    # В данном тест-кейсе мы используем методы поиска элементов на странице find_element_by_xpath и find_element_by_id, чтобы найти необходимые поля формы и кнопки. Затем мы вводим данные в поля формы и нажимаем на кнопку "Оплатить". Далее мы проверяем, что платеж прошел успешно, и пользователь перенаправлен на страницу с подтверждением заказа.
    
def test_password_recovery_by_sms(browser):
    # Шаг 1
    browser.get("url_for_password_recovery_by_sms")
    assert "password_recovery_by_sms" in browser.current_url
    phone_input = browser.find_element_by_id("phone")
    assert phone_input.is_displayed()
    get_code_button = browser.find_element_by_id("get_code_button")
    assert get_code_button.is_displayed()

    # Шаг 2
    phone_input.send_keys("555-555-5555") # вводим тестовый номер телефона
    get_code_button.click()
    assert "code_sent" in browser.current_url

    # Шаг 3
    code_input = browser.find_element_by_id("code")
    assert code_input.is_displayed()
    continue_button = browser.find_element_by_id("continue_button")
    assert continue_button.is_displayed()
    new_password_input = browser.find_element_by_id("new_password")
    assert new_password_input.is_displayed()
    confirm_password_input = browser.find_element_by_id("confirm_password")
    assert confirm_password_input.is_displayed()
    save_button = browser.find_element_by_id("save_button")
    assert save_button.is_displayed()
    password_rules = browser.find_element_by_id("password_rules")
    assert password_rules.is_displayed()

    # Шаг 4
    new_password_input.send_keys("new_password123")
    confirm_password_input.send_keys("new_password123")
    save_button.click()
    assert "password_recovery_success" in browser.current_url

    # Проверка ошибок при некорректном пароле
    new_password_input.clear()
    confirm_password_input.clear()
    new_password_input.send_keys("password")
    confirm_password_input.send_keys("password")
    save_button.click()
    error_message = browser.find_element_by_id("password_error_message")
    assert error_message.text == "Пароль слишком простой. Используйте более сложный пароль."

    # Проверка ошибки при использовании ранее использованного пароля
    new_password_input.clear()
    confirm_password_input.clear()
    new_password_input.send_keys("old_password")
    confirm_password_input.send_keys("old_password")
    save_button.click()
    error_message = browser.find_element_by_id("password_error_message")
    assert error_message.text == "Вы не можете использовать ранее использованный пароль."

    # Он проверяет каждый шаг сценария восстановления пароля по номеру телефона и убеждается, что каждый элемент на странице отображается правильно и что система обрабатывает ошибки при некорректном вводе пароля.
    
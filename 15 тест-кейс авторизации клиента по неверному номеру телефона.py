def test_auth_phone_number(browser):
    # проверяем наличие кнопки "Вход"
    assert "Вход" in browser.page_source

    # нажимаем на кнопку "Вход"
    browser.find_element_by_link_text("Вход").click()

    # проверяем наличие кнопки "Номер" и поля ввода для номера телефона и пароля
    assert "Номер" in browser.page_source
    assert browser.find_element_by_name("phone")
    assert browser.find_element_by_name("password")

    # вводим некорректный номер телефона и нажимаем на кнопку "Войти"
    browser.find_element_by_name("phone").send_keys("123")
    browser.find_element_by_css_selector(".btn-green").click()

    # проверяем, что система выводит соответствующую ошибку
    assert "Введите корректный номер телефона" in browser.page_source

    # мы проверяем наличие кнопки "Вход" на главной странице, нажимаем на нее и проверяем наличие кнопки "Номер" и полей ввода для номера телефона и пароля на странице авторизации. Затем мы вводим некорректный номер телефона и нажимаем на кнопку "Войти", после чего проверяем, что система выводит соответствующую ошибку.
    
    
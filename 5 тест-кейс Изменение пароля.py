def test_change_password(browser):
    # Открыть сайт https://b2c.passport.rt.ru/
    browser.get('https://b2c.passport.rt.ru/')

    # Войти в личный кабинет зарегистрированного пользователя
    login_link = browser.find_element_by_link_text('Вход')
    login_link.click()

    # Заполнить логин и пароль и нажать кнопку "Войти"
    username_field = browser.find_element_by_name('username')
    password_field = browser.find_element_by_name('password')
    username_field.send_keys('username')
    password_field.send_keys('password')
    password_field.send_keys(Keys.RETURN)

    # Нажать на ссылку "Изменить пароль"
    change_password_link = browser.find_element_by_link_text('Изменить пароль')
    change_password_link.click()

    # Ввести текущий пароль, новый пароль и его подтверждение
    current_password_field = browser.find_element_by_name('old_password')
    new_password_field = browser.find_element_by_name('new_password1')
    confirm_password_field = browser.find_element_by_name('new_password2')
    current_password_field.send_keys('oldpassword')
    new_password_field.send_keys('newpassword')
    confirm_password_field.send_keys('newpassword')

    # Нажать кнопку "Сохранить"
    save_button = browser.find_element_by_css_selector('button[type="submit"]')
    save_button.click()

    # Проверить, что пароль был успешно изменен
    success_message = browser.find_element_by_css_selector('.alert-success')
    assert 'Пароль успешно изменен' in success_message.text
    # Этот тест также открывает сайт, входит в личный кабинет зарегистрированного пользователя, переходит на страницу изменения пароля, вводит данные для изменения пароля и проверяет, что после нажатия кнопки "Сохранить" появляется сообщение об успешном изменении пароля.
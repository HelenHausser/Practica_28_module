def test_correct_login():
    # Запуск браузера
    driver = webdriver.Chrome()

    # Переход на сайт
    driver.get('https://b2c.passport.rt.ru/')

    # Ввод Лицевого счета
    account_number_input = driver.find_element_by_name('accountNumber')
    account_number_input.send_keys('76542158')

    # Ввод пароля
    password_input = driver.find_element_by_name('password')
    password_input.send_keys('Richard')

    # Нажатие на кнопку "Войти"
    login_button = driver.find_element_by_css_selector('.form__submit')
    login_button.click()

    # Проверка успешной авторизации и перехода на страницу личного кабинета
    assert 'Личный кабинет' in driver.title

    # Закрытие браузера
    driver.quit()
    # Данный тест проверяет корректность ввода Лицевого счета и пароля, а также проверяет успешную авторизацию и переход на страницу личного кабинета.
    
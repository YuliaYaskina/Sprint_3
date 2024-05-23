Тесты для Stellar Burgers
Файл test_reg.py создержит автотесты для проверки регистрации: 
    test_registration - проверяет успешную регистрацию
    test_registration_incorrect_password - проверяет ввод пароля, не удовлетворящего условиям

Файл test_logout.py содержит автотесты для проверки выхода из профиля:
    test_logout_from_lk - проверяет логаут из личного кабинета

Файл test_login.py содержит автотесты для проверки логина:
    test_login_from_main - проверяет вход по кнопке «Войти в аккаунт» на главной
    test_login_from_lk_button - проверяет вход через кнопку «Личный кабинет»
    test_login_from_sign_in_button_reg - проверяет вход через кнопку в форме регистрации
    test_login_from_reset_pass_button - проверяет вход через кнопку в форме восстановления пароля

Файл test_lk.py содержит автотесты для проверки переходов в/из Личного кабинета
    test_lk_from_main - проверяет переход по клику на «Личный кабинет»
    test_from_lk_to_constructor - проверяет переход из Личного кабинета в Конструктор
    test_from_lk_to_logo - проверяет переход из Личного кабинета при нажатии на логотип Stellar Burger

Файл test_constructor.py проверяет переход между разделами Конструктора:
    test_sauce - проверяет переход на раздел "Соусы"
    test_stuffing - проверяет переход на раздел "Начинки"
    test_roll - проверяет переход на раздел "Булки"

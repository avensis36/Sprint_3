# Sprint_3
## Список реализованных тестов

### Тесты по регистрации в `test_registration_page.py`

Тест на не пустое поле «Имя» – `test_registration_name_not_empty`

Тест на валидацию почты в поле «Email» – `test_registration_email_is_valid`

Тест на длину пароля от 6 символов включительно в поле «Пароль» – `test_registration_name_not_empty`

Тест на успешную регистрацию – `test_registration_true`

Тест на проверку появления ошибки для некорректного пароля – `test_registration_input_password_less_than_six_symbols_appears_incorrect_password_message`

### Тесты по входу в `test_login_through_buttons_true.py`

Тест на вход по кнопке «Войти в аккаунт» на главной – `test_login_through_login_into_account_button_true`

Тест на вход через кнопку «Личный кабинет» – `test_login_through_personal_account_button_true`

Тест на вход через кнопку в форме регистрации – `test_login_through_login_button_on_register_true`

Тест на вход через кнопку в форме восстановления пароля – `test_login_through_forgot_password_button_true`

### Тесты по личному кабинету в `test_personal_account_page.py`

Тест на переход в личный кабинет по клику на «Личный кабинет» – `test_go_to_personal_account_through_personal_account_button_true`

Тест на выход по кнопке «Выйти» в личном кабинете – `test_exit_from_account_true`

### Тесты по переходу из личного кабинета в конструктор `test_going_to_constructor.py`

Тест на переход по клику на «Конструктор» – `test_click_constructor_button_to_go_to_constructor_from_personal_account_true`

Тест на переход по клику на логотип Stellar Burgers – `test_click_stellar_burger_logo_to_go_to_constructor_from_personal_account_true`

### Тесты по разделу «Конструктор» в `test_go_to_sections_true.py`

Тест на переход к разделу «Булки» – `test_go_to_buns_section_true`

Тест на переход к разделу «Соусы» – `test_go_to_sauces_section_true`

Тест на переход к разделу «Начинки» – `test_go_to_toppings_section_true`

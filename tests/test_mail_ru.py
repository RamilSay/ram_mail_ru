from model.pages.page_mail_ru import login_page


def test_mail_ru(setup_browser):
    login_page.page_auth()  # Авторизация

    login_page.send_mail()  # Пишем письмо и отправляем сообщение

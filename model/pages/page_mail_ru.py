import time, os

from dotenv import load_dotenv
from selene import browser

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
mail_sber = os.getenv('MAIL_SBER')


class LoginPage:

    def __init__(self):
        pass

    #  Авторизация
    def page_auth(self):
        browser.open('https://auth.mail.ru/cgi-bin/auth')
        browser.element('input[name="username"]').type(login).press_enter()
        browser.element('input[placeholder="Пароль"]').type(password).press_enter()
        return self

    #  Пишем письмо и отправляем сообщение
    def send_mail(self):
        browser.element('.compose-button__txt').click()
        browser.element('.container--zU301').type(mail_sber).press_enter()
        browser.element('.container--3QXHv').click()
        browser.element('[name="Subject"]').type('Hello, Andrey')
        browser.element('div[role="textbox"]').type(
            'Привет!\nЭто сообщение отправлено через автотест\nВот ссылка на github')
        browser.element('.vkuiButton__in').click()
        time.sleep(4)
        return self


login_page = LoginPage()

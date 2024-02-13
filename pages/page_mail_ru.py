import time, os

import typing_extensions
from dotenv import load_dotenv
from selene import browser, by, have

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
login_sber = os.getenv('LOGIN_SBER')


class LoginPage:

    def __init__(self):
        pass

    def page_auth(self):
        browser.open('https://auth.mail.ru/cgi-bin/auth')
        browser.element('input[name="username"]').type(login).press_enter()
        browser.element('input[placeholder="Пароль"]').type(password).press_enter()
        return self

    def send_mail(self):
        browser.element('.compose-button__txt').click()
        browser.element('.container--zU301').type(login_sber).press_enter()
        browser.element('.container--3QXHv').click()
        browser.element('[name="Subject"]').type('Hello, Andrey')
        browser.element('div[role="textbox"]').type('Это сообщение отправлено через автотест')
        browser.element('.vkuiButton__in').click()
        time.sleep(5)
        return self


login_page = LoginPage()

import time, os

from dotenv import load_dotenv

from selene import browser

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
mail = os.getenv('MAILa')
auth_url = 'https://account.mail.ru/login'


class LoginPage:

    def __init__(self):
        pass

    #  Авторизация
    def page_auth(self):
        browser.open(auth_url)
        browser.element('input[name="username"]').type(login).press_enter()
        browser.element('input[placeholder="Пароль"]').type(password).press_enter()
        return self

    #  Пишем письмо и отправляем сообщение
    def send_mail(self):
        browser.element('.compose-button__txt').click()
        browser.element('.container--zU301').type(mail).press_enter()
        browser.element('.container--3QXHv').click()

        browser.element('[name="Subject"]').type('Hello, dude from Python')
        browser.element('div[role="textbox"]').type(
            '''Привет!\nЭто сообщение отправлено через автотест.
        \nВот ссылка на github https://github.com/RamilSay/ram_mail_ru'''
        )
        browser.element('.vkuiButton__in').click()
        time.sleep(4)
        return self


login_page = LoginPage()

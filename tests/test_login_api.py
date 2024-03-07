import os
import requests
from dotenv import load_dotenv

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
auth_url = 'https://account.mail.ru/login'

payload = {'username': login, 'password': password, 'RememberMe': False}
headers = {}

def test_login_through_api():
    """ Successful authorization through UI"""
    url = auth_url
   # with allure.step('Open login page')
     response = requests.request("POST", url, data=payload, allow_redirects=False)
     for cookie in response.cookies:
         print(cookie)
         print(response.status_code)

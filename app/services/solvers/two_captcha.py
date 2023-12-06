# -*- coding: utf-8 -*-
# app/services/solvers/two_captcha.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Python default imports.
from requests import get as getr
from os.path import abspath
from random import randint
from time import sleep
from re import search


class TwoCaptcha:
    """Solve reCAPTCHAs using 2Captcha API."""

    def __init__(self, api_key: str) -> None:
        """Get the API key and init the URLs."""
        self.url_in = f'https://2captcha.com/in.php?key={api_key}'
        self.url_res = f'https://2captcha.com/res.php?key={api_key}'

    def get_site_key(self) -> str:
        """Get the reCAPTCHA data sitekey."""
        return search('&k=(.*)&co=', web.visible(
            '(//iframe[@title="reCAPTCHA"])[position()=1]'
        ).get_attribute('src')).group(1)

    def solve(self, web: object) -> bool:
        """Solve the reCAPTCHA."""
        _, callback = get_webdriver(web), web.driver.execute_script(
            open(abspath('app/services/solvers/recaptcha_callback.js'),
                 'r', encoding='utf-8')  # Javascript callback.
            .read() + 'return recaptchaCallback();')
        in_ = getr(f'{self.url_in}&method=userrecaptcha&googlekey='
                   f'{self.get_site_key()}&json=1&invisible=1&pageurl='
                   f'{web.driver.current_url}')
        in_, waiting_time = in_.json().get('request'), 0
        sleep(randint(3, 5))  # Wait between 3 and 5 seconds.
        while True:  # Send requests to 2Captcha.
            res = getr(f'{self.url_res}&action=get&id={in_}&json=1').json()
            if res.get('status') == 1:
                token = res.get('request')
                break  # Token request is correct.
            elif waiting_time >= 120:  # ~2 minutes.
                return False  # Token request is not correct.
            sleep(randint(1, 2))  # Wait between 1 and 2 seconds.
            waiting_time += 1  # Increase the waiting time.
        sleep(randint(3, 5))  # Wait between 3 and 5 seconds.
        web.driver.execute_script('document.getElementById("g-recaptcha'
                                  f'-response").innerHTML="{token}";')
        web.driver.execute_script(f'{callback}("{token}");')
        return True


def get_webdriver(_web: object) -> None:
    """Send the instance of the webdriver."""
    global web
    web = _web

"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.

Version 1.6.12 - 2022, 15 April.

Transfer as many non-fungible tokens as you want to
the OpenSea marketplace. Easy, efficient and fast,
this tool lets you make your life as an Artist of
the digital world much smoother.
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

    def solver(self) -> bool:
        """Solve the reCAPTCHA."""
        callback = web.driver.execute_script(open(abspath(
            'recaptcha_callback.js'), 'r', encoding='utf-8').read()
            + 'return recaptchaCallback();')
        print(callback)
        in_ = getr(f'{self.url_in}&method=userrecaptcha&googlekey='
                   f'{self.get_site_key()}&json=1&invisible=1&pageurl='
                   f'{web.driver.current_url}')
        in_, waiting_time = in_.json().get('request'), 0
        sleep(randint(3, 5))  # Wait between 3 and 5 seconds.
        while True:
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


class Gateway:
    """Gateway between main.py and this file."""

    def __init__(self, api_key: str) -> None:
        """Init the class."""
        global twocaptcha
        twocaptcha = TwoCaptcha(api_key)

    def webdriver(self, webdriver) -> None:
        """Communication between the two script for the webdriver."""
        global web
        web = webdriver

    def proceed(self) -> bool:
        """Gateway between the two scripts to call the proceed method."""
        return twocaptcha.solver()

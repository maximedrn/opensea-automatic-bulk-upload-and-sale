# -*- coding: utf-8 -*-
# app/services/solvers/no_captcha.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Python default imports.
from os.path import abspath


class NoCaptcha:
    """Solve reCAPTCHAs using 2Captcha API."""

    def solve(self, web: object) -> bool:
        """Solve the reCAPTCHA."""
        """if self.counter % 10 == 0:
            self.result(True)  # Check if the license key is valid."""
        callback = web.driver.execute_script(open(abspath(
            'app/services/solvers/recaptcha_callback.js'),
            'r', encoding='utf-8')  # Javascript callback.
            .read() + 'return recaptchaCallback();')
        try:  # Use the exploit.
            web.driver.execute_script(f'{callback}();')
        except Exception:
            pass  # Continue.
        return True  # Success.

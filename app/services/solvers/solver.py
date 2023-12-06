# -*- coding: utf-8 -*-
# app/services/solvers/solver.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Python internal imports.
from ...utils.const import YOLO_ERROR, NO_CAPTCHA_ERROR
from ...utils.func import exit


class Solver:
    """Permit the call of the reCAPTCHA solver according to user choice."""

    def __init__(self, solver: int, key: str) -> None:
        """Get the solver chosen by the user and an API key."""
        self.solver = solver  # Solver number.
        self.key = key  # API key for paid services.

    def init_solver(self) -> None:
        """Init the reCAPTCHA solver according to user choice."""
        if self.solver == 2:  # No reCAPTCHA.
            from .no_captcha import NoCaptcha
            self.recaptcha = NoCaptcha()
        elif self.solver == 3:  # 2Captcha solver.
            from .two_captcha import TwoCaptcha
            self.recaptcha = TwoCaptcha(self.key)
        elif self.solver == 2:  # Yolov5x6 reCAPTPCHA solver.
            try:  # Try to init the reCAPTCHA models.
                from .recaptcha import solver
                self.recaptcha = solver()  # Class object.
            except Exception as error:
                exit(f'{YOLO_ERROR}\n{error}')

    def solve(self, web: object) -> bool:
        """Call the solve() method from the specific solver."""
        return self.recaptcha.solve(web)

#!/usr/bin/python
# app/services/solvers/solver.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Python internal imports.
from ...utils.colors import RESET
from ...utils.func import exit


class Solver:
    """Permit the call of the reCAPTCHA solver according to user choice."""

    def __init__(self, solver: int, key: str) -> None:
        """Get the solver chosen by the user and an API key."""
        self.solver = solver  # Solver number.
        self.key = key  # API key for paid services.

    def init_solver(self) -> None:
        """Init the reCAPTCHA solver according to user choice."""
        if self.solver == 3:  # 2Captcha solver.
            from .two_captcha import TwoCaptcha
            self.recaptcha = TwoCaptcha(self.key)
        elif self.solver == 2:  # Yolov5x6 reCAPTPCHA solver.
            try:  # Try to init the reCAPTCHA models.
                from .recaptcha import solver
                self.recaptcha = solver()  # Class object.
            except Exception as error:
                exit('\nAn error occured while loading Yolov5 and RealESRGAN.'
                     '\nPlease verify that your computer is powerful enough,'
                     '\nevery modules are installed and files are correctly '
                     '\ndownloaded and presents in the right directory.'
                     f'\n{RESET}{error}')

    def solve(self, web: object) -> bool:
        """Call the solve() method from the specific solver."""
        return self.recaptcha.solve(web)

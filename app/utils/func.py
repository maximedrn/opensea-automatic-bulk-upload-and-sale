#!/usr/bin/python
# app/utils/func.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


def cls() -> None:
    """
    Clear console from the command line.

    It uses the default system function:
    - "cls" if system is Windows.
    - "clear" is system is Linux or MacOS.
    """
    # Type the specific command using the system function.
    from os import name, system  # A Python default import.
    system('cls' if name == 'nt' else 'clear')


def exit(message: str = '') -> None:
    """
    Exit and stop the process.

    Call the the exit method from the sys module.
    Change the text color to red before displaying
    the message at the end of the process.
    """
    from sys import exit  # A Python default import.
    from .colors import RED, RESET  # An internal import.
    exit(f'{RED}{message}{RESET}')

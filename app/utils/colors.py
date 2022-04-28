#!/usr/bin/python
# app/utils/colors.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Colorama module: pip install colorama
from colorama import init, Fore, Style


# Create the instance of the Colorama module.
# Convertion and autoreset are activated.
init(convert=True, autoreset=True)

# Set text color to red in the command line.
RED = Fore.RED

# Set text color to green in the command line.
GREEN = Fore.GREEN

# Set text color to yellow in the command line.
YELLOW = Fore.YELLOW

# Reset any color attribute in command line.
RESET = Style.RESET_ALL

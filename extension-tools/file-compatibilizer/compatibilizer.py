"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.

Version 1.0.0 - 2022, 06 April.

Convert a file from a type to an other one.
Arrange a file in a specific order.
"""


# Colorama module: pip install colorama
from colorama import init, Fore, Style

# Python default imports.
from os import name as osname, system as ossystem, mkdir
from os.path import abspath, isdir
from json import loads, dumps
from requests import post
from uuid import uuid4
from glob import glob
from sys import exit


"""Colorama module constants."""
# This module may not work under MacOS.
init(convert=True, autoreset=True)  # Init the Colorama module.
red = Fore.RED  # Red color.
green = Fore.GREEN  # Green color.
yellow = Fore.YELLOW  # Yellow color.
reset = Style.RESET_ALL  # Reset color attribute.


class Arrange:
    """Read files and extract NFTs data. Convert all types into a list."""

    def __init__(self, path: str, _type: str) -> None:
        """Basically open a file and get all NFTs' data."""

    def arrange(self) -> None:
        """Arrange the data in the file."""

    def save(self) -> None:
        """Save the file in the data folder."""


def data_file() -> str:
    """Read the data folder and extract JSON files."""

def file_type() -> list:
    """Ask the file type of the new file."""


def exit_(message: str) -> None:
    """Use the Python exit method with a red text to stop the program."""
    exit(f'{red}{message}{reset}')


def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    ossystem('cls' if osname == 'nt' else 'clear')


if __name__ == '__main__':

    cls()  # Clear console.
    print(f'{green}Created by Maxime Dréan.'
          '\n\nCopyright © 2022 Maxime Dréan. All rights reserved.'
          '\nAny distribution, modification or commercial use is strictly'
          f' prohibited.{reset}\n\n'
          'Buy the full version on Gumroad:\n'
          'https://maximedrn.gumroad.com/l/opensea-collection-compatibilizer')

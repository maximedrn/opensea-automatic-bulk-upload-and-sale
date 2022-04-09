"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.

Version 1.0.0 - 2022, 09 April.

Duplicate values or generate a new file from a generic one.
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


class Generic:
    """."""

    def __init__(self, generic: str, file_type: str,
                 file: str = '', lenght: int = 0) -> None:
        """Get the files details."""

    def open_file(self, path: str):
        """Open in read mode a file and return its content."""

    def save(self) -> None:
        """Save the file in the data folder."""

    def complete_file(self) -> None:
        """Replace empty values of the metadata file with the generic one."""

    def generic_values(self) -> None:
        """Attribute generic values in the class."""

    def change_value(self, value: str, number: int = 0,
                     _bool: bool = False) -> None:
        """Change a value in brackets using the Generic class."""

    def number_to_alphabet(self, number: int, string: str = '') -> str:
        """Change a number to its equal in the alphabet."""

    def add_incrementation(self, value: str, number: int,
                           _type: str, _format: int = 0) -> str:
        """Add incremented value to the value."""


def perform_action() -> list:
    """Suggest multiple actions to the user."""


def file_type() -> list:
    """Ask the file type of the new file."""


def file_lenght() -> int:
    """Ask for the file lenght and return its value."""


def data_file(folder: str) -> str:
    """Read the data folder and extract JSON files."""


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
          'https://maximedrn.gumroad.com/l/opensea-generic-file')

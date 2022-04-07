"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.

Version 1.0.0 - 2022, 04 April.

Scrape an OpenSea collection easily and create a sale file
for the OpenSea upload and sale bot.
"""


# Colorama module: pip install colorama
from colorama import init, Fore, Style

# Python default imports.
from os import name as osname, system as ossystem, popen, mkdir
from pandas import DataFrame, json_normalize
from os.path import isdir, abspath
from json import loads, dumps
from requests import post
from uuid import uuid4
from sys import exit


"""Colorama module constants."""
# This module may not work under MacOS.
init(convert=True, autoreset=True)  # Init the Colorama module.
red = Fore.RED  # Red color.
green = Fore.GREEN  # Green color.
yellow = Fore.YELLOW  # Yellow color.
reset = Style.RESET_ALL  # Reset color attribute.


class Scraper:
    """Scrape an OpenSea collection using JavaScript OpenSea-Scraper."""

    def __init__(self) -> None:
        """Contains details for sale file."""

    def get_collection(self, collection) -> None:
        """Call the JavaScript file and get collection details."""

    def save_to_csv(self) -> None:
        """Convert result to CSV and save it."""

    def save_to_json(self) -> None:
        """Convert result to JSON and save it."""

    def save_to_xlsx(self) -> None:
        """Convert result to XLSX and save it."""


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
          'https://maximedrn.gumroad.com/l/opensea-collection-scraper')

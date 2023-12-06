# -*- coding: utf-8 -*-
# task.py

"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Utils functions for GUI and CLI.
from app.utils.colors import RED, YELLOW, RESET
from app.utils.const import ALL_DONE
from app.utils.func import exit

# Main functions.
from main import main, login, process

# A Python default import.
from argparse import ArgumentParser


def multiprocess(wallet_name: str, password: str, recovery_phrase: str,
                 private_key: str, action: list, solver: int, key: str,
                 browser: int, file: str, browser_path: str) -> None:
    """Call the required functions to start the multiprocess."""
    # Initialize the default classes for the bot.
    wallet, reader, structure, save, recaptcha, delete = main(
        wallet_name, password, recovery_phrase, private_key,
        file, action, solver, key, True)
    process(action, solver, key, structure, save, login(
        wallet, browser, browser_path, wallet_name, solver),
        wallet, recaptcha, reader, delete)  # Start the process.


if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument('--wallet_name', type=str)
        parser.add_argument('--password', type=str)
        parser.add_argument('--recovery_phrase', type=str, required=False)
        parser.add_argument('--private_key', type=str)
        parser.add_argument('--action', type=int, nargs="+")
        parser.add_argument('--solver', type=int, required=False)
        parser.add_argument('--key', type=str, required=False)
        parser.add_argument('--browser', type=int)
        parser.add_argument('--file', type=str)
        parser.add_argument('--browser_path', type=str)
        parser.parse_args()
        multiprocess(**vars(parser.parse_args()))
        print(ALL_DONE)  # Script stops, all done.
    except KeyboardInterrupt:
        print(f'\n\n{YELLOW}The program has been '
              f'stopped by the user.{RESET}')
    except Exception as error:
        print(f'{RED}Something went wrong.{RESET} \n{error}')
    exit()  # Exit the script.

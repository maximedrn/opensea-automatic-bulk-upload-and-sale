#!/usr/bin/python
# divide.py

"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Utils functions for GUI and CLI.
from app.utils.func import cls
from app.utils.colors import RED, YELLOW, RESET
from app.utils.const import FIRST_PAGE, ENTER, SECOND_PAGE
from app.utils.values import UPLOAD, SALE, UPLOAD_AND_SALE

# Utils functions for user choices.
from app.utils.user import perform_action, data_file

# Common functions for the metadata file.
from app.common.reader import Reader
from app.common.structure import Structure
from app.common.save import Save


# Mode and details constants.
MODE = {'1': 'upload', '2': 'sale', '1 2': 'upload_and_sale'}
DETAILS = {'1': UPLOAD, '2': SALE, '1 2': UPLOAD_AND_SALE}


def main() -> None:
    """Open the file and divide according to a number."""
    # What the action the user wants to do.
    action = perform_action()
    action_str = ' '.join(str(element) for element in action)
    file = data_file()  # Metadata file to read.
    reader = Reader(file)
    print(f'\n{YELLOW}{reader.lenght_file} elements.{RESET}')
    # Initialize the Structure class by sending the action.
    structure = Structure(action, reader)
    save = Save(structure)  # Initialize the Save class.
    # Divide the file.
    from_, to_ = number('Start from:') - 1, number('End at:')
    for nft_number in range(from_, to_):
        print(f'Element n°{nft_number}.', end='\r')
        if not structure.get_data(nft_number, True):
            continue  # Remove the error message and continue.
        save.save(MODE[action_str], DETAILS[action_str], True if
                  nft_number != to_ - 1 else False)

def number(question: str) -> int:
    """Ask for a number and return it."""
    while True:
        lenght = input(f'{question} ')
        if lenght.isdigit() and int(lenght) > 0:
            return int(lenght)
        print(f'{RED}Answer must be a strictly positive integer.{RESET}')


if __name__ == '__main__':
    try:
        cls()  # Clear console.
        print(FIRST_PAGE)  # Copyright, licence, author and version.
        input(ENTER)  # Press enter to continue.
        cls()  # Clear console.
        print(SECOND_PAGE)  # Copyright, licence and author.
        main()  # Begin the process.
    except KeyboardInterrupt:
        print(f'\n\n{YELLOW}The program has been '
              f'stopped by the user.{RESET}')
    except Exception as error:
        print(f'{RED}Something went wrong.{RESET} \n{error}')

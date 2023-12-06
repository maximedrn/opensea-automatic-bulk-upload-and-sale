# -*- coding: utf-8 -*-
# order.py

"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Utils functions for GUI and CLI.
from app.utils.func import cls
from app.utils.colors import GREEN, RED, YELLOW, RESET
from app.utils.const import FIRST_PAGE, ENTER, SECOND_PAGE

# Utils functions for user choices.
from app.utils.user import data_file

# Python default imports.
from json import loads, dumps
from re import findall


def main(file_path: str) -> None:
    """Order the elements in a JSON file."""
    # Read the file as a JSON string and get the "nft" part.
    file = loads(open(file_path, 'r', encoding='utf-8').read())['nft']
    order = list(range(0, len(file)))  # List with the length of the file.
    for element in file:  # Get each element of the file.
        # Place the element at the index of its name in the order list.
        order[int(  # NFT name: get only the digits from it.
            findall('[0-9]+', element['nft_name'])[-1]) - 1] = element
        # NFT name: name #{number} -> split at "#" and read the number.
        # Note: use this line below if lines 35/36 do not work!
        # order[int(element['nft_name'].split('#')[1]) - 1] = element
    # Save the file with the new order as a JSON file.
    name = 'data/' + file_path.split('/')[-1].split(
        '.json')[0] + '_order.json'
    open(name, 'w', encoding='utf-8').write(dumps({'nft': order}, indent=4))
    print(f'{GREEN}Saved in {name}{RESET}')


if __name__ == '__main__':
    try:
        cls()  # Clear console.
        print(FIRST_PAGE)  # License, author and version.
        input(ENTER)  # Press enter to continue.
        cls()  # Clear console.
        print(SECOND_PAGE)  # License and author.
        main(data_file())  # Begin the process.
    except KeyboardInterrupt:
        print(f'\n\n{YELLOW}The program has been '
              f'stopped by the user.{RESET}')
    except Exception as error:
        print(f'{RED}Something went wrong.{RESET} \n{error}')

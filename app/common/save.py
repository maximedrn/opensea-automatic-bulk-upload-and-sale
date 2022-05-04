#!/usr/bin/python
# app/common/save.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Python default imports.
from os.path import abspath, isfile
from uuid import uuid4

# Python internal imports.
from ..utils.values import UPLOAD, SALE, UPLOAD_AND_SALE
from ..utils.colors import GREEN, RESET


class Save:
    """
    Retrieve the details of a metadata file and save them to another file.

    If the "Upload only" mode selected, or in case of failure when using
    the tool, the metadata for each NFT is entered or generated.
    They are then saved in a CSV file.
    """

    def __init__(self, structure: object) -> None:
        """Contains default path of file for each mode."""
        self.upload_file = ''
        self.sale_file = ''
        self.upload_and_sale_file = ''
        self.structure = structure  # Get the instance of the Structure class.

    def create_file(self, mode: str, content: str) -> None:
        """Create a file containing data for all NFTs."""
        # Create the metadata file according to the mode selected.
        # "data/" + mode (upload, upload_and_sale, sale) + UUID + ".csv".
        exec(f'self.{mode}_file = "data/{mode}_{str(uuid4())[:8]}.csv"')
        # Open the file and write the headers according to the mode.
        with open(abspath(eval(f'self.{mode}_file')),
                  'a+', encoding='utf-8') as file:
            # Remove the ";;" at the end of the row of headers.
            file.write(content[:-3] if content.endswith(';; ') else content)

    def save(self, mode: str, details: list) -> None:
        """Save the metadata in a CSV file."""
        # Create the file if it doesn't exist.
        if not isfile(abspath(eval(f'self.{mode}_file'))):
            self.create_file(mode, ''.join(
                f'{detail};; ' for detail in details))
        # Open the file and write the details.
        with open(abspath(eval(f'self.{mode}_file')),
                  'a+', encoding='utf-8') as file:
            # Remove the ";;" at the end of each row and replace "\" in
            # each file path by "/" to prevent unknown path error.
            file.write('\n' + ''.join(str(eval(f'self.structure.{detail}', {
                'self': self})).replace('\\', '/') + ';; ' for detail in
                details if hasattr(self.structure, detail))[:-3])
        print(f'{GREEN}Data saved in {eval(f"self.{mode}_file")}.{RESET}')

    def save_upload(self) -> None:
        """Save all the details of the NFT for a new upload."""
        self.save('upload', UPLOAD)

    def save_upload_and_sale(self) -> None:
        """Save all the details of the NFT for a new upload and sale."""
        self.save('upload_and_sale', UPLOAD_AND_SALE)

    def save_sale(self, future: bool = False) -> None:
        """Save all the details of the NFT for a new of future sale."""
        # Set an empty value to the missing sale details.
        [exec(f'self.structure.{detail} = ""' if future else '',
         {'self': self}) for detail in SALE[3:]]
        self.save('sale', SALE)

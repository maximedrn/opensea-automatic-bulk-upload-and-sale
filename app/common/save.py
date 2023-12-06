# -*- coding: utf-8 -*-
# app/common/save.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Python default imports.
from os.path import abspath, isfile
from json import loads, dumps
from uuid import uuid4

# Python internal imports.
from ..utils.values import UPLOAD, SALE, UPLOAD_AND_SALE
from ..utils.colors import GREEN, RED, RESET


class Save:
    """
    Retrieve the details of a metadata file and save them to another file.

    If the "Upload only" mode selected, or in case of failure when using
    the tool, the metadata for each NFT is entered or generated.
    They are then saved in a JSON file.
    """

    def __init__(self, structure: object) -> None:
        """Contains default path of file for each mode."""
        self.upload_file = ''  # Path to the upload file.
        self.sale_file = ''  # Path to the future sale file.
        self.upload_and_sale_file = ''  # Path to the upload and sale file.
        self.structure = structure  # Get the instance of the Structure class.

    def list_to_dict(self, detail: str) -> list:
        """Transform a list into a dictionnary."""
        return [{'type': element[0], 'value': element[1]} for element
                in eval(f'self.structure.{detail}', {'self': self})]

    def create_file(self, mode: str) -> None:
        """Create a file containing data for all NFTs."""
        # Create the metadata file according to the mode selected.
        # "data/" + mode (upload, upload_and_sale, sale) + UUID + ".json".
        exec(f'self.{mode}_file = "data/{mode}_{str(uuid4())[:8]}.json"')
        # Open the file and write the {"nft": []} default content.
        open(abspath(eval(f'self.{mode}_file')), 'a+',
             encoding='utf-8').write(dumps({'nft': []}, indent=4))

    def save(self, mode: str, details: list, mute: bool = False) -> None:
        """Save the metadata in a JSON file."""
        try:
            if not isfile(abspath(eval(f'self.{mode}_file'))):
                self.create_file(mode)  # Create the file if it doesn't exist.
            content = loads(open(abspath(  # Open the file and read content.
                eval(f'self.{mode}_file')), 'r', encoding='utf-8').read())
            content['nft'].append([{detail: ((eval(
                f'self.structure.{detail}', {'self': self}) if detail not in
                ['properties', 'levels', 'stats'] else (self.list_to_dict(
                    detail))) if hasattr(self.structure, detail) else '') for
                detail in details}][0])  # Add the new NFT to the list.
            open(abspath(eval(f'self.{mode}_file')),  # Write the content.
                 'w', encoding='utf-8').write(dumps(content, indent=4))
            if not mute:  # If the user wants to mute the output.
                print(f'{GREEN}Metadata saved in the '
                      f'{eval(f"self.{mode}_file")} file.{RESET}')
        except Exception:  # An error occured while saving the file.
            if not mute:  # If the user wants to mute the output.
                print(f'{RED}Cannot save the metadata in a file.{RESET}')

    def save_upload(self) -> None:
        """Save all the details of the NFT for a new upload."""
        self.save('upload', UPLOAD)

    def save_upload_and_sale(self) -> None:
        """Save all the details of the NFT for a new upload and sale."""
        self.save('upload_and_sale', UPLOAD_AND_SALE)

    def save_sale(self) -> None:
        """Save all the details of the NFT for a new of future sale."""
        self.save('sale', SALE)

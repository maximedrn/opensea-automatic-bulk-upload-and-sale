#!/usr/bin/python
# app/common/reader.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# A Python default import.
from os.path import splitext


class Reader:
    """
    Open and read metadata from JSON, CSV or XLSX file.

    Extract the metadata from the file and arrange it differently
    according to the extension of the file.

    Result for JSON is a list of dictionaries.
    Result for CSV if a list of lists containing strings.
    Result for XLSX is a dictionnary of dictionaries according
    to the pandas.read_excel().to_dict() function.
    """

    def __init__(self, path: str) -> None:
        """
        Get the path of the file.

        Get extension of the file, check if the extension is
        supported and call a function according to the extension.
        """
        self.path = path  # Contains the path of the file.
        # Get the splitted file name (['file', '.txt']).
        # Remove the dot before the extension.
        # Get the extension of the to lowercase (support for MacOS).
        self.extension = splitext(self.path)[1][1:].lower()
        # Check if the extension is supported by the Reader class.
        if self.extension not in ('json', 'csv', 'xlsx'):
            from ..utils.func import exit  # An internal import.
            exit('The file extension is not supported.')
        # Call the right method according to the extension.
        eval(f'self.extract_{self.extension}_file()')

    def extract_json_file(self) -> None:
        """Transform JSON file format to a list of dictionaries."""
        from json import loads  # A Python default import.
        from os.path import abspath  # A Python default import.
        # Load and read the JSON file and extract the "nft" part.
        with open(abspath(self.path), encoding='utf-8') as file:
            self.file = loads(file.read())['nft']
        self.lenght_file = len(self.file)  # Number of elements.

    def extract_csv_file(self) -> None:
        """Transform CSV file format to a list of strings."""
        from os.path import abspath  # A Python default import.
        # Open file, splitlines (every "\n") and remove headers.
        # It gets a list of each rows that are strings.
        with open(abspath(self.path), encoding='utf-8') as file:
            self.file = file.read().splitlines()[1:]
        self.lenght_file = len(self.file)  # Number of elements.

    def extract_xlsx_file(self) -> None:
        """Transform XLSX file format to a dictionnary of dictionnaries."""
        from pandas import read_excel  # Pandas module: pip install pandas
        self.file = read_excel(self.path)  # Read the Excel (XLSX) file.
        self.lenght_file = self.file.shape[0]  # Get number of rows.
        self.file = self.file.to_dict()  # Transform XLSX to a dictionnnary.

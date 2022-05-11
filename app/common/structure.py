#!/usr/bin/python
# app/common/structure.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Python internal imports.
from ..utils.colors import RED, RESET


class Structure:
    """Structure JSON/CSV/XLSX data lists or dictionnaries."""

    def __init__(self, action: list, reader: object) -> None:
        """Make a copy of the readed file and its extension."""
        # It gets a copy of the file from the Reader class as
        # well as its extension both in a tuple.
        self.file, self.extension = reader.file, reader.extension
        self.action = action  # Can be [1], [2] or [1, 2].
        self.structured = False  # If the file is well structured.

    def get_data(self, nft_number: int) -> None:
        """
        Permit to get the NFT's metadata after the process.

        Structure the actual NFT details according to file
        extension. Return a boolean to know if the file is
        well structured or not.
        """
        self.nft_number = nft_number
        # Eval function: self.structure_{FILE_EXTENSION}()
        eval(f'self.structure_{self.extension}()')
        return self.structured

    def structure_json(self) -> None:
        """Transform JSON dictionnaries list to a whole list."""
        nft_data = self.file[self.nft_number]  # Get data by index.
        # Get key's value from the NFT data.
        nft_data = [nft_data[data] for data in nft_data]
        # Take each element in the list and check it.
        # Then structure data by replacing dictionnaries to lists.
        self.structure_data([self.dict_to_list(
            element) for element in nft_data])

    def structure_csv(self) -> None:
        """Transform the CSV file into a list."""
        # Each detail is split every ";;".
        self.structure_data(self.change_type(
            self.file[self.nft_number].split(';;')))

    def structure_xlsx(self) -> None:
        """Transform XLSX file into a list."""
        # Remove "NaN" (= None in Excel) values.
        # Remove useful whitespaces with the strip() method.
        # Call the change_type() method to change the type of elements.
        self.structure_data([element.replace('nan', '').strip(
        ) if isinstance(element, str) else element for element in
            self.change_type([self.file[element].get(
                self.nft_number) for element in self.file])])

    def dict_to_list(self, element: dict or str) -> list or str:
        """Transform a dictionnary into a list. - JSON file method."""
        if isinstance(element, list):  # If the element type is a list.
            return [[item.get(key) for key in item] if isinstance(
                item, dict) else item for item in element]
        return element  # Return the exact same element.

    def change_type(self, nft_data: list) -> list:
        """Change type of element with a literal eval."""
        from ast import literal_eval  # A Python default import.
        _list = []  # List that contains NFT's data.
        for data in nft_data:  # Get each element of NFT's data.
            element = str(data).strip()  # Remove whitespaces.
            try:  # Change the type of element from string to any other one.
                # In case of type is an integer, float, list or boolean.
                _list.append(literal_eval(element))
            except Exception:  # SyntaxError or ValueError.
                # In case of type of the element cannot be changed.
                _list.append(element)  # Append the exact same element.
        return _list  # Return the list of type changed elements.

    def structure_data(self, nft_data: list) -> None:
        """Structure each data of the NFT in a variable."""
        index = 9 if 1 not in self.action else 0  # Remove 9 if "Sale only".
        # Check if the file is well structured or not by checking lenght.
        if (1 in self.action and 2 in self.action and len(nft_data) < 18) \
                or (1 in self.action and len(nft_data) < 12) or \
                (2 in self.action and len(nft_data) < 9) or \
                (3 in self.action and len(nft_data) < 1):
            print(f'{RED}Your file is poorly structured for this NFT.\nCheck '
                  f'that elements are present and in the right order.{RESET}')
            return  # Do not try to structure the file.
        if 1 in self.action:  # Upload details.
            # Set string values to string to prevent different types.
            self.file_path: str or list = nft_data[0]
            self.nft_name: str = str(nft_data[1])
            self.external_link: str = str(nft_data[2])
            self.description: str = str(nft_data[3])
            self.collection: str = str(nft_data[4])
            self.properties: list = nft_data[5]  # [[type, name], ...].
            self.levels: list = nft_data[6]  # [[name, from, to], ...].
            self.stats: list = nft_data[7]  # [[name, from, to], ...].
            self.unlockable_content: list or bool = nft_data[8]  # [bool, str].
            self.explicit_and_sensitive_content: bool = nft_data[9]
            self.supply: int = nft_data[10]
            self.blockchain: str = str(nft_data[11]).capitalize()
        if 2 in self.action:  # Sale details.
            self.sale_type: str = str(nft_data[12 - index]).title()
            self.price: float or int = nft_data[13 - index]
            self.method: list = nft_data[14 - index]  # [method, price].
            self.duration: list or str = nft_data[15 - index]
            self.specific_buyer: list or bool = nft_data[16 - index]
            self.quantity: int = nft_data[17 - index]
        if 2 in self.action and index != 0:  # "Sale only" details.
            self.nft_url: str = str(nft_data[0])
            self.supply: int = nft_data[1]
            self.blockchain: str = str(nft_data[2]).capitalize()
        if 3 in self.action:  # Remove NFTs.
            self.nft_url: str = str(nft_data[0])
        self.structured = True  # File is well structured.

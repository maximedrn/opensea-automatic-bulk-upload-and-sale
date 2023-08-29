#!/usr/bin/python
# app/services/wallets/wallet.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2023 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


class Wallet:
    """
    Allow the connection to OpenSea with different wallets.

    It uses the exec() function to import the wallet class.
    Then it calls the refered method of this wallet class.
    """

    def __init__(self, wallet: int, password: int,
                 recovery_phrase: str, private_key: str) -> None:
        """Get the wallet and connect to the extension/etc."""
        self.recovery_phrase = recovery_phrase  # Get the phrase.
        self.password = password  # Get the new/same password.
        self.private_key = private_key  # Get the account primary key.
        self.wallet = wallet  # Wallet user choice.
        self.fails = 0  # Counter of fails during wallet connection.
        self.success = False  # Boolean returned after login.

    def init_wallet(self, web: object) -> None:
        """Import the wallet class required using exec()."""
        exec(f'from .{self.wallet.replace(" ", "_").lower()}'
             f' import {self.wallet.replace(" ", "")}')
        exec(f'self._wallet = {self.wallet.replace(" ", "")}(web, self)')

    def login(self) -> bool:
        """Connect to OpenSea using a specific wallet."""
        self._wallet.login()
        return self.success

    def sign(self, contract: bool = True, page: int = 2) -> None:
        """Use the method of the wallet to sign the login."""
        self._wallet.sign(contract, page)

    def contract(self, new_contract: bool = False) -> None:
        """Use the method of the wallet to sign the contract."""
        self._wallet.contract(new_contract)

    def close(self) -> None:
        """Close any popup or page opened by an extension."""
        self._wallet.close()

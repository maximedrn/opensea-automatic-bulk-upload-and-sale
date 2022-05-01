#!/usr/bin/python
# main.py

"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.

Version 1.7.2.1 - 2022, 01 May.

Transfer as many non-fungible tokens as you want to
the OpenSea marketplace. Easy, efficient and fast,
this tool lets you make your life as an Artist of
the digital world much smoother.
"""


# Utils functions for GUI and CLI.
from app.utils.func import cls
from app.utils.colors import RED, YELLOW, RESET
from app.utils.const import FIRST_PAGE, ENTER, SECOND_PAGE, \
    PASSWORD, RECOVERY_PHRASE, PRIVATE_KEY, ALL_DONE

# Utils functions for user choices.
from app.utils.user import choose_wallet, read_file, perform_action, \
    recaptcha_solver, choose_browser, data_file

# Common functions for the metadata file.
from app.common.reader import Reader
from app.common.structure import Structure
from app.common.save import Save

# Services functions for Upload/Sale process.
from app.services.webdriver import download_browser, Webdriver
from app.services.wallets.wallet import Wallet
from app.services.processes.login import Login


def login(wallet: object, browser: int, browser_path: str,
          wallet_name: str, solver: int):
    """Login to a specific wallet then to OpenSea."""
    while True:
        web = None  # Prevent Exception.
        try:  # Try to login to a wallet and OpenSea.
            web = Webdriver(browser, browser_path, wallet_name, solver)
            wallet.init_wallet(web)  # Send web instance.
            if wallet.login() and Login(web, wallet).login():
                return web  # Stop the while loop.
        except Exception:  # Stop the browser.
            web.quit() if web is not None else None


def process(action: list, solver: int, key: str, structure: object,
            save: object, web: object, wallet: object,
            recaptcha: object, reader: object) -> None:
    """Begin the upload, listing or both, or any process."""
    if 1 in action:  # Initialize the Upload class.
        from app.services.processes.upload import Upload
        upload = Upload(solver, key, structure, save, web,
                        wallet, recaptcha)
    if 2 in action:  # Initialize the Sale class.
        from app.services.processes.sale import check_price, Sale
        sale = Sale(structure, save, web, wallet)
    # Proceed to the Upload or Sale process in a loop.
    for nft_number in range(reader.lenght_file):
        print(f'\nNFT n°{nft_number + 1}/{reader.lenght_file}:')
        if not structure.get_data(nft_number):
            continue  # Data is not well structured.
        success = None  # Prevent "referenced before assignment" error.
        if 1 in action:  # Upload part.
            success = upload.upload()  # Get the result of the upload.
        if (2 in action and success) or action == [2]:  # Sale part.
            # Check the price validity by sending price and blockchain.
            if check_price(structure.price, structure.blockchain):
                sale.sale()  # Process to listing of the NFT.
    web.quit()  # Stop the webdriver.


def user() -> tuple:
    """Ask different informations to the user."""
    wallet_name = choose_wallet()  # Choose a wallet.
    # User wallet credentials.
    password = read_file('password', PASSWORD)
    recovery_phrase = read_file('recovery_phrase', RECOVERY_PHRASE)
    private_key = read_file('private_key', PRIVATE_KEY)
    # What the action the user wants to do.
    action = perform_action()
    # Ask what solver the user wants to use.
    solver, key = recaptcha_solver() if 1 in action else ('', '')
    # Ask what browser the user wants to use
    # if the Coinbase Wallet is not selected.
    browser = 0 if wallet_name == 'Coinbase Wallet' \
        else choose_browser(solver)
    file = data_file()  # Metadata file to read.
    return wallet_name, password, recovery_phrase, private_key, \
        action, solver, key, browser, file


def main(wallet_name: str, password: str, recovery_phrase: str,
         private_key: str, file: str, action: list, solver: int,
         key: str) -> tuple:
    """Initialize default classes for the bot."""
    # Initialize the wallet by sending credentials.
    wallet = Wallet(wallet_name, password, recovery_phrase, private_key)
    # Initialize the Reader class by sending the file to read.
    reader = Reader(file)
    # Initialize the Structure class by sending the action.
    structure = Structure(action, reader)
    save = Save(structure)  # Initialize the Save class.
    # Initialize the solver by sending which
    # solver to use and an API key if it is necessary.
    recaptcha = None
    if 1 in action:
        from app.services.solvers.solver import Solver
        recaptcha = Solver(solver, key)
        recaptcha.init_solver()  # Send web instance.
    return wallet, reader, structure, save, recaptcha


if __name__ == '__main__':
    try:
        cls()  # Clear console.
        print(FIRST_PAGE)  # Copyright, licence, author and version.
        input(ENTER)  # Press enter to continue.
        cls()  # Clear console.
        print(SECOND_PAGE)  # Copyright, licence and author.
        # Get user informations and choices.
        wallet_name, password, recovery_phrase, private_key, \
            action, solver, key, browser, file = user()
        cls()  # Clear console.
        browser_path = download_browser(browser)  # Download the webdriver.
        # Initialize the default classes for the bot.
        wallet, reader, structure, save, recaptcha = main(
            wallet_name, password, recovery_phrase, private_key,
            file, action, solver, key)
        cls()  # Clear console.
        process(action, solver, key, structure, save, login(
            wallet, browser, browser_path, wallet_name, solver),
            wallet, recaptcha, reader)  # Start the process.
        print(ALL_DONE)  # Script stops, all done.
    except KeyboardInterrupt:
        print(f'\n\n{YELLOW}The program has been '
              f'stopped by the user.{RESET}')
    except Exception as error:
        print(f'{RED}Something went wrong.{RESET} \n{error}')

#!/usr/bin/python
# app/utils/const.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn

Copyright © 2022 Maxime Dréan. All rights reserved.
Any distribution, modification or commercial use is strictly prohibited.
"""


# Python internal imports.
from .colors import GREEN, YELLOW, RESET
from .user import check_version


VERSION = '1.12.16'

# Change this with any values.
# 1 means 2 failures allowed.
# 9 means 10 failures allowed.
UPLOAD_FAILS = 1
SALE_FAILS = 1

FIRST_PAGE = (
    f'{GREEN}Created by Maxime Dréan.'
    '\nGithub: https://github.com/maximedrn'
    '\nTelegram: https://t.me/maximedrn'
    '\nYouTube: https://www.youtube.com/channel/UCoqpR1OLb'
    'swIyQVatKBoGxA'
    '\nEthereum: 0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E'
    '\n\nCopyright © 2023 Maxime Dréan. All rights reserved.'
    '\nAny distribution, modification or commercial use '
    'is strictly prohibited.'
    f'\n\nVersion {VERSION} - 2023, 22 March.{RESET}'
    f'{check_version(VERSION)}'  # Check for a new update of the bot.
    '\n\nAdd-ons available here: https://maximedrn.gumroad.com/'
    '\nJOIN ME ON TELEGRAM: https://t.me/opensea_bulk_upload_and_sale'
    '\n\nIf you face any problem, please open an issue.')

ENTER = '\nPRESS [ENTER] TO CONTINUE. '

SECOND_PAGE = (
    f'{GREEN}Created by Maxime Dréan.'
    '\nCopyright © 2023 Maxime Dréan. All rights reserved.'
    '\nAny distribution, modification or commercial use '
    f'is strictly prohibited.{RESET}'
    '\n\nAdd-ons available here: https://maximedrn.gumroad.com/'
    '\nJOIN ME ON TELEGRAM: https://t.me/opensea_bulk_upload_and_sale')

STARTING_VALUE = '\nStart from the item n°'

PASSWORD = (
    '\nWhat is your wallet password? '
    '(Press [ENTER] to do it manually) ')

RECOVERY_PHRASE = (
    '\nWhat is your wallet recovery phrase? '
    '(Press [ENTER] to do it manually) ')

PRIVATE_KEY = (
    '\nWhat is your account number or private key? '
    '(Press [ENTER] to ignore this step) ')

USER_DATA = '\nWhat is the "Chrome/User Data/" path? '

PROFILE = '\nWhat is your Google Chrome profile name? '

METAMASK_IMPORT = f'{YELLOW}Press [ENTER] when "Import" button is clicked.'

METAMASK_RECONNECT = f'{YELLOW}Press [ENTER] when "Unlock" button is clicked.'

COINBASE_WALLET_IMPORT = \
    f'{YELLOW}Press [ENTER] when "Submit" button is clicked.'

NO_DELETE_ERROR = (
    'Cannot found the file. Please check that you placed it in the'
    '\napp/services/processes/delete.py path or that you purchased'
    '\nthis extension. (available here: '
    'https://maximedrn.gumroad.com/l/opensea-deletion)')

YOLO_ERROR = (
    '\nAn error occured while loading Yolov5 and RealESRGAN.'
    '\nPlease verify that your computer is powerful enough,'
    '\nevery modules are installed and files are correctly '
    f'\ndownloaded and presents in the right directory.\n{RESET}')

NO_CAPTCHA_ERROR = (
    'Cannot found the file. Please check that you placed it in the\n'
    'app/services/solvers/no_captcha.py path or that you purchased'
    '\nthis extension. (available here: '
    'https://maximedrn.gumroad.com/l/opensea-no-recaptcha)')

ALL_DONE = (
    f'\n{GREEN}All done!{RESET}'
    '\nIn order to support me, you can make donations at this address:'
    '\n0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E (Ethereum).')

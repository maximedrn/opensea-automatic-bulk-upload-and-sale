# -*- coding: utf-8 -*-
# app/utils/const.py


"""
@author: Maxime Dréan.

Github: https://github.com/maximedrn
Telegram: https://t.me/maximedrn
"""


# Python internal imports.
from .colors import GREEN, YELLOW, RESET
from .user import check_version


VERSION = '1.13.0'

# Change this with any values.
# 1 means 2 failures allowed.
# 9 means 10 failures allowed.
UPLOAD_FAILS = 1
SALE_FAILS = 1

FIRST_PAGE = (
    f'{GREEN}Created by Maxime Dréan.'
    '\nGithub: https://github.com/maximedrn'
    '\nTelegram: https://t.me/maximedrn'
    f'\n\nVersion {VERSION} - 2023, 06 December.{RESET}'
    f'{check_version(VERSION)}'  # Check for a new update of the bot.
    '\n\nIf you face any problem, please open an issue.')

ENTER = '\nPRESS [ENTER] TO CONTINUE. '

SECOND_PAGE = f'{GREEN}Created by Maxime Dréan.'

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

ALL_DONE = f'\n{GREEN}All done!{RESET}'

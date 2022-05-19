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


FIRST_PAGE = (
    f'{GREEN}Created by Maxime Dréan.'
    '\nGithub: https://github.com/maximedrn'
    '\nTelegram: https://t.me/maximedrn'
    '\nEthereum: 0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E'
    '\n\nCopyright © 2022 Maxime Dréan. All rights reserved.'
    '\nAny distribution, modification or commercial use '
    'is strictly prohibited.'
    f'\n\nVersion 1.7.12 - 2022, 19 May.{RESET}'
    '\n\nIf you face any problem, please open an issue.')

ENTER = '\nPRESS [ENTER] TO CONTINUE. '

SECOND_PAGE = (
    f'{GREEN}Created by Maxime Dréan.'
    '\nCopyright © 2022 Maxime Dréan. All rights reserved.'
    '\nAny distribution, modification or commercial use '
    f'is strictly prohibited.{RESET}'
    '\n\nExtension tools available here: https://maximedrn.gumroad.com/'
    '\nTutorials on YouTube: https://www.youtube.com/channel/UCoqpR1OLb'
    'swIyQVatKBoGxA')

PASSWORD = (
    '\nWhat is your wallet password? '
    '(Press [ENTER] to do it manually) ')

RECOVERY_PHRASE = (
    '\nWhat is your wallet recovery phrase? '
    '(Press [ENTER] to do it manually) ')

PRIVATE_KEY = (
    '\nWhat is your account number? '
    '(Press [ENTER] to ignore this step) ')

METAMASK_IMPORT = f'{YELLOW}Press [ENTER] when "Import" button is clicked.'
COINBASE_WALLET_IMPORT = \
    f'{YELLOW}Press [ENTER] when "Submit" button is clicked.'

NO_DELETE_ERROR = (
    'Cannot found the file. Please check that you placed it correctly or'
    ' that you purchased this extension. (available here: '
    'https://maximedrn.gumroad.com/l/opensea-deletion)')

YOLO_ERROR = (
    '\nAn error occured while loading Yolov5 and RealESRGAN.'
    '\nPlease verify that your computer is powerful enough,'
    '\nevery modules are installed and files are correctly '
    f'\ndownloaded and presents in the right directory.\n{RESET}')

NO_CAPTCHA_ERROR = (
    'Cannot found the file. Please check that you placed it correctly or'
    ' that you purchased this extension. (available here: '
    'https://maximedrn.gumroad.com/l/opensea-recaptcha-bypasser)')

ALL_DONE = (
    f'\n{GREEN}All done!{RESET}'
    '\nIn order to support me, you can make donations at this address:'
    '\n0xDD135d5be0a23f6daAAE7D2d0580828c9e09402E (Ethereum).')
